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
        
        return {
            'name': tool['name'].replace('-', ' ').title().replace(' ', ''),
            'display_name': tool['name'].replace('-', ' ').title(),
            'category': teaching_category,
            'description': self._clean_description(tool['description']),
            'priority': priority,
            'techLevel': tech_level,
            'contexts': contexts,
            'subjects': subjects,
            'original_category': tool['original_category']
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

    def generate_report(self, tools: List[Dict[str, Any]]) -> str:
        """Generate a summary report of the tools analysis"""
        category_counts = {}
        tech_level_counts = {}
        priority_counts = {}
        
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
        
        report = f"""
=== QUIZ TOOL UPDATE REPORT ===
Updated: {len(tools)} tools

CATEGORY DISTRIBUTION:
{chr(10).join(f"  {cat.replace('_', ' ').title()}: {count} tools" for cat, count in sorted(category_counts.items()))}

TECHNICAL LEVEL DISTRIBUTION:
{chr(10).join(f"  {level.title()}: {count} tools" for level, count in sorted(tech_level_counts.items()))}

PRIORITY DISTRIBUTION:
{chr(10).join(f"  {pri.title()}: {count} tools" for pri, count in sorted(priority_counts.items()))}

HIGH PRIORITY TOOLS:
{chr(10).join(f"  - {tool['display_name']}" for tool in tools if tool['priority'] == 'high')}

FILES UPDATED:
  - {self.js_file}

The quiz recommendation engine has been updated with the latest tools from {self.html_file}.
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
            print("✅ Quiz tools updated successfully!")
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