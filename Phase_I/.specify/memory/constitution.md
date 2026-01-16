<!-- Sync Impact Report:
Version change: 1.0.0 → 1.1.0 (Phase I specific updates)
Added sections: none
Modified principles: III. Progressive Complexity Evolution, VI. Clean Architecture & Separation of Concerns
Removed sections: none
Templates requiring updates: ⚠ pending manual review of .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: none
-->

# Todo App Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All development must follow the Spec-Driven Development methodology: Specification → Plan → Tasks → Implementation. No code may be written without a corresponding specification, plan, and task breakdown. This ensures alignment between requirements and implementation.

### II. AI-Agent Driven Implementation
All code must be generated using Claude Code or other approved AI agents following the Agentic Dev Stack workflow. Manual coding is prohibited. AI agents must follow the structured workflow defined in AGENTS.md and utilize Spec-Kit Plus for specification management.

### III. Progressive Complexity Evolution
Development follows a structured progression from simple to complex: starting with in-memory console applications in Phase I and evolving to full-stack web apps, AI chatbots, and cloud-native deployments in subsequent phases. Each phase builds upon the previous with increasing architectural sophistication. Currently focused on Phase I implementation.

### IV. Reusable Intelligence & Modularity
Components must be designed as reusable, modular units that can be leveraged across different phases and applications. Emphasis on creating reusable intelligence via Claude Code Subagents and Agent Skills to accelerate development.

### V. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced. All features must have corresponding tests before implementation completion.

### VI. Clean Architecture & Separation of Concerns
Maintain clear separation between different modules and functions within the console application. Each component should have well-defined interfaces and responsibilities to enable independent development and testing. In Phase I, focus on clean module organization and proper separation of concerns within the single console application.

## Technology Stack Standards

### Primary Technologies
- Python 3.13+ for console application development
- UV for package management
- Claude Code and Spec-Kit Plus for spec-driven development
- In-memory data storage for Phase I

### Infrastructure & Deployment
- Console-based user interface for Phase I
- Local development environment
- Spec-Driven Development workflow with Claude Code

## Development Workflow

### Specification Process
1. Write comprehensive specifications in the /specs directory following Spec-Kit Plus conventions for Phase I console application
2. Generate implementation plans that align with architectural constraints for in-memory Python console app
3. Break plans into atomic, testable tasks specific to Phase I requirements
4. Implement only what is specified in approved tasks for Phase I

### Code Review & Quality Gates
- All PRs must verify compliance with Phase I specification requirements
- Code must be generated via AI agents following AGENTS.md guidelines
- Specifications must be updated if requirements change during development
- Manual code changes require explicit exception approval
- Focus on implementing Basic Level features: Add Task, Delete Task, Update Task, View Task List, Mark as Complete

## Changelog

### Version 1.1.0 - 2026-01-16
- Updated technology stack to reflect Phase I requirements (Python console app, UV, in-memory storage)
- Modified Progressive Complexity Evolution to clarify current Phase I focus
- Updated Clean Architecture principle to reflect console application context
- Revised Development Workflow to emphasize Phase I specific requirements
- Added focus on Basic Level features: Add, Delete, Update, View, Mark Complete

### Version 1.0.0 - 2026-01-16
- Initial constitution created for Todo App Hackathon II
- Established core principles: Spec-Driven Development, AI-Agent Implementation, Progressive Complexity
- Defined initial technology stack and development workflow

## Governance

This constitution supersedes all other development practices. Amendments require documentation of the change, approval from project maintainers, and a migration plan for existing code. All development activities must comply with these principles and can be audited for compliance.

**Version**: 1.1.0 | **Ratified**: 2026-01-16 | **Last Amended**: 2026-01-16