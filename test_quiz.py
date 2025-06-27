#!/usr/bin/env python3
"""
Test script for the educational tools quiz recommendation system
"""

import json
import sys
from pathlib import Path

def test_recommendation_engine():
    """Test the recommendation logic with sample answers"""
    
    # Test scenarios
    test_scenarios = [
        {
            "name": "University Technical Educator",
            "answers": {
                "q1": "university",
                "q2": "technology", 
                "q3": "advanced",
                "q4": "technical",
                "q5": "project_based",
                "q6": "data_analysis",
                "q7": "significant",
                "q8": "technical_skills"
            },
            "expected_categories": ["technical_education", "project_management", "content_creation"]
        },
        {
            "name": "K-12 General Educator",
            "answers": {
                "q1": "k12",
                "q2": "general",
                "q3": "beginner", 
                "q4": "interactive",
                "q5": "realtime",
                "q6": "realtime_feedback",
                "q7": "minimal",
                "q8": "engaging"
            },
            "expected_categories": ["student_interaction", "content_creation", "ai_tutoring"]
        },
        {
            "name": "Corporate Business Trainer",
            "answers": {
                "q1": "corporate",
                "q2": "business",
                "q3": "intermediate",
                "q4": "analysis",
                "q5": "project_based", 
                "q6": "project_outcomes",
                "q7": "moderate",
                "q8": "real_world"
            },
            "expected_categories": ["project_management", "assessment_feedback", "content_creation"]
        }
    ]
    
    print("=== QUIZ RECOMMENDATION SYSTEM TEST ===")
    print(f"Testing {len(test_scenarios)} scenarios...\n")
    
    all_tests_passed = True
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"TEST {i}: {scenario['name']}")
        print(f"Answers: {scenario['answers']}")
        
        # Simulate the scoring logic
        categories = {
            'content_creation': 0,
            'technical_education': 0,
            'project_management': 0,
            'assessment_feedback': 0,
            'ai_tutoring': 0,
            'student_interaction': 0,
            'language_communication': 0,
            'utility': 0
        }
        
        # Apply scoring rules (simplified version of the JS logic)
        answers = scenario['answers']
        
        # Teaching level scoring
        if answers['q1'] == 'k12':
            categories['student_interaction'] += 3
            categories['content_creation'] += 2
            categories['ai_tutoring'] += 1
        elif answers['q1'] == 'university':
            categories['content_creation'] += 3
            categories['assessment_feedback'] += 2
            categories['project_management'] += 2
        elif answers['q1'] == 'corporate':
            categories['project_management'] += 3
            categories['technical_education'] += 2
            categories['content_creation'] += 1
        
        # Subject area scoring
        if answers['q2'] == 'technology':
            categories['technical_education'] += 3
            categories['content_creation'] += 1
        elif answers['q2'] == 'business':
            categories['project_management'] += 3
            categories['assessment_feedback'] += 1
        elif answers['q2'] == 'general':
            categories['content_creation'] += 2
            categories['student_interaction'] += 1
            categories['ai_tutoring'] += 1
        
        # Content focus scoring
        if answers['q4'] == 'interactive':
            categories['content_creation'] += 3
            categories['student_interaction'] += 2
        elif answers['q4'] == 'technical':
            categories['technical_education'] += 3
            categories['content_creation'] += 1
        elif answers['q4'] == 'analysis':
            categories['content_creation'] += 2
            categories['assessment_feedback'] += 3
        
        # Engagement style scoring
        if answers['q5'] == 'realtime':
            categories['student_interaction'] += 3
            categories['assessment_feedback'] += 1
        elif answers['q5'] == 'project_based':
            categories['project_management'] += 3
            categories['technical_education'] += 2
        
        # Educational goal scoring
        if answers['q8'] == 'technical_skills':
            categories['technical_education'] += 3
            categories['project_management'] += 1
        elif answers['q8'] == 'engaging':
            categories['content_creation'] += 3
            categories['student_interaction'] += 2
        elif answers['q8'] == 'real_world':
            categories['project_management'] += 3
            categories['technical_education'] += 1
        
        # Get top categories
        sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
        top_categories = [cat[0] for cat in sorted_categories[:3] if cat[1] > 0]
        
        print(f"Top categories: {top_categories}")
        print(f"Expected: {scenario['expected_categories']}")
        
        # Check if at least 2 of the expected categories are in top 3
        matches = sum(1 for cat in scenario['expected_categories'] if cat in top_categories)
        success = matches >= 2
        
        print(f"Result: {'✅ PASS' if success else '❌ FAIL'} ({matches}/{len(scenario['expected_categories'])} expected categories matched)")
        print()
        
        if not success:
            all_tests_passed = False
    
    print("=== TEST SUMMARY ===")
    print(f"Overall result: {'✅ ALL TESTS PASSED' if all_tests_passed else '❌ SOME TESTS FAILED'}")
    
    return all_tests_passed

def verify_file_integrity():
    """Verify that all required files exist and are properly formatted"""
    
    print("=== FILE INTEGRITY CHECK ===")
    
    required_files = [
        "index.html",
        "educational-tools-quiz.html", 
        "recommendation_engine.js",
        "update_quiz_tools.py"
    ]
    
    all_files_ok = True
    
    for filename in required_files:
        file_path = Path(filename)
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"✅ {filename} - {size:,} bytes")
        else:
            print(f"❌ {filename} - MISSING")
            all_files_ok = False
    
    # Check if quiz HTML has the expected structure
    quiz_file = Path("educational-tools-quiz.html")
    if quiz_file.exists():
        content = quiz_file.read_text()
        required_elements = [
            "ToolRecommendationEngine",
            "question-1",
            "question-8", 
            "results",
            "calculateRecommendations"
        ]
        
        missing_elements = [elem for elem in required_elements if elem not in content]
        if missing_elements:
            print(f"❌ Quiz HTML missing elements: {missing_elements}")
            all_files_ok = False
        else:
            print("✅ Quiz HTML structure validated")
    
    # Check if main index has quiz links
    index_file = Path("index.html")
    if index_file.exists():
        content = index_file.read_text()
        if "educational-tools-quiz.html" in content:
            print("✅ Index HTML has quiz integration")
        else:
            print("❌ Index HTML missing quiz links")
            all_files_ok = False
    
    print(f"\nFile integrity: {'✅ PASSED' if all_files_ok else '❌ FAILED'}")
    return all_files_ok

def main():
    """Run all tests"""
    print("Educational Tools Quiz - System Test\n")
    
    # Test recommendation logic
    rec_test_passed = test_recommendation_engine()
    print()
    
    # Test file integrity  
    file_test_passed = verify_file_integrity()
    print()
    
    # Overall result
    all_passed = rec_test_passed and file_test_passed
    print("=== OVERALL TEST RESULT ===")
    print(f"{'✅ SYSTEM READY' if all_passed else '❌ ISSUES DETECTED'}")
    
    if all_passed:
        print("\nThe educational tools quiz system is ready for use!")
        print("To deploy:")
        print("1. Open educational-tools-quiz.html in a browser to test")
        print("2. Run 'python3 update_quiz_tools.py' when you add/remove tools")
        print("3. The main index.html now includes quiz navigation links")
    else:
        print("\nPlease fix the issues above before deploying.")
    
    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())