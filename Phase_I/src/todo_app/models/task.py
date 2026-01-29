from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with all necessary attributes.

    Attributes:
        id: Auto-generated sequential unique identifier
        title: Task title/description in brief
        description: Detailed task description (optional)
        completed: Completion status indicator
        created_at: Timestamp of task creation
    """
    id: int
    title: str
    description: Optional[str] = ""
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Initialize the created_at timestamp if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

    def validate(self) -> bool:
        """
        Validate the task according to the data model constraints.

        Returns:
            True if the task is valid, False otherwise
        """
        # Title must not be empty (after trimming whitespace)
        if not self.title or not self.title.strip():
            return False

        # Title length must be between 1-200 characters
        if len(self.title.strip()) < 1 or len(self.title.strip()) > 200:
            return False

        # Description length must not exceed 1000 characters
        if self.description and len(self.description) > 1000:
            return False

        # Completed status must be boolean (true/false)
        if not isinstance(self.completed, bool):
            return False

        # Created timestamp must be a valid datetime
        if not isinstance(self.created_at, datetime):
            return False

        return True

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary for serialization.

        Returns:
            Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Task instance from a dictionary.

        Args:
            data: Dictionary containing task data

        Returns:
            Task instance
        """
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            created_at=datetime.fromisoformat(data["created_at"])
        )