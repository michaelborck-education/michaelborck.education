#!/usr/bin/env python3
"""
Tool Analysis Script for Educational Tools Quiz
Analyzes all tools from index.html and categorizes them by teaching context
"""

import re
import json
from pathlib import Path

def extract_tools_from_html(html_file):
    """Extract all tool information from index.html"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all repo-card blocks
    card_pattern = r'<div class="bg-white rounded-lg shadow-md p-6.*?repo-card"[^>]*?(data-category="[^"]*")[^>]*?(data-name="[^"]*")[^>]*?(data-description="[^"]*")[^>]*?(data-topics="[^"]*")?[^>]*?>'
    
    tools = []
    
    # Extract individual data attributes
    category_matches = re.findall(r'data-category="([^"]*)"', content)
    name_matches = re.findall(r'data-name="([^"]*)"', content)
    desc_matches = re.findall(r'data-description="([^"]*)"', content)
    topic_matches = re.findall(r'data-topics="([^"]*)"', content)
    
    # Filter out category navigation elements
    filtered_categories = [cat for cat in category_matches if cat not in ['all', 'desktop-application', 'web-application', 'python-package', 'learning-resource', 'infrastructure-tool', 'command-line-tool']]
    
    # Match up the data (assuming they appear in the same order)
    min_length = min(len(name_matches), len(filtered_categories), len(desc_matches))
    
    for i in range(min_length):
        tool = {
            'name': name_matches[i],
            'category': filtered_categories[i] if i < len(filtered_categories) else 'unknown',
            'description': desc_matches[i] if i < len(desc_matches) else '',
            'topics': topic_matches[i] if i < len(topic_matches) else ''
        }
        tools.append(tool)
    
    return tools

def categorize_for_teaching(tools):
    """Categorize tools by teaching context and use case"""
    
    # Define teaching context categories
    teaching_categories = {
        'content_creation': {
            'description': 'Tools for creating educational content, presentations, and materials',
            'tools': []
        },
        'student_interaction': {
            'description': 'Tools for engaging with students and interactive learning',
            'tools': []
        },
        'assessment_feedback': {
            'description': 'Tools for assessment, grading, and providing feedback',
            'tools': []
        },
        'language_communication': {
            'description': 'Tools for language learning and communication skills',
            'tools': []
        },
        'data_analysis': {
            'description': 'Tools for analyzing student data and educational insights',
            'tools': []
        },
        'technical_development': {
            'description': 'Tools for programming, development, and technical education',
            'tools': []
        },
        'project_management': {
            'description': 'Tools for managing educational projects and resources',
            'tools': []
        },
        'infrastructure_setup': {
            'description': 'Technical infrastructure and setup tools (mainly for educators)',
            'tools': []
        }
    }
    
    # Categorize each tool based on name and description
    for tool in tools:
        name_lower = tool['name'].lower()
        desc_lower = tool['description'].lower()
        
        # Content Creation Tools
        if any(keyword in name_lower or keyword in desc_lower for keyword in 
               ['curriculum', 'content', 'presentation', 'case studies', 'brief', 'slide', 'docs']):
            teaching_categories['content_creation']['tools'].append(tool)
        
        # Student Interaction Tools
        elif any(keyword in name_lower or keyword in desc_lower for keyword in 
                 ['interaction', 'poll', 'audience', 'pulse', 'engage', 'clone', 'buddy']):
            teaching_categories['student_interaction']['tools'].append(tool)
        
        # Assessment & Feedback Tools
        elif any(keyword in name_lower or keyword in desc_lower for keyword in 
                 ['feedback', 'forward', 'insight', 'analysis', 'survey', 'quest']):
            teaching_categories['assessment_feedback']['tools'].append(tool)
        
        # Language & Communication Tools
        elif any(keyword in name_lower or keyword in desc_lower for keyword in 
                 ['talk', 'conversation', 'english', 'communication', 'voice', 'transcription']):
            teaching_categories['language_communication']['tools'].append(tool)
        
        # Data Analysis Tools
        elif any(keyword in name_lower or keyword in desc_lower for keyword in 
                 ['data', 'analysis', 'insights', 'trends', 'visualise', 'lens']):
            teaching_categories['data_analysis']['tools'].append(tool)
        
        # Technical Development Tools
        elif any(keyword in name_lower or keyword in desc_lower for keyword in 
                 ['python', 'programming', 'code', 'dev', 'sim-lab', 'calculator', 'weather']):
            teaching_categories['technical_development']['tools'].append(tool)
        
        # Project Management Tools
        elif any(keyword in name_lower or keyword in desc_lower for keyword in 
                 ['project', 'management', 'capstone', 'connect', 'venture', 'lab']):
            teaching_categories['project_management']['tools'].append(tool)
        
        # Infrastructure Tools (mainly for educators/developers)
        elif any(keyword in name_lower or keyword in desc_lower for keyword in 
                 ['template', 'scaffold', 'kit', 'cms', 'infrastructure', 'docker', 'toolkit', 'utils']):
            teaching_categories['infrastructure_setup']['tools'].append(tool)
        
        # Default category if no match
        else:
            # Try to guess based on category
            if tool['category'] == 'learning-resource':
                teaching_categories['technical_development']['tools'].append(tool)
            elif tool['category'] == 'infrastructure-tool':
                teaching_categories['infrastructure_setup']['tools'].append(tool)
            else:
                teaching_categories['content_creation']['tools'].append(tool)
    
    return teaching_categories

def analyze_tool_complexity(tools):
    """Analyze technical complexity of tools"""
    complexity_levels = {
        'beginner': [],
        'intermediate': [],
        'advanced': []
    }
    
    for tool in tools:
        name_lower = tool['name'].lower()
        desc_lower = tool['description'].lower()
        
        # Beginner-friendly indicators
        if any(keyword in name_lower or keyword in desc_lower for keyword in 
               ['beginner', 'jumpstart', 'learn', 'tutorial', 'guide', 'minimum', 'buddy']):
            complexity_levels['beginner'].append(tool)
        
        # Advanced technical indicators
        elif any(keyword in name_lower or keyword in desc_lower for keyword in 
                 ['docker', 'api', 'framework', 'infrastructure', 'electron', 'cms', 'ollama']):
            complexity_levels['advanced'].append(tool)
        
        # Everything else is intermediate
        else:
            complexity_levels['intermediate'].append(tool)
    
    return complexity_levels

def main():
    # Extract tools from HTML
    html_file = 'index.html'
    tools = extract_tools_from_html(html_file)
    
    print(f"Found {len(tools)} tools")
    print("\n=== ALL TOOLS ===")
    for tool in tools:
        print(f"- {tool['name']} ({tool['category']}): {tool['description'][:80]}...")
    
    # Categorize by teaching context
    teaching_cats = categorize_for_teaching(tools)
    
    print("\n=== TEACHING CONTEXT CATEGORIZATION ===")
    for cat_name, cat_data in teaching_cats.items():
        print(f"\n{cat_name.upper()} ({len(cat_data['tools'])} tools)")
        print(f"  Description: {cat_data['description']}")
        for tool in cat_data['tools']:
            print(f"  - {tool['name']}")
    
    # Analyze complexity
    complexity = analyze_tool_complexity(tools)
    
    print("\n=== COMPLEXITY ANALYSIS ===")
    for level, tool_list in complexity.items():
        print(f"\n{level.upper()} ({len(tool_list)} tools)")
        for tool in tool_list:
            print(f"  - {tool['name']}")
    
    # Save analysis to JSON
    analysis = {
        'all_tools': tools,
        'teaching_categories': teaching_cats,
        'complexity_levels': complexity,
        'total_count': len(tools)
    }
    
    with open('tool_analysis.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print(f"\nAnalysis saved to tool_analysis.json")

if __name__ == '__main__':
    main()