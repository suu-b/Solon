import typer
from typing import Optional

app = typer.Typer(help="Manage projects: create, list, open, close, delete")

@app.command()
def create(name: str, topic: Optional[str] = None, days: Optional[int] = None):
    """
    Create a new project with optional topic and duration.
    
    Args:
        name: Name of the project
        topic: Optional topic of study
        days: Optional duration in days
    
    Example:
        solon project create "Quantum Mechanics" --topic "Physics" --days 10
    """
    print(f"Creating project: {name}")
    if topic:
        print(f"  Topic: {topic}")
    if days:
        print(f"  Duration: {days} days")
    # TODO: Add DB creation logic here

@app.command()
def list():
    """List all projects for the current user."""
    print("Listing all projects...")
    # TODO: Fetch and display from DB

@app.command()
def open(project_identifier: str):
    """Open a project by name or ID."""
    print(f"Opening project: {project_identifier}")
    # TODO: Load project context

@app.command()
def close(project_identifier: str):
    """Close a project by name or ID."""
    print(f"Closing project: {project_identifier}")
    # TODO: Update project status in DB

@app.command()
def delete(project_identifier: str):
    """Delete a project by name or ID."""
    print(f"Deleting project: {project_identifier}")
    # TODO: Remove project from DB
