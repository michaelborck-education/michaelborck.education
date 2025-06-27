/**
 * Educational Tools Recommendation Engine
 * Maps quiz responses to personalized tool recommendations
 */

class ToolRecommendationEngine {
    constructor() {
        this.tools = this.initializeTools();
        this.categories = this.initializeCategories();
    }

    initializeTools() {
        return {
            'deeptalk': {
                name: 'Deep Talk',
                category: 'language_communication',
                description: 'Desktop app for ai-powered transcription and analysis of audio/video files with local processing and privacy-first design.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'charactercraftlite': {
                name: 'Character Craft Lite',
                category: 'language_communication',
                description: 'Create structured chatbot personalities for zero-shot prompts, rag pipelines, and conversational ai.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["self_directed"],
                subjects: ["communication"]
            },
            'critiquequest': {
                name: 'Critique Quest',
                category: 'content_creation',
                description: 'Desktop application for generating ai-powered educational case studies with support for   openai, anthropic, google gemini, and local ollama models.',
                priority: 'high',
                techLevel: 'advanced',
                contexts: ["general"],
                subjects: ["general"]
            },
            'curriculumcurator': {
                name: 'Curriculum Curator',
                category: 'content_creation',
                description: '',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'insightlens': {
                name: 'Insight Lens',
                category: 'assessment_feedback',
                description: 'Desktop survey analysis tool for university lecturers. import pdf reports, visualise trends, and get ai-powered insights. built with electron for windows, macos, and linux.',
                priority: 'high',
                techLevel: 'advanced',
                contexts: ["university"],
                subjects: ["general"]
            },
            'studybuddy': {
                name: 'Study Buddy',
                category: 'ai_tutoring',
                description: 'Study buddy is a desktop application that provides ai tutoring without requiring internet access or accounts.',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ["general"],
                subjects: ["general"]
            },
            'swipeverse': {
                name: 'Swipe Verse',
                category: 'content_creation',
                description: 'Configure, play, transform - enter a universe of your making.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'talkbuddy': {
                name: 'Talk Buddy',
                category: 'language_communication',
                description: 'Your ai talking partner. practice english conversations and ace interviews with real-time voice ai.',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ["general"],
                subjects: ["communication"]
            },
            'venturelab': {
                name: 'Venture Lab',
                category: 'project_management',
                description: 'Ai-powered tools for business innovation and entrepreneurship education.',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ["corporate"],
                subjects: ["business"]
            },
            'capstoneconnect': {
                name: 'Capstone Connect',
                category: 'project_management',
                description: 'A web-based project management system that connects curtin university students with industry clients for capstone projects, featuring project browsing, interest tracking, and administrative oversight.',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ["university"],
                subjects: ["business"]
            },
            'classpulse': {
                name: 'Class Pulse',
                category: 'student_interaction',
                description: 'A real-time audience interaction tool that allows presenters to create interactive polls, word clouds, and rating scales for audience engagement with instant visualised results.',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'cloudcore': {
                name: 'Cloudcore',
                category: 'assessment_feedback',
                description: 'A github repository for a fictional company's website, serving as an educational platform in security, web design, and systems analysis and design.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'deepbrief': {
                name: 'Deep Brief',
                category: 'assessment_feedback',
                description: 'A video analysis application that helps students, educators, and professionals analyze presentations by combining speech transcription, visual analysis, and ai-powered feedback. the app processes videos to provide actionable insights on speaking performance, visual effectiveness, and overall presentation quality.',
                priority: 'high',
                techLevel: 'advanced',
                contexts: ["k12"],
                subjects: ["communication"]
            },
            'docslanding': {
                name: 'Docslanding',
                category: 'content_creation',
                description: 'Jekyll theme for script-generated landing pages + auto-docs.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'feedforward': {
                name: 'Feed Forward',
                category: 'assessment_feedback',
                description: 'Feedforward: elevate your learning. transforming feedback into a path to success.',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ["general"],
                subjects: ["general"]
            },
            'lecturerclone': {
                name: 'Lecturer Clone',
                category: 'student_interaction',
                description: '',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["university"],
                subjects: ["general"]
            },
            'slinkr': {
                name: 'Slinkr',
                category: 'utility',
                description: 'A lightweight url toolkit that lets you shorten, expand, qr-ify, and validate links—all in one spot.',
                priority: 'low',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'simlab': {
                name: 'Sim Lab',
                category: 'assessment_feedback',
                description: 'A set of classes for simulating various business-related scenarios. it is designed for educational use, allowing students to experiment with modeling, analysis, and decision-making in different contexts.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["k12"],
                subjects: ["business"]
            },
            'fetchmyweather': {
                name: 'Fetch My Weather',
                category: 'technical_education',
                description: 'A beginner-friendly python package for fetching weather data from wttr.in with built-in caching and error handling.',
                priority: 'medium',
                techLevel: 'beginner',
                contexts: ["general"],
                subjects: ["technology"]
            },
            'handsonai': {
                name: 'Hands On Ai',
                category: 'technical_education',
                description: 'A lightweight python framework for building personality-driven ai bots in the classroom.',
                priority: 'high',
                techLevel: 'advanced',
                contexts: ["k12"],
                subjects: ["technology"]
            },
            'pythonjumpstart': {
                name: 'Python Jumpstart',
                category: 'ai_tutoring',
                description: 'Learn just enough python to effectively work with ai coding assistants - a   beginner-friendly guide to coding fundamentals in the ai era.',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ["general"],
                subjects: ["technology"]
            },
            'intentionalprompting': {
                name: 'Intentional Prompting',
                category: 'content_creation',
                description: '',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'programmingparadigms': {
                name: 'Programming Paradigms',
                category: 'technical_education',
                description: '',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["technology"]
            },
            'pythondevbook': {
                name: 'Python Dev Book',
                category: 'technical_education',
                description: 'A comprehensive guide to python development practices from zero to production.',
                priority: 'medium',
                techLevel: 'beginner',
                contexts: ["general"],
                subjects: ["technology"]
            },
            'theabsoluteminimumyoumustknow': {
                name: 'The Absolute Minimum You Must Know',
                category: 'content_creation',
                description: '',
                priority: 'medium',
                techLevel: 'beginner',
                contexts: ["general"],
                subjects: ["general"]
            },
            'thecalculatorwalkthrough': {
                name: 'The Calculator Walkthrough',
                category: 'technical_education',
                description: 'An exercise in programming to help hone your skills through practice and repetition.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["technology"]
            },
            'electronkit': {
                name: 'Electron Kit',
                category: 'content_creation',
                description: 'Professional electron app template with modular architecture.',
                priority: 'medium',
                techLevel: 'advanced',
                contexts: ["corporate"],
                subjects: ["general"]
            },
            'headlesscmsreact': {
                name: 'Headless Cms React',
                category: 'project_management',
                description: 'A minimal react project scaffold that builds on headless cms concepts, enabling students to implement wordpress api integration using react hooks.',
                priority: 'medium',
                techLevel: 'advanced',
                contexts: ["k12"],
                subjects: ["general"]
            },
            'headlesscmsvanilla': {
                name: 'Headless Cms Vanilla',
                category: 'project_management',
                description: 'A scaffolded html/css/javascript project based on the headless wordpress proof of concept, providing structure for students to implement a retail product display.',
                priority: 'medium',
                techLevel: 'advanced',
                contexts: ["k12"],
                subjects: ["general"]
            },
            'secutils': {
                name: 'Sec Utils',
                category: 'ai_tutoring',
                description: 'Provide security utilities in docker containers.',
                priority: 'medium',
                techLevel: 'advanced',
                contexts: ["general"],
                subjects: ["general"]
            },
            'weatherwisetemplate': {
                name: 'Weatherwise Template',
                category: 'technical_education',
                description: '🌦️ kickstart your weatherwise assignment with this ready-to-use python template featuring ai prompts, weather data, and cool visualisations! 🧠📊.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["technology"]
            },
            'askdocs': {
                name: 'Ask Docs',
                category: 'ai_tutoring',
                description: 'A general-purpose document assistant for any documentation using rag and llms like openai, claude, gemini, groq, and ollama.',
                priority: 'medium',
                techLevel: 'advanced',
                contexts: ["general"],
                subjects: ["general"]
            },
            'ghtoolkit': {
                name: 'Gh Toolkit',
                category: 'utility',
                description: 'Github repository portfolio management and presentation toolkit with llm-powered categorization and beautiful site generation.',
                priority: 'low',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["business"]
            },
            'markmate': {
                name: 'Mark Mate',
                category: 'ai_tutoring',
                description: 'Your ai teaching assistant for assignments and assessment.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            },
            'slidestream': {
                name: 'Slide Stream',
                category: 'content_creation',
                description: 'Instantly turn your text, slides, or markdown notes into engaging videos with the power of ai.',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ["general"],
                subjects: ["general"]
            }
        };
    }

    initializeCategories() {
        return {
            content_creation: { weight: 0, label: 'Content Creation' },
            technical_education: { weight: 0, label: 'Technical Education' },
            project_management: { weight: 0, label: 'Project Management' },
            assessment_feedback: { weight: 0, label: 'Assessment & Feedback' },
            ai_tutoring: { weight: 0, label: 'AI Tutoring' },
            student_interaction: { weight: 0, label: 'Student Interaction' },
            utility: { weight: 0, label: 'Utility Tools' }
        };
    }

    calculateRecommendations(answers) {
        // Reset category weights
        Object.keys(this.categories).forEach(cat => {
            this.categories[cat].weight = 0;
        });

        // Process each answer
        this.processTeachingLevel(answers.q1);
        this.processSubjectArea(answers.q2);
        this.processTechnicalLevel(answers.q3);
        this.processContentFocus(answers.q4);
        this.processEngagementStyle(answers.q5);
        this.processAssessmentApproach(answers.q6);
        this.processTimeInvestment(answers.q7);
        this.processEducationalGoal(answers.q8);

        // Generate recommendations
        return this.generateToolRecommendations(answers);
    }

    processTeachingLevel(answer) {
        const weights = {
            'k12': {
                student_interaction: 3,
                content_creation: 2,
                ai_tutoring: 1
            },
            'university': {
                content_creation: 3,
                assessment_feedback: 2,
                project_management: 2
            },
            'corporate': {
                project_management: 3,
                technical_education: 2,
                content_creation: 1
            },
            'self_directed': {
                ai_tutoring: 3,
                technical_education: 2,
                content_creation: 1
            }
        };

        if (weights[answer]) {
            Object.entries(weights[answer]).forEach(([category, weight]) => {
                this.categories[category].weight += weight;
            });
        }
    }

    processSubjectArea(answer) {
        const weights = {
            'technology': {
                technical_education: 3,
                content_creation: 1
            },
            'business': {
                project_management: 3,
                assessment_feedback: 1
            },
            'communication': {
                ai_tutoring: 2,
                student_interaction: 2,
                assessment_feedback: 1
            },
            'general': {
                content_creation: 2,
                student_interaction: 1,
                ai_tutoring: 1
            }
        };

        if (weights[answer]) {
            Object.entries(weights[answer]).forEach(([category, weight]) => {
                this.categories[category].weight += weight;
            });
        }
    }

    processTechnicalLevel(answer) {
        const weights = {
            'beginner': {
                ai_tutoring: 2,
                student_interaction: 2,
                content_creation: 1
            },
            'intermediate': {
                content_creation: 2,
                assessment_feedback: 2,
                technical_education: 1
            },
            'advanced': {
                technical_education: 3,
                project_management: 1
            },
            'expert': {
                technical_education: 3,
                project_management: 2
            }
        };

        if (weights[answer]) {
            Object.entries(weights[answer]).forEach(([category, weight]) => {
                this.categories[category].weight += weight;
            });
        }
    }

    processContentFocus(answer) {
        const weights = {
            'interactive': {
                content_creation: 3,
                student_interaction: 2
            },
            'analysis': {
                content_creation: 2,
                assessment_feedback: 3
            },
            'technical': {
                technical_education: 3,
                content_creation: 1
            },
            'ai_powered': {
                ai_tutoring: 3,
                content_creation: 2
            }
        };

        if (weights[answer]) {
            Object.entries(weights[answer]).forEach(([category, weight]) => {
                this.categories[category].weight += weight;
            });
        }
    }

    processEngagementStyle(answer) {
        const weights = {
            'realtime': {
                student_interaction: 3,
                assessment_feedback: 1
            },
            'project_based': {
                project_management: 3,
                technical_education: 2
            },
            'tutoring': {
                ai_tutoring: 3,
                assessment_feedback: 1
            },
            'self_paced': {
                content_creation: 2,
                technical_education: 2
            }
        };

        if (weights[answer]) {
            Object.entries(weights[answer]).forEach(([category, weight]) => {
                this.categories[category].weight += weight;
            });
        }
    }

    processAssessmentApproach(answer) {
        const weights = {
            'data_analysis': {
                assessment_feedback: 3,
                technical_education: 1
            },
            'ai_insights': {
                ai_tutoring: 2,
                assessment_feedback: 3
            },
            'realtime_feedback': {
                student_interaction: 2,
                ai_tutoring: 1
            },
            'project_outcomes': {
                project_management: 3,
                technical_education: 1
            }
        };

        if (weights[answer]) {
            Object.entries(weights[answer]).forEach(([category, weight]) => {
                this.categories[category].weight += weight;
            });
        }
    }

    processTimeInvestment(answer) {
        const weights = {
            'minimal': {
                ai_tutoring: 2,
                student_interaction: 2,
                utility: 1
            },
            'moderate': {
                content_creation: 2,
                assessment_feedback: 1
            },
            'significant': {
                technical_education: 2,
                project_management: 1
            },
            'ongoing': {
                technical_education: 1,
                content_creation: 1,
                project_management: 1
            }
        };

        if (weights[answer]) {
            Object.entries(weights[answer]).forEach(([category, weight]) => {
                this.categories[category].weight += weight;
            });
        }
    }

    processEducationalGoal(answer) {
        const weights = {
            'engaging': {
                content_creation: 3,
                student_interaction: 2
            },
            'technical_skills': {
                technical_education: 3,
                project_management: 1
            },
            'real_world': {
                project_management: 3,
                technical_education: 1
            },
            'personalized': {
                ai_tutoring: 3,
                assessment_feedback: 2
            }
        };

        if (weights[answer]) {
            Object.entries(weights[answer]).forEach(([category, weight]) => {
                this.categories[category].weight += weight;
            });
        }
    }

    generateToolRecommendations(answers) {
        // Sort categories by weight
        const sortedCategories = Object.entries(this.categories)
            .sort((a, b) => b[1].weight - a[1].weight)
            .map(([name, data]) => ({ name, ...data }));

        // Get user context for filtering
        const userContext = {
            teachingLevel: answers.q1,
            subjectArea: answers.q2,
            techLevel: answers.q3,
            timeInvestment: answers.q7
        };

        // Select tools based on category priorities
        const recommendations = [];
        const maxRecommendations = 12;

        // Get top tools from highest weighted categories
        for (const category of sortedCategories) {
            if (recommendations.length >= maxRecommendations) break;

            const categoryTools = Object.entries(this.tools)
                .filter(([_, tool]) => tool.category === category.name)
                .filter(([_, tool]) => this.isToolSuitable(tool, userContext))
                .sort((a, b) => this.getToolScore(b[1], userContext) - this.getToolScore(a[1], userContext))
                .map(([name, tool]) => ({ id: name, ...tool }));

            // Add 2-3 tools from each high-weight category
            const toolsToAdd = category.weight > 5 ? 3 : category.weight > 2 ? 2 : 1;
            recommendations.push(...categoryTools.slice(0, toolsToAdd));
        }

        // Ensure we have enough recommendations
        if (recommendations.length < 10) {
            const remainingTools = Object.entries(this.tools)
                .filter(([name, _]) => !recommendations.find(r => r.id === name))
                .filter(([_, tool]) => this.isToolSuitable(tool, userContext))
                .sort((a, b) => this.getToolScore(b[1], userContext) - this.getToolScore(a[1], userContext))
                .map(([name, tool]) => ({ id: name, ...tool }));

            recommendations.push(...remainingTools.slice(0, 12 - recommendations.length));
        }

        return {
            recommendations: recommendations.slice(0, 12),
            topCategories: sortedCategories.slice(0, 3),
            userProfile: this.generateUserProfile(sortedCategories, userContext)
        };
    }

    isToolSuitable(tool, userContext) {
        // Filter by teaching context
        if (tool.contexts && !tool.contexts.includes(userContext.teachingLevel) && !tool.contexts.includes('general')) {
            return false;
        }

        // Filter by technical level
        if (userContext.techLevel === 'beginner' && tool.techLevel === 'advanced') {
            return false;
        }

        return true;
    }

    getToolScore(tool, userContext) {
        let score = 0;

        // Priority bonus
        if (tool.priority === 'high') score += 3;
        else if (tool.priority === 'medium') score += 2;
        else if (tool.priority === 'low') score += 1;

        // Context match bonus
        if (tool.contexts && tool.contexts.includes(userContext.teachingLevel)) score += 2;

        // Subject match bonus
        if (tool.subjects && tool.subjects.includes(userContext.subjectArea)) score += 2;

        // Technical level match bonus
        if (tool.techLevel === userContext.techLevel) score += 1;

        return score;
    }

    generateUserProfile(sortedCategories, userContext) {
        const topCategory = sortedCategories[0];
        const profiles = {
            'content_creation': {
                title: 'The Content Creator',
                description: 'You excel at creating engaging educational materials and presentations. Your focus is on building comprehensive learning experiences that captivate and educate.'
            },
            'technical_education': {
                title: 'The Technical Educator',
                description: 'You specialize in teaching technical skills and programming concepts. Your approach combines hands-on learning with systematic skill development.'
            },
            'project_management': {
                title: 'The Project Connector',
                description: 'You believe in learning through real-world application. Your strength lies in connecting students with practical, industry-relevant experiences.'
            },
            'assessment_feedback': {
                title: 'The Insight Analyst',
                description: 'You value data-driven insights and meaningful feedback. Your teaching approach focuses on understanding student progress through analysis.'
            },
            'ai_tutoring': {
                title: 'The AI Learning Guide',
                description: 'You embrace AI-powered personalization in education. Your approach leverages technology to provide individualized learning support.'
            },
            'student_interaction': {
                title: 'The Engagement Specialist',
                description: 'You thrive on real-time interaction and student engagement. Your teaching style emphasizes active participation and immediate feedback.'
            }
        };

        return profiles[topCategory.name] || profiles['content_creation'];
    }
}

// Export for use in HTML
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ToolRecommendationEngine;
} else {
    window.ToolRecommendationEngine = ToolRecommendationEngine;
}