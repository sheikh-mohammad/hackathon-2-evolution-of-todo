from typing import Optional
import sys
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from ..services.task_service import TaskService


class TodoCLI:
    """
    Command-line interface for the Todo application.
    Implements all the required commands with Rich formatting.
    """

    def __init__(self):
        """Initialize the CLI with a task service and console."""
        self.task_service = TaskService()
        self.console = Console()

    def run(self):
        """Main CLI loop that handles user commands."""
        self.console.print("[bold blue]Welcome to the Todo App![/bold blue]")
        self.console.print("Type 'help' for available commands or 'quit' to exit.\n")

        while True:
            try:
                command = Prompt.ask("[green]Todo App[/green]", default="help").strip().lower()

                if command in ['quit', 'q']:
                    self._handle_quit()
                    break
                elif command in ['add', 'a']:
                    self._handle_add()
                elif command in ['view', 'v']:
                    self._handle_view()
                elif command in ['update', 'u']:
                    self._handle_update()
                elif command in ['delete', 'd']:
                    self._handle_delete()
                elif command in ['complete', 'c']:
                    self._handle_complete()
                elif command in ['help', 'h']:
                    self._handle_help()
                else:
                    self.console.print(f"[red]Unknown command: {command}[/red]")
                    self.console.print("Type 'help' for available commands.\n")

            except KeyboardInterrupt:
                self.console.print("\n[bold yellow]Received interrupt signal. Quitting...[/bold yellow]")
                self._handle_quit()
                break
            except EOFError:
                self.console.print("\n[bold yellow]End of input received. Quitting...[/bold yellow]")
                self._handle_quit()
                break

    def _handle_add(self):
        """Handle the add command to create a new task."""
        self.console.print("\n[bold]Adding a new task:[/bold]")

        title = Prompt.ask("Enter task title")

        # Validate title length
        if not title or len(title.strip()) < 1 or len(title.strip()) > 200:
            self.console.print("[red]Error: Title must be between 1 and 200 characters.[/red]\n")
            return

        description = Prompt.ask("Enter task description (optional)", default="")

        # Validate description length
        if len(description) > 1000:
            self.console.print("[red]Error: Description cannot exceed 1000 characters.[/red]\n")
            return

        # Add the task
        task = self.task_service.add(title.strip(), description)

        if task:
            self.console.print(f"[green]Task added successfully with ID: {task.id}[/green]\n")
        else:
            self.console.print("[red]Error: Failed to add task. Please check your input.[/red]\n")

    def _handle_view(self):
        """Handle the view command to display all tasks."""
        tasks = self.task_service.get_all()

        if not tasks:
            self.console.print("\n[yellow]No tasks found.[/yellow]\n")
            return

        table = Table(title="Your Tasks")
        table.add_column("ID", style="dim", width=5)
        table.add_column("Title", min_width=15)
        table.add_column("Description", min_width=20)
        table.add_column("Status", justify="center")
        table.add_column("Created", style="dim")

        for task in tasks:
            status = "[green]✓ Complete[/green]" if task.completed else "[red]○ Pending[/red]"
            table.add_row(
                str(task.id),
                task.title,
                task.description if task.description else "[italic dim]No description[/italic dim]",
                status,
                task.created_at.strftime("%Y-%m-%d %H:%M")
            )

        self.console.print("\n", table, "\n")

    def _handle_update(self):
        """Handle the update command to modify a task."""
        self.console.print("\n[bold]Updating a task:[/bold]")

        try:
            task_id_str = Prompt.ask("Enter task ID to update")
            task_id = int(task_id_str)
        except ValueError:
            self.console.print("[red]Error: Invalid task ID. Please enter a number.[/red]\n")
            return

        # Check if task exists
        task = self.task_service.get_by_id(task_id)
        if not task:
            self.console.print(f"[red]Error: Task with ID {task_id} not found.[/red]\n")
            return

        self.console.print(f"Current task: {task.title}")

        # Get new values or keep current ones
        new_title = Prompt.ask("Enter new title (or press Enter to keep current)", default=task.title)

        # Validate title length
        if new_title and (len(new_title.strip()) < 1 or len(new_title.strip()) > 200):
            self.console.print("[red]Error: Title must be between 1 and 200 characters.[/red]\n")
            return

        new_description = Prompt.ask("Enter new description (or press Enter to keep current)",
                                   default=task.description)

        # Validate description length
        if len(new_description) > 1000:
            self.console.print("[red]Error: Description cannot exceed 1000 characters.[/red]\n")
            return

        # Update the task
        success = self.task_service.update(
            task_id=task_id,
            title=new_title if new_title != task.title else None,
            description=new_description if new_description != task.description else None
        )

        if success:
            self.console.print(f"[green]Task {task_id} updated successfully![/green]\n")
        else:
            self.console.print(f"[red]Error: Failed to update task {task_id}. Please check your input.[/red]\n")

    def _handle_delete(self):
        """Handle the delete command to remove a task."""
        self.console.print("\n[bold]Deleting a task:[/bold]")

        try:
            task_id_str = Prompt.ask("Enter task ID to delete")
            task_id = int(task_id_str)
        except ValueError:
            self.console.print("[red]Error: Invalid task ID. Please enter a number.[/red]\n")
            return

        # Check if task exists
        task = self.task_service.get_by_id(task_id)
        if not task:
            self.console.print(f"[red]Error: Task with ID {task_id} not found.[/red]\n")
            return

        self.console.print(f"Task to delete: {task.title}")

        confirm = Confirm.ask("Are you sure you want to delete this task?")

        if confirm:
            success = self.task_service.delete(task_id)

            if success:
                self.console.print(f"[green]Task {task_id} deleted successfully![/green]\n")
            else:
                self.console.print(f"[red]Error: Failed to delete task {task_id}.[/red]\n")
        else:
            self.console.print("[yellow]Task deletion cancelled.[/yellow]\n")

    def _handle_complete(self):
        """Handle the complete command to toggle task completion status."""
        self.console.print("\n[bold]Toggle task completion:[/bold]")

        try:
            task_id_str = Prompt.ask("Enter task ID to toggle completion status")
            task_id = int(task_id_str)
        except ValueError:
            self.console.print("[red]Error: Invalid task ID. Please enter a number.[/red]\n")
            return

        # Check if task exists
        task = self.task_service.get_by_id(task_id)
        if not task:
            self.console.print(f"[red]Error: Task with ID {task_id} not found.[/red]\n")
            return

        # Toggle completion status
        success = self.task_service.toggle_complete(task_id)

        if success:
            new_status = "completed" if task.completed else "incomplete"
            self.console.print(f"[green]Task {task_id} marked as {new_status}![/green]\n")
        else:
            self.console.print(f"[red]Error: Failed to toggle completion status for task {task_id}.[//red]\n")

    def _handle_quit(self):
        """Handle the quit command to gracefully shut down the app."""
        self.console.print("[blue]Saving tasks and exiting...[/blue]")
        self.task_service.save_to_file()
        self.console.print("[bold green]Tasks saved successfully. Goodbye![/bold green]")

    def _handle_help(self):
        """Display help information with all available commands."""
        self.console.print("\n[bold]Available Commands:[/bold]")
        self.console.print("  [green]add[/green] or [green]a[/green]     - Add a new task")
        self.console.print("  [green]view[/green] or [green]v[/green]    - View all tasks")
        self.console.print("  [green]update[/green] or [green]u[/green]  - Update a task")
        self.console.print("  [green]delete[/green] or [green]d[/green]  - Delete a task")
        self.console.print("  [green]complete[/green] or [green]c[/green] - Toggle task completion status")
        self.console.print("  [green]help[/green] or [green]h[/green]    - Show this help message")
        self.console.print("  [green]quit[/green] or [green]q[/green]    - Exit the application\n")


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    try:
        cli.run()
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()