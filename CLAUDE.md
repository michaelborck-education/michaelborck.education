# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a static educational tools portfolio website hosted on GitHub Pages. It showcases 35+ educational tools across 8 categories and includes an interactive quiz system for personalized tool recommendations.

## Project Structure

```
├── index.html                     # Main portfolio page (auto-generated)
├── educational-tools-quiz.html    # Interactive quiz interface
├── recommendation_engine.js       # Quiz recommendation algorithm
├── update_quiz_tools.py           # Tool to sync quiz with main page
├── test_quiz.py                   # Quiz system testing
├── dev/                           # Development files and analysis
├── _notes/                        # Educational content and presentations
└── QUIZ_README.md                 # Detailed quiz system documentation
```

## Common Development Commands

### Testing and Validation
```bash
# Test the quiz recommendation system
python3 test_quiz.py

# Update quiz tools from main page (dry run)
python3 update_quiz_tools.py --dry-run

# Apply quiz updates
python3 update_quiz_tools.py
```

### Content Generation
The main `index.html` is auto-generated using [gh-toolkit](https://github.com/michael-borck/gh-toolkit):
```bash
# Install the toolkit
pip install gh-toolkit

# Generate updated portfolio page
gh-toolkit generate --config your-config.json
```

## Architecture

### Quiz System Architecture
- **Frontend**: Vanilla HTML/CSS/JavaScript quiz interface
- **Recommendation Engine**: JavaScript class-based system with 8 teaching categories
- **Data Sync**: Python scripts maintain tool consistency between main page and quiz
- **Categories**: Content Creation, Technical Education, Project Management, Assessment & Feedback, AI Tutoring, Student Interaction, Language Communication, Utility Tools

### Tool Categorization System
Tools are categorized using keyword matching rules in `update_quiz_tools.py:20-50`. The system maps HTML data attributes to teaching contexts and assigns priority levels.

### Recommendation Algorithm
Located in `recommendation_engine.js:6`, uses weighted scoring across 8 quiz questions to recommend 10-12 most relevant tools from the collection.

## Key Components

### Main Portfolio (`index.html`)
- Auto-generated from repository data using gh-toolkit
- Contains structured data attributes for each tool
- Includes search, filtering, and responsive design
- **Critical**: Do not manually edit - regenerate using gh-toolkit

### Quiz Interface (`educational-tools-quiz.html`)
- Self-contained quiz with embedded CSS and JavaScript
- Links to `recommendation_engine.js` for algorithm logic
- Responsive design that works across all devices

### Recommendation Engine (`recommendation_engine.js`)
- Class-based architecture with tool definitions starting at line 12
- Scoring logic maps quiz answers to tool categories
- High-priority tools get preference in recommendations

### Update Scripts
- `update_quiz_tools.py`: Parses `index.html` and updates quiz data structures
- `test_quiz.py`: Validates recommendation logic with test scenarios
- Both scripts are essential for maintaining quiz-portfolio synchronization

## Development Workflow

1. **Adding New Tools**: Use gh-toolkit to regenerate `index.html`, then run `python3 update_quiz_tools.py`
2. **Quiz Modifications**: Edit `educational-tools-quiz.html` and `recommendation_engine.js`, then test with `python3 test_quiz.py`
3. **Testing**: Always run `python3 test_quiz.py` after changes to validate the system

## Important Notes

- This is a static site with no build process or dependencies
- All Python scripts use only standard library (no requirements.txt needed)
- The quiz system is designed to auto-update when tools are added/removed
- Main page generation requires external gh-toolkit package
- Website is deployed automatically via GitHub Pages from main branch