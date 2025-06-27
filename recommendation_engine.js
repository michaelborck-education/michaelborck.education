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
            // Content Creation Tools
            'critique-quest': {
                name: 'Critique Quest',
                category: 'content_creation',
                description: 'Generate AI-powered educational case studies with multiple AI model support',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ['university', 'corporate'],
                subjects: ['general', 'business']
            },
            'curriculum-curator': {
                name: 'Curriculum Curator',
                category: 'content_creation',
                description: 'Design and manage educational curricula with structured frameworks',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ['university', 'k12'],
                subjects: ['general']
            },
            'deep-brief': {
                name: 'Deep Brief',
                category: 'content_creation',
                description: 'Analyze presentations with AI-powered feedback on speech and visuals',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ['university', 'corporate'],
                subjects: ['general', 'communication']
            },
            'slide-stream': {
                name: 'Slide Stream',
                category: 'content_creation',
                description: 'Streaming presentation tool for interactive educational content',
                priority: 'medium',
                techLevel: 'beginner',
                contexts: ['university', 'k12'],
                subjects: ['general']
            },
            'docslanding': {
                name: 'Docs Landing',
                category: 'content_creation',
                description: 'Create script-generated documentation and landing pages',
                priority: 'low',
                techLevel: 'advanced',
                contexts: ['university'],
                subjects: ['technology']
            },

            // Technical Education Tools
            'python-jumpstart': {
                name: 'Python Jumpstart',
                category: 'technical_education',
                description: 'Learn Python fundamentals for working with AI coding assistants',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ['university', 'self_directed'],
                subjects: ['technology']
            },
            'hands-on-ai': {
                name: 'Hands-on AI',
                category: 'technical_education',
                description: 'Build personality-driven AI bots for classroom use',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ['university'],
                subjects: ['technology']
            },
            'the-calculator-walkthrough': {
                name: 'Calculator Walkthrough',
                category: 'technical_education',
                description: 'Programming practice through calculator implementation',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ['university', 'self_directed'],
                subjects: ['technology']
            },
            'python-dev-book': {
                name: 'Python Dev Book',
                category: 'technical_education',
                description: 'Comprehensive guide from zero to production Python development',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ['university', 'self_directed'],
                subjects: ['technology']
            },
            'programming-paradigms': {
                name: 'Programming Paradigms',
                category: 'technical_education',
                description: 'Educational resource covering different programming approaches',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ['university'],
                subjects: ['technology']
            },

            // Assessment & Feedback Tools
            'insight-lens': {
                name: 'Insight Lens',
                category: 'assessment_feedback',
                description: 'Analyze survey data and visualize trends with AI insights',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ['university'],
                subjects: ['general']
            },
            'feed-forward': {
                name: 'Feed Forward',
                category: 'assessment_feedback',
                description: 'Transform feedback into actionable learning paths',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ['university', 'k12'],
                subjects: ['general']
            },
            'deep-talk': {
                name: 'Deep Talk',
                category: 'assessment_feedback',
                description: 'AI-powered transcription and analysis of audio/video content',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ['university', 'corporate'],
                subjects: ['general', 'communication']
            },

            // Project Management Tools
            'capstone-connect': {
                name: 'Capstone Connect',
                category: 'project_management',
                description: 'Connect students with industry clients for real-world projects',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ['university'],
                subjects: ['business', 'technology']
            },
            'venture-lab': {
                name: 'Venture Lab',
                category: 'project_management',
                description: 'AI-powered tools for business innovation and entrepreneurship',
                priority: 'high',
                techLevel: 'intermediate',
                contexts: ['university', 'corporate'],
                subjects: ['business']
            },
            'sim-lab': {
                name: 'Sim Lab',
                category: 'project_management',
                description: 'Simulate business scenarios for educational decision-making',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ['university', 'corporate'],
                subjects: ['business']
            },

            // AI Tutoring Tools
            'study-buddy': {
                name: 'Study Buddy',
                category: 'ai_tutoring',
                description: 'Offline AI tutoring without internet or account requirements',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ['university', 'k12', 'self_directed'],
                subjects: ['general']
            },
            'talk-buddy': {
                name: 'Talk Buddy',
                category: 'ai_tutoring',
                description: 'Practice conversations and interview skills with AI',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ['university', 'corporate', 'self_directed'],
                subjects: ['communication']
            },
            'character-craft-lite': {
                name: 'Character Craft Lite',
                category: 'ai_tutoring',
                description: 'Create structured chatbot personalities for educational use',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ['university'],
                subjects: ['technology']
            },

            // Student Interaction Tools
            'class-pulse': {
                name: 'Class Pulse',
                category: 'student_interaction',
                description: 'Real-time polls, word clouds, and interactive audience engagement',
                priority: 'high',
                techLevel: 'beginner',
                contexts: ['university', 'k12', 'corporate'],
                subjects: ['general']
            },
            'lecturer-clone': {
                name: 'Lecturer Clone',
                category: 'student_interaction',
                description: 'Clone and adapt lecturer presentation styles',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ['university'],
                subjects: ['general']
            },

            // Utility Tools (High-value additions)
            'ask-docs': {
                name: 'Ask Docs',
                category: 'utility',
                description: 'AI-powered document assistant for any documentation',
                priority: 'medium',
                techLevel: 'intermediate',
                contexts: ['university', 'corporate'],
                subjects: ['general', 'technology']
            },
            'slinkr': {
                name: 'Slinkr',
                category: 'utility',
                description: 'URL toolkit for shortening, expanding, and QR code generation',
                priority: 'low',
                techLevel: 'beginner',
                contexts: ['general'],
                subjects: ['general']
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