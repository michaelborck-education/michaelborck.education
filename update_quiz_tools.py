#!/usr/bin/env python3
"""
Quiz Tool Update Script
Automatically parses index.html and updates the recommendation engine with current tools
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any
import sys

class QuizToolUpdater:
    def __init__(self, html_file: str = "index.html", js_file: str = "recommendation_engine.js"):
        self.html_file = Path(html_file)
        self.js_file = Path(js_file)
        
        # Teaching context mapping rules
        self.context_rules = {
            'content_creation': [
                'curriculum', 'content', 'presentation', 'case studies', 'brief', 'slide', 'docs',
                'docslanding', 'curator', 'creative', 'material'
            ],
            'student_interaction': [
                'interaction', 'poll', 'audience', 'pulse', 'engage', 'clone', 'real-time',
                'interactive', 'live', 'participation'
            ],
            'assessment_feedback': [
                'feedback', 'forward', 'insight', 'analysis', 'survey', 'lens', 'assessment',
                'evaluation', 'analytics', 'performance', 'grade'
            ],
            'language_communication': [
                'talk', 'conversation', 'english', 'communication', 'voice', 'transcription',
                'language', 'speech', 'pronunciation', 'chat'
            ],
            'technical_education': [
                'python', 'programming', 'code', 'dev', 'calculator', 'weather', 'paradigms',
                'technical', 'tutorial', 'coding', 'algorithm', 'software'
            ],
            'project_management': [
                'project', 'management', 'capstone', 'connect', 'venture', 'business', 'industry',
                'enterprise', 'collaboration', 'workflow'
            ],
            'ai_tutoring': [
                'ai', 'tutor', 'buddy', 'intelligent', 'personalized', 'adaptive', 'smart',
                'chatbot', 'assistant', 'guide'
            ],
            'utility': [
                'toolkit', 'utils', 'helper', 'tool', 'utility', 'link', 'url', 'general'
            ]
        }
        
        # Technical level indicators
        self.tech_level_rules = {
            'beginner': [
                'beginner', 'jumpstart', 'learn', 'tutorial', 'guide', 'minimum', 'buddy',
                'simple', 'easy', 'basic', 'intro'
            ],
            'advanced': [
                'docker', 'api', 'framework', 'infrastructure', 'electron', 'cms', 'ollama',
                'advanced', 'expert', 'complex', 'professional'
            ]
            # Everything else defaults to 'intermediate'
        }
        
        # Teaching context indicators
        self.context_indicators = {
            'university': ['university', 'lecturer', 'college', 'academic', 'higher education'],
            'k12': ['k12', 'school', 'classroom', 'student', 'primary', 'secondary'],
            'corporate': ['corporate', 'business', 'professional', 'workplace', 'enterprise'],
            'self_directed': ['self', 'independent', 'personal', 'individual']
        }
        
        # Subject area indicators
        self.subject_indicators = {
            'technology': ['python', 'programming', 'code', 'tech', 'software', 'development'],
            'business': ['business', 'venture', 'enterprise', 'management', 'entrepreneurship'],
            'communication': ['communication', 'language', 'speech', 'conversation', 'presentation'],
            'general': ['general', 'multi', 'broad', 'diverse', 'various']
        }
        
        # Role-based classification rules
        self.role_indicators = {
            'lecturer': [
                'teaching', 'instructor', 'classroom', 'curriculum', 'assessment', 'grading', 
                'presentation', 'lecture', 'course', 'educational', 'pedagogy', 'feedback',
                'management', 'analysis', 'evaluation', 'design', 'create', 'develop'
            ],
            'student': [
                'learning', 'study', 'practice', 'tutorial', 'buddy', 'guide', 'beginner',
                'jumpstart', 'learn', 'self-directed', 'training', 'skill', 'exercise',
                'interactive', 'help', 'support', 'personal'
            ],
            'researcher': [
                'analysis', 'data', 'research', 'survey', 'insight', 'analytics', 'modeling',
                'simulation', 'processing', 'investigation', 'exploration', 'discovery',
                'evaluation', 'measurement', 'statistical', 'scientific'
            ]
        }

    def extract_tools_from_html(self) -> List[Dict[str, Any]]:
        """Extract all tools from the HTML file"""
        if not self.html_file.exists():
            raise FileNotFoundError(f"HTML file not found: {self.html_file}")
        
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tools = []
        
        # Find all repo-card blocks using a more flexible pattern
        card_pattern = r'<div[^>]*class="[^"]*repo-card[^"]*"[^>]*data-category="([^"]*)"[^>]*data-name="([^"]*)"[^>]*data-description="([^"]*)"[^>]*(?:data-topics="([^"]*)")?[^>]*>'
        
        matches = re.findall(card_pattern, content, re.DOTALL)
        
        for match in matches:
            category, name, description, topics = match
            
            # Skip category filter buttons
            if name in ['all', 'desktop-application', 'web-application', 'python-package', 
                       'learning-resource', 'infrastructure-tool', 'command-line-tool']:
                continue
            
            tools.append({
                'name': name,
                'original_category': category,
                'description': description.lower().strip(),
                'topics': topics.lower().strip() if topics else ''
            })
        
        # If regex fails, try alternative extraction
        if not tools:
            tools = self._extract_tools_alternative(content)
        
        return tools

    def _extract_tools_alternative(self, content: str) -> List[Dict[str, Any]]:
        """Alternative extraction method using line-by-line parsing"""
        tools = []
        lines = content.split('\n')
        
        current_tool = {}
        in_card = False
        
        for line in lines:
            line = line.strip()
            
            if 'repo-card' in line and 'data-category=' in line:
                in_card = True
                current_tool = {}
                
                # Extract data attributes
                category_match = re.search(r'data-category="([^"]*)"', line)
                name_match = re.search(r'data-name="([^"]*)"', line)
                desc_match = re.search(r'data-description="([^"]*)"', line)
                topics_match = re.search(r'data-topics="([^"]*)"', line)
                
                if category_match and name_match:
                    current_tool['name'] = name_match.group(1)
                    current_tool['original_category'] = category_match.group(1)
                    current_tool['description'] = desc_match.group(1).lower() if desc_match else ''
                    current_tool['topics'] = topics_match.group(1).lower() if topics_match else ''
                    
                    # Skip category buttons
                    if current_tool['name'] not in ['all', 'desktop-application', 'web-application', 
                                                   'python-package', 'learning-resource', 
                                                   'infrastructure-tool', 'command-line-tool']:
                        tools.append(current_tool)
                    
                    in_card = False
        
        return tools

    def classify_role(self, tool: Dict[str, Any]) -> Dict[str, Any]:
        """Classify tool by target user roles with confidence scoring"""
        text_to_analyze = f"{tool['description']} {tool['topics']}"
        role_scores = {}
        
        for role, keywords in self.role_indicators.items():
            score = 0
            for keyword in keywords:
                if keyword in text_to_analyze:
                    score += 1
            role_scores[role] = score
        
        # Determine primary roles (with confidence levels)
        max_score = max(role_scores.values()) if role_scores.values() else 0
        roles = []
        
        for role, score in role_scores.items():
            if score > 0:
                # Calculate confidence: high (75%+), medium (50%+), low (<50%)
                confidence_ratio = score / max_score if max_score > 0 else 0
                if confidence_ratio >= 0.75:
                    confidence = 'high'
                elif confidence_ratio >= 0.5:
                    confidence = 'medium'
                else:
                    confidence = 'low'
                
                roles.append({'role': role, 'confidence': confidence, 'score': score})
        
        # Default fallback - if no clear role indicators, assign based on category
        if not roles:
            if tool['original_category'] in ['desktop-application', 'infrastructure-tool']:
                roles.append({'role': 'lecturer', 'confidence': 'low', 'score': 0})
            elif 'python-package' in tool['original_category'] or 'learning' in text_to_analyze:
                roles.append({'role': 'student', 'confidence': 'low', 'score': 0})
            else:
                roles.append({'role': 'lecturer', 'confidence': 'low', 'score': 0})
        
        return {
            'roles': roles,
            'primary_role': roles[0]['role'] if roles else 'lecturer'
        }

    def categorize_tool(self, tool: Dict[str, Any]) -> Dict[str, Any]:
        """Categorize a tool based on its name and description"""
        name_lower = tool['name'].lower()
        desc_lower = tool['description'].lower()
        text_to_analyze = f"{name_lower} {desc_lower} {tool['topics']}"
        
        # Determine teaching category
        teaching_category = 'content_creation'  # default
        max_score = 0
        
        for category, keywords in self.context_rules.items():
            score = sum(1 for keyword in keywords if keyword in text_to_analyze)
            if score > max_score:
                max_score = score
                teaching_category = category
        
        # Determine technical level
        tech_level = 'intermediate'  # default
        for level, keywords in self.tech_level_rules.items():
            if any(keyword in text_to_analyze for keyword in keywords):
                tech_level = level
                break
        
        # Determine teaching contexts
        contexts = ['general']  # default
        for context, keywords in self.context_indicators.items():
            if any(keyword in text_to_analyze for keyword in keywords):
                contexts = [context]
                break
        
        # Determine subjects
        subjects = ['general']  # default
        for subject, keywords in self.subject_indicators.items():
            if any(keyword in text_to_analyze for keyword in keywords):
                subjects = [subject]
                break
        
        # Determine priority based on category and usefulness
        priority = 'medium'  # default
        high_priority_tools = [
            'critique-quest', 'curriculum-curator', 'deep-brief', 'python-jumpstart',
            'hands-on-ai', 'insight-lens', 'feed-forward', 'capstone-connect',
            'venture-lab', 'study-buddy', 'talk-buddy', 'class-pulse'
        ]
        
        if tool['name'] in high_priority_tools:
            priority = 'high'
        elif teaching_category in ['utility', 'infrastructure']:
            priority = 'low'
        
        # Classify by user roles
        role_classification = self.classify_role(tool)
        
        return {
            'name': tool['name'].replace('-', ' ').title().replace(' ', ''),
            'display_name': tool['name'].replace('-', ' ').title(),
            'category': teaching_category,
            'description': self._clean_description(tool['description']),
            'priority': priority,
            'techLevel': tech_level,
            'contexts': contexts,
            'subjects': subjects,
            'original_category': tool['original_category'],
            'roles': role_classification['roles'],
            'primary_role': role_classification['primary_role']
        }

    def _clean_description(self, description: str) -> str:
        """Clean and format the description"""
        # Capitalize first letter and ensure proper sentence structure
        desc = description.strip()
        if desc:
            desc = desc[0].upper() + desc[1:] if len(desc) > 1 else desc.upper()
            if not desc.endswith('.'):
                desc += '.'
        return desc

    def generate_js_tools_object(self, tools: List[Dict[str, Any]]) -> str:
        """Generate the JavaScript tools object string"""
        js_tools = {}
        
        for tool in tools:
            tool_id = tool['name'].lower().replace(' ', '')
            js_tools[tool_id] = {
                'name': tool['display_name'],
                'category': tool['category'],
                'description': tool['description'],
                'priority': tool['priority'],
                'techLevel': tool['techLevel'],
                'contexts': tool['contexts'],
                'subjects': tool['subjects']
            }
        
        # Convert to JavaScript object format
        js_code = "{\n"
        for tool_id, tool_data in js_tools.items():
            js_code += f"            '{tool_id}': {{\n"
            js_code += f"                name: '{tool_data['name']}',\n"
            js_code += f"                category: '{tool_data['category']}',\n"
            js_code += f"                description: '{tool_data['description']}',\n"
            js_code += f"                priority: '{tool_data['priority']}',\n"
            js_code += f"                techLevel: '{tool_data['techLevel']}',\n"
            js_code += f"                contexts: {json.dumps(tool_data['contexts'])},\n"
            js_code += f"                subjects: {json.dumps(tool_data['subjects'])}\n"
            js_code += "            },\n"
        js_code = js_code.rstrip(',\n') + "\n        }"
        
        return js_code

    def update_js_file(self, tools: List[Dict[str, Any]]) -> None:
        """Update the JavaScript file with new tools"""
        if not self.js_file.exists():
            raise FileNotFoundError(f"JavaScript file not found: {self.js_file}")
        
        with open(self.js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        # Generate new tools object
        new_tools_js = self.generate_js_tools_object(tools)
        
        # Replace the tools object in the JavaScript file
        # Find the initializeTools() method and replace its return statement
        pattern = r'(initializeTools\(\) \{[\s\n]*return )(\{.*?\});'
        replacement = f'\\1{new_tools_js};'
        
        updated_content = re.sub(pattern, replacement, js_content, flags=re.DOTALL)
        
        # Write updated content back to file
        with open(self.js_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)

    def update_html_file(self, tools: List[Dict[str, Any]]) -> None:
        """Update HTML file with role data attributes and remove redundant quiz button"""
        if not self.html_file.exists():
            raise FileNotFoundError(f"HTML file not found: {self.html_file}")
        
        with open(self.html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Remove redundant "Take Quiz" button from navigation
        html_content = self._remove_redundant_quiz_button(html_content)
        
        # Add role filter buttons
        html_content = self._add_role_filter_buttons(html_content)
        
        # Add role data attributes to tool cards
        html_content = self._add_role_attributes(html_content, tools)
        
        # Add JavaScript for role filtering
        html_content = self._add_role_filtering_javascript(html_content)
        
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

    def _remove_redundant_quiz_button(self, html_content: str) -> str:
        """Remove the redundant Take Quiz button from navigation filters"""
        # Pattern to match the quiz button in navigation
        pattern = r'<a href="educational-tools-quiz\.html" class="[^"]*">🎯 Take Quiz</a>\s*'
        updated_content = re.sub(pattern, '', html_content)
        return updated_content

    def _add_role_filter_buttons(self, html_content: str) -> str:
        """Add role-based filter buttons to navigation"""
        # Find the navigation section and add role buttons
        role_buttons = '''
                <div class="mt-2 flex flex-wrap gap-2 justify-center border-t pt-2">
                    <span class="text-sm text-gray-600 px-2 py-1">Filter by Role:</span>
                    <button onclick="filterByRole('all')" class="role-btn px-3 py-1 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition text-sm" data-role="all">All Roles</button>
                    <button onclick="filterByRole('lecturer')" class="role-btn px-3 py-1 bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200 transition text-sm" data-role="lecturer">For Lecturers</button>
                    <button onclick="filterByRole('student')" class="role-btn px-3 py-1 bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200 transition text-sm" data-role="student">For Students</button>
                    <button onclick="filterByRole('researcher')" class="role-btn px-3 py-1 bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200 transition text-sm" data-role="researcher">For Researchers</button>
                </div>'''
        
        # Insert role buttons after the category navigation
        pattern = r'(</nav>)'
        replacement = f'{role_buttons}\n            </div>\n        \\1'
        updated_content = re.sub(pattern, replacement, html_content)
        return updated_content

    def _add_role_attributes(self, html_content: str, tools: List[Dict[str, Any]]) -> str:
        """Add role data attributes to tool cards"""
        # Create a mapping of tool names to their role data
        tool_roles = {}
        for tool in tools:
            tool_name = tool['name'].replace(' ', '').lower().replace('-', '')
            original_name = tool['display_name'].lower().replace(' ', '-')
            
            # Create role strings for data attributes
            role_list = [role['role'] for role in tool['roles']]
            confidence_list = [f"{role['role']}:{role['confidence']}" for role in tool['roles']]
            
            tool_roles[original_name] = {
                'roles': ' '.join(role_list),
                'primary_role': tool['primary_role'],
                'role_confidence': ' '.join(confidence_list)
            }
        
        # Add role attributes to each tool card
        for tool_name, role_data in tool_roles.items():
            # Pattern to find the specific tool card
            pattern = rf'(<div[^>]*class="[^"]*repo-card[^"]*"[^>]*data-name="{re.escape(tool_name)}"[^>]*)(>)'
            
            # Add role data attributes
            role_attrs = f' data-roles="{role_data["roles"]}" data-primary-role="{role_data["primary_role"]}" data-role-confidence="{role_data["role_confidence"]}"'
            replacement = f'\\1{role_attrs}\\2'
            
            html_content = re.sub(pattern, replacement, html_content)
        
        return html_content

    def _add_role_filtering_javascript(self, html_content: str) -> str:
        """Add JavaScript function for role-based filtering"""
        role_filter_js = '''
        
        // Role filtering functionality
        let currentRole = 'all';
        
        function filterByRole(role) {
            currentRole = role;
            
            // Update button styles
            document.querySelectorAll('.role-btn').forEach(btn => {
                if (btn.dataset.role === role) {
                    btn.className = 'role-btn px-3 py-1 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition text-sm';
                } else {
                    btn.className = 'role-btn px-3 py-1 bg-blue-100 text-blue-700 rounded-full hover:bg-blue-200 transition text-sm';
                }
            });
            
            // Filter cards
            let visibleCount = 0;
            
            allCards.forEach(card => {
                const searchableText = 
                    card.dataset.name + ' ' + 
                    card.dataset.description + ' ' + 
                    card.dataset.topics;
                
                const searchTerms = searchInput.value.toLowerCase()
                    .split(' ')
                    .filter(term => term.length > 0);
                
                const matchesCategory = currentCategory === 'all' || card.dataset.category === currentCategory;
                const matchesSearch = searchTerms.length === 0 || 
                    searchTerms.every(term => searchableText.includes(term));
                
                // Check if card matches role filter
                let matchesRole = true;
                if (role !== 'all' && card.dataset.roles) {
                    const cardRoles = card.dataset.roles.split(' ');
                    matchesRole = cardRoles.includes(role);
                }
                
                if (matchesCategory && matchesSearch && matchesRole) {
                    card.style.display = 'block';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });
            
            // Smooth scroll to results
            document.querySelector('main').scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        
        // Update existing filterByCategory to respect role filters
        const originalFilterByCategory = filterByCategory;
        filterByCategory = function(category) {
            currentCategory = category;
            
            // Update button styles
            document.querySelectorAll('.category-btn').forEach(btn => {
                if (btn.dataset.category === category) {
                    btn.className = 'category-btn px-4 py-2 bg-purple-600 text-white rounded-full hover:bg-purple-700 transition';
                } else {
                    btn.className = 'category-btn px-4 py-2 bg-purple-100 text-purple-700 rounded-full hover:bg-purple-200 transition';
                }
            });
            
            // Filter cards (including role filter)
            let visibleCount = 0;
            
            allCards.forEach(card => {
                const searchableText = 
                    card.dataset.name + ' ' + 
                    card.dataset.description + ' ' + 
                    card.dataset.topics;
                
                const searchTerms = searchInput.value.toLowerCase()
                    .split(' ')
                    .filter(term => term.length > 0);
                
                const matchesCategory = category === 'all' || card.dataset.category === category;
                const matchesSearch = searchTerms.length === 0 || 
                    searchTerms.every(term => searchableText.includes(term));
                
                // Check role filter
                let matchesRole = true;
                if (currentRole !== 'all' && card.dataset.roles) {
                    const cardRoles = card.dataset.roles.split(' ');
                    matchesRole = cardRoles.includes(currentRole);
                }
                
                if (matchesCategory && matchesSearch && matchesRole) {
                    card.style.display = 'block';
                    visibleCount++;
                } else {
                    card.style.display = 'none';
                }
            });
            
            // Smooth scroll to results
            document.querySelector('main').scrollIntoView({ behavior: 'smooth', block: 'start' });
        };'''
        
        # Insert the role filtering JavaScript before the closing script tag
        pattern = r'(    </script>\s*</body>)'
        replacement = f'{role_filter_js}\n\\1'
        updated_content = re.sub(pattern, replacement, html_content)
        return updated_content

    def generate_report(self, tools: List[Dict[str, Any]]) -> str:
        """Generate a summary report of the tools analysis"""
        category_counts = {}
        tech_level_counts = {}
        priority_counts = {}
        role_counts = {}
        primary_role_counts = {}
        
        for tool in tools:
            # Count categories
            cat = tool['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1
            
            # Count tech levels
            tech = tool['techLevel']
            tech_level_counts[tech] = tech_level_counts.get(tech, 0) + 1
            
            # Count priorities
            pri = tool['priority']
            priority_counts[pri] = priority_counts.get(pri, 0) + 1
            
            # Count primary roles
            primary_role = tool['primary_role']
            primary_role_counts[primary_role] = primary_role_counts.get(primary_role, 0) + 1
            
            # Count all roles (including multi-role tools)
            for role_info in tool['roles']:
                role = role_info['role']
                role_counts[role] = role_counts.get(role, 0) + 1
        
        report = f"""
=== QUIZ TOOL UPDATE REPORT ===
Updated: {len(tools)} tools

CATEGORY DISTRIBUTION:
{chr(10).join(f"  {cat.replace('_', ' ').title()}: {count} tools" for cat, count in sorted(category_counts.items()))}

ROLE DISTRIBUTION (Primary):
{chr(10).join(f"  {role.title()}: {count} tools" for role, count in sorted(primary_role_counts.items()))}

ROLE DISTRIBUTION (All Assignments):
{chr(10).join(f"  {role.title()}: {count} tools" for role, count in sorted(role_counts.items()))}

TECHNICAL LEVEL DISTRIBUTION:
{chr(10).join(f"  {level.title()}: {count} tools" for level, count in sorted(tech_level_counts.items()))}

PRIORITY DISTRIBUTION:
{chr(10).join(f"  {pri.title()}: {count} tools" for pri, count in sorted(priority_counts.items()))}

HIGH PRIORITY TOOLS:
{chr(10).join(f"  - {tool['display_name']} (Primary: {tool['primary_role']})" for tool in tools if tool['priority'] == 'high')}

FILES UPDATED:
  - {self.js_file}
  - {self.html_file} (role attributes and navigation)

The quiz recommendation engine and HTML have been updated with role-based filtering from {self.html_file}.
        """
        
        return report.strip()

    def run(self, dry_run: bool = False) -> None:
        """Main execution method"""
        print(f"Extracting tools from {self.html_file}...")
        
        # Extract tools from HTML
        raw_tools = self.extract_tools_from_html()
        print(f"Found {len(raw_tools)} tools")
        
        if not raw_tools:
            print("ERROR: No tools found in HTML file. Check the file format.")
            return
        
        # Categorize each tool
        categorized_tools = []
        for tool in raw_tools:
            categorized = self.categorize_tool(tool)
            categorized_tools.append(categorized)
        
        # Generate report
        report = self.generate_report(categorized_tools)
        print(report)
        
        if not dry_run:
            # Update JavaScript file
            print(f"\\nUpdating {self.js_file}...")
            self.update_js_file(categorized_tools)
            
            # Update HTML file with role data and remove redundant button
            print(f"\\nUpdating {self.html_file}...")
            self.update_html_file(categorized_tools)
            
            print("✅ Quiz tools and HTML updated successfully!")
        else:
            print("\\n🔍 DRY RUN - No files were modified")
            
            # Save analysis to JSON for inspection
            analysis_file = "tool_analysis_preview.json"
            with open(analysis_file, 'w') as f:
                json.dump(categorized_tools, f, indent=2)
            print(f"📊 Analysis saved to {analysis_file}")

def main():
    parser = argparse.ArgumentParser(description='Update quiz tools from index.html')
    parser.add_argument('--html-file', default='index.html', 
                       help='Path to HTML file (default: index.html)')
    parser.add_argument('--js-file', default='recommendation_engine.js',
                       help='Path to JavaScript file (default: recommendation_engine.js)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Preview changes without modifying files')
    
    args = parser.parse_args()
    
    try:
        updater = QuizToolUpdater(args.html_file, args.js_file)
        updater.run(dry_run=args.dry_run)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()