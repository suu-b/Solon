import typer
from . import user, project, dashboard

app = typer.Typer()

app.add_typer(user.app, name="user")
app.add_typer(project.app, name="project")
app.add_typer(dashboard.app, name="dashboard")

if __name__ == "__main__":
    app()