from datetime import datetime
from typing import Dict, List, Optional
import json
import os
from ..models.task import Task
from ..utils.file_handler import FileHandler


class TaskService:
    """
    Service class for managing tasks with CRUD operations.
    Implements the TaskList operations as defined in the data model.
    """

    def __init__(self, data_file: str = "todo_data.json"):
        """
        Initialize the TaskService with an empty task list and next_id counter.
        Loads existing data from file if it exists.
        """
        self.tasks: Dict[int, Task] = {}
        self.next_id: int = 1
        self.data_file = data_file
        self.file_handler = FileHandler()

        # Load existing data if file exists
        if os.path.exists(self.data_file):
            self.load_from_file()

    def add(self, title: str, description: str = "") -> Optional[Task]:
        """
        Add a new task to the list.
        Validates task before adding, assigns auto-generated sequential ID, sets creation timestamp.

        Args:
            title: Task title
            description: Task description (optional)

        Returns:
            Created Task object or None if validation fails
        """
        # Create a temporary task to validate
        temp_task = Task(id=self.next_id, title=title, description=description)

        # Validate the task
        if not temp_task.validate():
            return None

        # Assign the new task with the next available ID
        new_task = Task(
            id=self.next_id,
            title=temp_task.title,
            description=temp_task.description,
            completed=False,
            created_at=datetime.now()
        )

        self.tasks[self.next_id] = new_task
        self.next_id += 1

        return new_task

    def get_all(self) -> List[Task]:
        """
        Retrieve all tasks in the list.
        Returns ordered list of tasks, maintaining insertion order or sorts by ID.

        Returns:
            List of all tasks
        """
        # Return tasks sorted by ID
        return sorted(self.tasks.values(), key=lambda x: x.id)

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieve specific task by ID.
        Validates ID exists in collection.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return self.tasks.get(task_id)

    def update(self, task_id: int, title: str = None, description: str = None, completed: bool = None) -> bool:
        """
        Update task properties.
        Validates updates against field constraints, preserves immutable fields (id, created_at),
        updates mutable fields (title, description, completed).

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)
            completed: New completion status (optional)

        Returns:
            True if update was successful, False otherwise
        """
        task = self.get_by_id(task_id)
        if not task:
            return False

        # Store original values in case validation fails
        original_title = task.title
        original_description = task.description
        original_completed = task.completed

        # Prepare updates
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed

        # Validate the updated task
        if not task.validate():
            # Restore original values if validation fails
            task.title = original_title
            task.description = original_description
            task.completed = original_completed
            return False

        # Update the task in the collection
        self.tasks[task_id] = task
        return True

    def delete(self, task_id: int) -> bool:
        """
        Remove task from list.
        Validates ID exists before deletion.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if deletion was successful, False otherwise
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def toggle_complete(self, task_id: int) -> bool:
        """
        Toggle completion status.
        Flips completed boolean value, validates ID exists before toggling.

        Args:
            task_id: ID of the task to toggle

        Returns:
            True if toggle was successful, False otherwise
        """
        task = self.get_by_id(task_id)
        if not task:
            return False

        task.completed = not task.completed
        self.tasks[task_id] = task
        return True

    def save_to_file(self):
        """Save all tasks and next_id to the data file."""
        data = {
            "tasks": [task.to_dict() for task in self.tasks.values()],
            "next_id": self.next_id
        }
        self.file_handler.save_data(self.data_file, data)

    def load_from_file(self):
        """Load tasks and next_id from the data file."""
        try:
            data = self.file_handler.load_data(self.data_file)
            if data and "tasks" in data and "next_id" in data:
                self.tasks = {}
                for task_data in data["tasks"]:
                    task = Task.from_dict(task_data)
                    self.tasks[task.id] = task

                self.next_id = data["next_id"]
        except FileNotFoundError:
            # If file doesn't exist, we'll start with empty data
            pass
        except Exception:
            # If there's any error loading the file, start with empty data
            print(f"Warning: Could not load data from {self.data_file}. Starting with empty task list.")
            self.tasks = {}
            self.next_id = 1