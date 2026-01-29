# Tasks: Console Todo App

**Feature**: Console Todo App (Phase I)
**Branch**: `001-console-todo-app`
**Created**: 2026-01-28
**Input**: specs/001-console-todo-app/spec.md, plan.md, data-model.md

## Implementation Strategy

MVP approach: Implement User Story 1 (Add New Tasks) first to establish core functionality, then incrementally add other user stories. Each user story should be independently testable and deliver value.

## Dependencies

User stories are largely independent thanks to shared TaskList data structure, but implementation order follows priority (P1 stories first).

## Parallel Execution Examples

- Task model and file handler can be developed in parallel
- Individual CLI commands can be developed in parallel after core models/services exist
- Unit tests can be written in parallel with implementation

---

## Phase 1: Setup & Project Initialization

**Goal**: Establish project structure and install dependencies per implementation plan.

- [ ] T001 Initialize UV project with `uv init .` command in root directory
- [ ] T002 Add Rich dependency for CLI formatting using `uv add rich`
- [ ] T003 Add Pytest dependency for testing using `uv add pytest --dev`
- [ ] T004 Create project directory structure per plan.md: src/todo_app/{models,services,cli,utils}
- [ ] T005 Create tests directory structure: tests/{unit,integration,contract}
- [ ] T006 Create __init__.py files in all directories for Python package recognition

---

## Phase 2: Foundational Components

**Goal**: Establish core data models and persistence layer that all user stories will use.

- [ ] T007 [P] Create Task model in src/todo_app/models/task.py with id, title, description, completed, created_at fields per data-model.md
- [ ] T008 [P] Create TaskList service in src/todo_app/services/task_service.py with add(), get_all(), get_by_id(), update(), delete(), toggle_complete() methods per data-model.md
- [ ] T009 [P] Create file handler in src/todo_app/utils/file_handler.py for JSON serialization/deserialization per data-model.md
- [ ] T010 [P] Implement data validation in Task model per validation rules in data-model.md
- [ ] T011 Initialize TaskService with empty task list and next_id counter
- [ ] T012 Integrate file handler with TaskService for load/save operations

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1)

**Goal**: Implement core functionality to add new todo tasks with auto-generated sequential IDs.

**Independent Test**: The app should allow users to enter a task title and description, store it in memory, and confirm successful addition with a unique ID.

- [ ] T013 [US1] Create CLI function for add command in src/todo_app/cli/todo_cli.py
- [ ] T014 [US1] Implement user input prompts for title and description in add command
- [ ] T015 [US1] Validate title length (1-200 chars) before creating task
- [ ] T016 [US1] Call TaskService.add() method to create task with auto-generated ID
- [ ] T017 [US1] Display success confirmation message with assigned task ID
- [ ] T018 [US1] Handle validation errors gracefully with informative messages
- [ ] T019 [US1] Add 'a' alias for add command per research.md command mapping
- [ ] T020 [US1] Create unit tests for Task creation in tests/unit/test_task.py
- [ ] T021 [US1] Create unit tests for TaskService.add() in tests/unit/test_task_service.py

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Implement functionality to display all tasks in a formatted list with status indicators.

**Independent Test**: The app should display all tasks with their status (complete/incomplete), titles, descriptions, and IDs in a well-formatted console output.

- [ ] T022 [US2] Create CLI function for view command in src/todo_app/cli/todo_cli.py
- [ ] T023 [US2] Call TaskService.get_all() to retrieve all tasks
- [ ] T024 [US2] Format task list using Rich tables per research.md
- [ ] T025 [US2] Display status indicators (completed/incomplete) visually distinct per success criteria
- [ ] T026 [US2] Handle empty task list with appropriate message
- [ ] T027 [US2] Add 'v' alias for view command per research.md command mapping
- [ ] T028 [US2] Create unit tests for TaskService.get_all() in tests/unit/test_task_service.py
- [ ] T029 [US2] Create integration tests for CLI view functionality in tests/integration/test_cli_integration.py

---

## Phase 5: User Story 3 - Mark Tasks Complete/Incomplete (Priority: P1)

**Goal**: Implement functionality to toggle task completion status by ID.

**Independent Test**: The app should allow users to specify a task ID and change its completion status, with immediate feedback showing the updated status.

- [ ] T030 [US3] Create CLI function for complete command in src/todo_app/cli/todo_cli.py
- [ ] T031 [US3] Prompt user for task ID input
- [ ] T032 [US3] Call TaskService.toggle_complete() to flip completion status
- [ ] T033 [US3] Display success message with new status
- [ ] T034 [US3] Handle invalid task ID with error message
- [ ] T035 [US3] Add 'c' alias for complete command per research.md command mapping
- [ ] T036 [US3] Add 'i' option for marking incomplete specifically
- [ ] T037 [US3] Create unit tests for TaskService.toggle_complete() in tests/unit/test_task_service.py

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Implement functionality to update task details by ID.

**Independent Test**: The app should allow users to specify a task ID and update its title or description, with confirmation of the changes.

- [ ] T038 [US4] Create CLI function for update command in src/todo_app/cli/todo_cli.py
- [ ] T039 [US4] Prompt user for task ID and new title/description
- [ ] T040 [US4] Call TaskService.update() with validated changes
- [ ] T041 [US4] Display success confirmation
- [ ] T042 [US4] Handle validation errors for title/description
- [ ] T043 [US4] Handle invalid task ID with error message
- [ ] T044 [US4] Add 'u' alias for update command per research.md command mapping
- [ ] T045 [US4] Create unit tests for TaskService.update() in tests/unit/test_task_service.py

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P2)

**Goal**: Implement functionality to remove tasks by ID.

**Independent Test**: The app should allow users to specify a task ID and remove it from the in-memory storage with confirmation.

- [ ] T046 [US5] Create CLI function for delete command in src/todo_app/cli/todo_cli.py
- [ ] T047 [US5] Prompt user for task ID and confirmation
- [ ] T048 [US5] Call TaskService.delete() to remove task
- [ ] T049 [US5] Display success confirmation
- [ ] T050 [US5] Handle invalid task ID with error message
- [ ] T051 [US5] Add 'd' alias for delete command per research.md command mapping
- [ ] T052 [US5] Create unit tests for TaskService.delete() in tests/unit/test_task_service.py

---

## Phase 8: CLI Integration & Navigation

**Goal**: Implement the main CLI loop with all commands and proper navigation.

- [ ] T053 Create main CLI loop in src/todo_app/cli/todo_cli.py with command menu
- [ ] T054 Implement quit command with 'q' alias per research.md command mapping
- [ ] T055 Add graceful shutdown that saves data to temporary file
- [ ] T056 Implement error handling wrapper for all CLI commands per FR-007
- [ ] T057 Create __main__.py file to allow running as module
- [ ] T058 Add rich formatting to all CLI output per FR-008
- [ ] T059 Implement sub-second response times for all operations per NFR-001

---

## Phase 9: Polish & Cross-Cutting Concerns

**Goal**: Complete the application with proper error handling, persistence, and user experience.

- [ ] T060 Implement data persistence between sessions per FR-009
- [ ] T061 Add comprehensive error handling with retry capability per FR-007
- [ ] T062 Add input validation for all user inputs per data model constraints
- [ ] T063 Create README.md with setup instructions per deliverables
- [ ] T064 Add rich formatting to all display elements per FR-008
- [ ] T065 Implement graceful error handling that allows users to retry operations per clarifications
- [ ] T066 Add help command to show all available commands with aliases
- [ ] T067 Create contract tests for CLI interface in tests/contract/test_api_contract.py
- [ ] T068 Perform end-to-end testing of all 5 core features per SC-002
- [ ] T069 Verify all commands are intuitive and follow common CLI conventions per SC-005
