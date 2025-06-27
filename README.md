# Educational Tools Collection

A comprehensive portal showcasing a diverse collection of educational tools, desktop applications, web platforms, and infrastructure resources designed for teaching, learning, and educational content creation.

## 🎯 Interactive Tool Discovery

**New!** Take our [Interactive Quiz](https://michael-borck.github.io/borck.education/educational-tools-quiz.html) to discover which tools best match your teaching style and needs. Answer 8 personalized questions to get curated recommendations from our collection of 35+ educational tools.

## About

This portal serves as a centralized hub for educational technology tools that span multiple categories:

### 🖥️ Desktop Applications
- **Deep Talk** - AI-powered transcription and analysis with local processing and privacy-first design
- **Case Crafter** - Intelligent case study generator for business scenarios
- **Character Craft Lite** - Create structured chatbot personalities for conversational AI
- **Critique Quest** - AI-powered educational case study generator with multi-model support
- **Insight Lens** - Survey analysis tool for university lecturers with PDF processing and AI insights
- **Study Buddy** - Offline AI tutoring without internet or accounts
- **Talk Buddy** - AI conversation practice for English learning and interview prep
- **Venture Lab** - AI-powered business innovation and entrepreneurship education tools

### 🌐 Web Applications
- **Capstone Connect** - Project management system connecting students with industry partners
- **Class Pulse** - Real-time audience interaction with polls, word clouds, and QR codes
- **CloudCore** - Educational platform for security, web design, and systems analysis
- **Feed Forward** - AI-powered formative feedback platform for student assignments
- **Slinkr** - URL toolkit for shortening, expanding, QR generation, and validation

### 🐍 Python Packages
- **Ask Docs** - Document assistant using RAG and multiple LLMs
- **Fetch My Weather** - Beginner-friendly weather data package with caching
- **Hands-On AI** - Framework for building personality-driven AI bots in classrooms
- **Sim Lab** - Comprehensive simulation toolkit for modeling complex systems

### 📚 Learning Resources
- **Intentional Prompting** - Guide to effective programming with AI assistants
- **Python Jumpstart** - Essential Python for the AI era
- **Python Dev Book** - Comprehensive Python development practices guide
- **Programming Paradigms** - Examples of different programming approaches

### 🛠️ Command Line Tools
- **GH Toolkit** - GitHub repository portfolio management with LLM categorization
- **Mark Mate** - AI teaching assistant for assignments and assessment
- **Slide Stream** - Convert text, slides, or Markdown into engaging videos

### ⚙️ Infrastructure Tools
- **Electron Kit** - Professional Electron app template with modular architecture
- **Sec Utils** - Security utilities in Docker containers
- **WeatherWise Template** - Python template for weather data projects

## Features

- **🎯 Interactive Quiz** - Personalized tool recommendations based on teaching style and preferences
- **🔍 Search & Filter** - Find tools by name, description, or topic with real-time filtering
- **📂 Category Navigation** - Browse by application type (Desktop, Web, Python Package, etc.)
- **📊 Rich Metadata** - Each tool includes descriptions, GitHub links, documentation, and download options
- **📱 Responsive Design** - Mobile-friendly interface with modern styling
- **✨ Interactive Cards** - Hover effects and detailed information for each tool
- **🤖 Smart Categorization** - AI-powered tool classification across 8 teaching contexts

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS
- **Icons**: Font Awesome
- **Hosting**: GitHub Pages
- **Quiz System**: Custom recommendation engine with 8-category tool mapping
- **Content Generation**: [gh-toolkit](https://github.com/michael-borck/gh-toolkit) - Automated portfolio page generation
- **Data**: Dynamic JSON-based tool catalog

## Project Stats

- **35+ Educational Tools** across 8 teaching contexts
- **Multiple Programming Languages**: Python, TypeScript, JavaScript, Rust, and more
- **Cross-Platform Support**: Desktop apps for Windows, macOS, and Linux
- **Open Source**: MIT licensed projects with full source code availability
- **Smart Recommendations**: Personalized tool suggestions based on teaching preferences

## Getting Started

1. **Take the Quiz**: Visit [borck.education](https://michael-borck.github.io/borck.education/) and click "Find My Perfect Toolkit" for personalized recommendations
2. **Browse All Tools**: Explore the complete collection using search and category filters
3. **Explore Individual Tools**: Click through to GitHub repositories, documentation, and downloads

### For Developers & Maintainers

The main index.html page is automatically generated using the [gh-toolkit](https://github.com/michael-borck/gh-toolkit) package:

```bash
# Install the toolkit
pip install gh-toolkit

# Generate updated portfolio page
gh-toolkit generate --config your-config.json
```

This allows for automated updates to the tool collection as repositories are added or modified.

## Quiz System

The interactive tool recommendation system includes:

- **8 personalized questions** covering teaching context, technical comfort, and educational goals
- **Smart categorization** across Content Creation, Technical Education, Project Management, Assessment & Feedback, AI Tutoring, Student Interaction, Language Communication, and Utility Tools
- **Auto-update functionality** that syncs recommendations when new tools are added
- **Responsive design** that works seamlessly across all devices

For detailed information about the quiz system, see [QUIZ_README.md](QUIZ_README.md).

## Contributing

This is an educational showcase portal. Individual tools are maintained in their respective repositories. See each tool's GitHub page for contribution guidelines.

To update the main tool collection:
1. Use [gh-toolkit](https://github.com/michael-borck/gh-toolkit) to regenerate index.html
2. Run `python3 update_quiz_tools.py` to sync the quiz recommendations
3. Test with `python3 test_quiz.py` to ensure everything works correctly

## License

This portal is MIT licensed. Individual tools may have their own licenses - check each repository for details.