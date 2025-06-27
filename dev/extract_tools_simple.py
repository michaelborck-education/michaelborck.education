#!/usr/bin/env python3
"""
Simple tool extraction script
"""

import re
import json

def extract_tools():
    """Extract tools manually from the known structure"""
    
    # Known tools from the grep output
    tools_data = [
        {'name': 'deep-talk', 'category': 'desktop-application', 'description': 'desktop app for ai-powered transcription and analysis of audio/video files with local processing and privacy-first design'},
        {'name': 'character-craft-lite', 'category': 'desktop-application', 'description': 'create structured chatbot personalities for zero-shot prompts, rag pipelines, and conversational ai'},
        {'name': 'critique-quest', 'category': 'desktop-application', 'description': 'desktop application for generating ai-powered educational case studies with support for openai, anthropic, google gemini, and local ollama models'},
        {'name': 'curriculum-curator', 'category': 'desktop-application', 'description': 'curriculum design and management tool'},
        {'name': 'insight-lens', 'category': 'desktop-application', 'description': 'desktop survey analysis tool for university lecturers. import pdf reports, visualise trends, and get ai-powered insights'},
        {'name': 'study-buddy', 'category': 'desktop-application', 'description': 'desktop application that provides ai tutoring without requiring internet access or accounts'},
        {'name': 'swipe-verse', 'category': 'desktop-application', 'description': 'configure, play, transform - enter a universe of your making'},
        {'name': 'talk-buddy', 'category': 'desktop-application', 'description': 'your ai talking partner. practice english conversations and ace interviews with real-time voice ai'},
        {'name': 'venture-lab', 'category': 'desktop-application', 'description': 'ai-powered tools for business innovation and entrepreneurship education'},
        
        {'name': 'capstone-connect', 'category': 'web-application', 'description': 'web-based project management system that connects curtin university students with industry clients for capstone projects'},
        {'name': 'class-pulse', 'category': 'web-application', 'description': 'real-time audience interaction tool that allows presenters to create interactive polls, word clouds, and rating scales'},
        {'name': 'cloudcore', 'category': 'web-application', 'description': 'github repository for a fictional company\'s website, serving as an educational platform in security, web design, and systems analysis'},
        {'name': 'deep-brief', 'category': 'web-application', 'description': 'video analysis application that helps analyze presentations by combining speech transcription, visual analysis, and ai-powered feedback'},
        {'name': 'docslanding', 'category': 'web-application', 'description': 'jekyll theme for script-generated landing pages + auto-docs'},
        {'name': 'feed-forward', 'category': 'web-application', 'description': 'feedforward: elevate your learning. transforming feedback into a path to success'},
        {'name': 'lecturer-clone', 'category': 'web-application', 'description': 'educational tool for cloning lecturer presentation styles'},
        {'name': 'slide-stream', 'category': 'web-application', 'description': 'streaming presentation tool for education'},
        {'name': 'slinkr', 'category': 'web-application', 'description': 'lightweight url toolkit that lets you shorten, expand, qr-ify, and validate links'},
        
        {'name': 'sim-lab', 'category': 'python-package', 'description': 'set of classes for simulating various business-related scenarios for educational use'},
        {'name': 'fetch-my-weather', 'category': 'python-package', 'description': 'beginner-friendly python package for fetching weather data with built-in caching and error handling'},
        {'name': 'hands-on-ai', 'category': 'python-package', 'description': 'lightweight python framework for building personality-driven ai bots in the classroom'},
        
        {'name': 'python-jumpstart', 'category': 'learning-resource', 'description': 'learn just enough python to effectively work with ai coding assistants - beginner-friendly guide'},
        {'name': 'intentional-prompting', 'category': 'learning-resource', 'description': 'learning resource for effective ai prompting techniques'},
        {'name': 'programming-paradigms', 'category': 'learning-resource', 'description': 'educational resource on programming paradigms'},
        {'name': 'python-dev-book', 'category': 'learning-resource', 'description': 'comprehensive guide to python development practices from zero to production'},
        {'name': 'the-absolute-minimum-you-must-know', 'category': 'learning-resource', 'description': 'essential knowledge guide for beginners'},
        {'name': 'the-calculator-walkthrough', 'category': 'learning-resource', 'description': 'exercise in programming to help hone skills through practice and repetition'},
        
        {'name': 'electron-kit', 'category': 'infrastructure-tool', 'description': 'professional electron app template with modular architecture'},
        {'name': 'headless-cms-react', 'category': 'infrastructure-tool', 'description': 'minimal react project scaffold that builds on headless cms concepts for wordpress api integration'},
        {'name': 'headless-cms-vanilla', 'category': 'infrastructure-tool', 'description': 'scaffolded html/css/javascript project for headless wordpress implementation'},
        {'name': 'sec-utils', 'category': 'infrastructure-tool', 'description': 'security utilities in docker containers'},
        {'name': 'weatherwise-template', 'category': 'infrastructure-tool', 'description': 'kickstart weatherwise assignment with ready-to-use python template featuring ai prompts and weather data'},
        
        {'name': 'ask-docs', 'category': 'command-line-tool', 'description': 'general-purpose document assistant for any documentation using rag and llms'},
        {'name': 'gh-toolkit', 'category': 'command-line-tool', 'description': 'github toolkit for command line operations'},
        {'name': 'mark-mate', 'category': 'command-line-tool', 'description': 'command line tool for markdown processing'},
    ]
    
    return tools_data

def categorize_for_teaching(tools):
    """Categorize tools by teaching context and use case"""
    
    teaching_categories = {
        'content_creation': {
            'description': 'Tools for creating educational content, presentations, and materials',
            'tools': [],
            'use_cases': ['Creating course content', 'Designing presentations', 'Building case studies', 'Documentation']
        },
        'student_interaction': {
            'description': 'Tools for engaging with students and interactive learning',
            'tools': [],
            'use_cases': ['Live polling', 'Interactive sessions', 'Student engagement', 'Real-time feedback']
        },
        'assessment_feedback': {
            'description': 'Tools for assessment, grading, and providing feedback',
            'tools': [],
            'use_cases': ['Analyzing student work', 'Providing feedback', 'Survey analysis', 'Performance insights']
        },
        'language_communication': {
            'description': 'Tools for language learning and communication skills',
            'tools': [],
            'use_cases': ['Conversation practice', 'Language learning', 'Interview preparation', 'Audio transcription']
        },
        'technical_education': {
            'description': 'Tools for programming, development, and technical education',
            'tools': [],
            'use_cases': ['Learning programming', 'Coding practice', 'Technical tutorials', 'Development skills']
        },
        'project_management': {
            'description': 'Tools for managing educational projects and connecting with industry',
            'tools': [],
            'use_cases': ['Capstone projects', 'Industry connections', 'Project coordination', 'Business education']
        },
        'ai_tutoring': {
            'description': 'AI-powered tutoring and personalized learning assistance',
            'tools': [],
            'use_cases': ['Personalized tutoring', 'AI assistance', 'Custom learning paths', 'Offline learning']
        },
        'infrastructure': {
            'description': 'Technical infrastructure and development tools (mainly for educators)',
            'tools': [],
            'use_cases': ['Setting up environments', 'Template creation', 'Development scaffolding', 'Technical setup']
        }
    }
    
    # Categorize each tool
    for tool in tools:
        name = tool['name'].lower()
        desc = tool['description'].lower()
        
        # Content Creation
        if any(keyword in name or keyword in desc for keyword in 
               ['curriculum', 'docs', 'brief', 'slide', 'case studies', 'content']):
            teaching_categories['content_creation']['tools'].append(tool)
        
        # Student Interaction
        elif any(keyword in name or keyword in desc for keyword in 
                 ['pulse', 'poll', 'interaction', 'audience', 'engage', 'clone']):
            teaching_categories['student_interaction']['tools'].append(tool)
        
        # Assessment & Feedback
        elif any(keyword in name or keyword in desc for keyword in 
                 ['feedback', 'forward', 'insight', 'lens', 'analysis', 'survey']):
            teaching_categories['assessment_feedback']['tools'].append(tool)
        
        # Language & Communication
        elif any(keyword in name or keyword in desc for keyword in 
                 ['talk', 'conversation', 'english', 'voice', 'transcription', 'deep-talk']):
            teaching_categories['language_communication']['tools'].append(tool)
        
        # Technical Education
        elif any(keyword in name or keyword in desc for keyword in 
                 ['python', 'programming', 'code', 'dev', 'calculator', 'weather', 'paradigms']):
            teaching_categories['technical_education']['tools'].append(tool)
        
        # Project Management
        elif any(keyword in name or keyword in desc for keyword in 
                 ['capstone', 'connect', 'project', 'venture', 'business', 'industry']):
            teaching_categories['project_management']['tools'].append(tool)
        
        # AI Tutoring
        elif any(keyword in name or keyword in desc for keyword in 
                 ['buddy', 'tutor', 'ai', 'chatbot', 'quest', 'hands-on-ai']):
            teaching_categories['ai_tutoring']['tools'].append(tool)
        
        # Infrastructure
        elif any(keyword in name or keyword in desc for keyword in 
                 ['template', 'kit', 'scaffold', 'cms', 'utils', 'toolkit', 'infrastructure']):
            teaching_categories['infrastructure']['tools'].append(tool)
        
        # Default fallback
        else:
            teaching_categories['content_creation']['tools'].append(tool)
    
    return teaching_categories

def analyze_target_users(tools):
    """Analyze target user groups"""
    user_groups = {
        'k12_teachers': [],
        'university_educators': [],
        'students': [],
        'technical_educators': [],
        'general_educators': []
    }
    
    for tool in tools:
        name = tool['name'].lower()
        desc = tool['description'].lower()
        
        if 'university' in desc or 'lecturer' in desc:
            user_groups['university_educators'].append(tool)
        elif any(keyword in name or keyword in desc for keyword in 
                 ['python', 'programming', 'code', 'technical', 'dev']):
            user_groups['technical_educators'].append(tool)
        elif any(keyword in name or keyword in desc for keyword in 
                 ['student', 'learn', 'study', 'jumpstart', 'beginner']):
            user_groups['students'].append(tool)
        else:
            user_groups['general_educators'].append(tool)
    
    return user_groups

def main():
    tools = extract_tools()
    
    print(f"=== EXTRACTED {len(tools)} TOOLS ===")
    for tool in tools:
        print(f"- {tool['name']} ({tool['category']})")
    
    # Categorize by teaching context
    teaching_cats = categorize_for_teaching(tools)
    
    print(f"\n=== TEACHING CONTEXT CATEGORIZATION ===")
    for cat_name, cat_data in teaching_cats.items():
        print(f"\n{cat_name.upper().replace('_', ' ')} ({len(cat_data['tools'])} tools)")
        print(f"  Use cases: {', '.join(cat_data['use_cases'])}")
        for tool in cat_data['tools']:
            print(f"  - {tool['name']}")
    
    # Analyze target users
    user_groups = analyze_target_users(tools)
    
    print(f"\n=== TARGET USER ANALYSIS ===")
    for group, tool_list in user_groups.items():
        print(f"\n{group.upper().replace('_', ' ')} ({len(tool_list)} tools)")
        for tool in tool_list:
            print(f"  - {tool['name']}")
    
    # Save comprehensive analysis
    analysis = {
        'all_tools': tools,
        'teaching_categories': teaching_cats,
        'user_groups': user_groups,
        'total_count': len(tools),
        'category_distribution': {cat: len(data['tools']) for cat, data in teaching_cats.items()}
    }
    
    with open('comprehensive_tool_analysis.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print(f"\n=== SUMMARY ===")
    print(f"Total tools analyzed: {len(tools)}")
    print("Top categories:")
    sorted_cats = sorted(teaching_cats.items(), key=lambda x: len(x[1]['tools']), reverse=True)
    for cat_name, cat_data in sorted_cats[:5]:
        print(f"  - {cat_name.replace('_', ' ').title()}: {len(cat_data['tools'])} tools")
    
    print("\nAnalysis complete! Saved to comprehensive_tool_analysis.json")

if __name__ == '__main__':
    main()