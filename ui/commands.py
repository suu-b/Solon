import sys
import typer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from auth.auth import register_user, login_user

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}!")

@app.command()
def register(username: str, password: str):
    print("Registration began...")
    register_user(username, password)

@app.command()
def login(username: str, password: str):
    print("Trying to log in...")
    login_user(username, password)