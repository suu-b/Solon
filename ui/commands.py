import typer
from pathlib import Path
import getpass

from db.auth.auth import register_user, login_user
from resources.banners import WELCOME_BANNER

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}!")

@app.command()
def register(username: str):
    password = getpass.getpass("Password: ")
    print("Registration began...")
    register_user(username, password)

@app.command()
def login(username: str):
    print(f"Welcome { username }!")
    password = getpass.getpass("Password: ")
    print("Trying to log in...")
    isLogin: bool =login_user(username, password)
    if isLogin:
        print(WELCOME_BANNER)
    else:
        print("Check you username and password")    
