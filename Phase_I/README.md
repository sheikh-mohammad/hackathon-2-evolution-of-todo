# Console Todo App

A command-line todo application that stores tasks in memory with temporary file persistence between sessions. Built with Python 3.13+ and Rich for beautiful console formatting.

## Features

- Add, view, update, delete, and mark tasks as complete/incomplete
- Auto-generated sequential task IDs
- Rich-formatted console interface with visual status indicators
- Temporary file persistence between sessions
- Sub-second response times for all operations
- Graceful error handling with informative messages

## Prerequisites

- Python 3.13+
- UV package manager

## Installation

1. Clone or download the repository
2. Install dependencies using UV:

```bash
uv sync
```

Or install the required packages directly:

```bash
pip install rich pytest
```

## Usage

Run the application:

```bash
python -m src.todo_app
```

Or alternatively:

```bash
cd src
python -m todo_app
```

### Available Commands

- `add` or `a` - Add a new task
- `view` or `v` - View all tasks
- `update` or `u` - Update a task
- `delete` or `d` - Delete a task
- `complete` or `c` - Mark task as complete/incomplete
- `help` or `h` - Show help information
- `quit` or `q` - Exit the application

### Example Workflow

1. Start the application: `python -m src.todo_app`
2. Add a task: Enter `add` or `a` and follow the prompts
3. View tasks: Enter `view` or `v` to see all tasks
4. Mark as complete: Enter `complete` or `c` and specify task ID
5. Update task: Enter `update` or `u` and specify task ID
6. Delete task: Enter `delete` or `d` and specify task ID
7. Exit: Enter `quit` or `q` to save and exit

## Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py              # Task data model
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py      # Business logic for task operations
│   ├── cli/
│   │   ├── __init__.py
│   │   └── todo_cli.py          # Command-line interface
│   └── utils/
│       ├── __init__.py
│       └── file_handler.py      # File persistence logic
│
tests/
├── unit/
│   ├── test_task.py             # Unit tests for Task model
│   └── test_task_service.py     # Unit tests for task service
├── integration/
│   └── test_cli_integration.py  # Integration tests for CLI functionality
└── contract/
    └── test_api_contract.py     # Contract tests for CLI interface
```

## Testing

Run the tests using pytest:

```bash
pytest
```

To run tests with verbose output:

```bash
pytest -v
```

To run specific test files:

```bash
pytest tests/unit/test_task.py
pytest tests/unit/test_task_service.py
pytest tests/integration/test_cli_integration.py
```

## Data Persistence

The application stores tasks in memory during runtime and persists them to a file named `todo_data.json` when exiting. The file is automatically loaded when the application starts.

## License

This project is part of a hackathon and is provided as-is for educational purposes.