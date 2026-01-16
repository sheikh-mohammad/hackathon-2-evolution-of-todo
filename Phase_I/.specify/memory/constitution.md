<!-- Sync Impact Report:
Version change: 1.0.0 → 1.0.0 (initial creation)
Added sections: All sections added as initial constitution
Modified principles: none
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
Development follows a structured progression from simple to complex: starting with in-memory console applications and evolving to full-stack web apps, AI chatbots, and cloud-native deployments. Each phase builds upon the previous with increasing architectural sophistication.

### IV. Reusable Intelligence & Modularity
Components must be designed as reusable, modular units that can be leveraged across different phases and applications. Emphasis on creating reusable intelligence via Claude Code Subagents and Agent Skills to accelerate development.

### V. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced. All features must have corresponding tests before implementation completion.

### VI. Clean Architecture & Separation of Concerns
Maintain clear separation between frontend, backend, and infrastructure layers. Each component should have well-defined interfaces and responsibilities to enable independent development and testing.

## Technology Stack Standards

### Primary Technologies
- Python 3.13+ for backend services
- Next.js 16+ for frontend applications
- FastAPI for REST APIs
- SQLModel for ORM operations
- Neon Serverless PostgreSQL for database
- Claude Code and Spec-Kit Plus for spec-driven development
- Better Auth for authentication

### Infrastructure & Deployment
- Docker for containerization
- Kubernetes (Minikube/DigitalOcean) for orchestration
- Helm Charts for deployment packaging
- MCP (Model Context Protocol) for AI tool integration

## Development Workflow

### Specification Process
1. Write comprehensive specifications in the /specs directory following Spec-Kit Plus conventions
2. Generate implementation plans that align with architectural constraints
3. Break plans into atomic, testable tasks
4. Implement only what is specified in approved tasks

### Code Review & Quality Gates
- All PRs must verify compliance with specification requirements
- Code must be generated via AI agents following AGENTS.md guidelines
- Specifications must be updated if requirements change during development
- Manual code changes require explicit exception approval

## Governance

This constitution supersedes all other development practices. Amendments require documentation of the change, approval from project maintainers, and a migration plan for existing code. All development activities must comply with these principles and can be audited for compliance.

**Version**: 1.0.0 | **Ratified**: 2026-01-16 | **Last Amended**: 2026-01-16