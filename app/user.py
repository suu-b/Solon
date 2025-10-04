import typer
import getpass

from db.auth.auth import register_user, login_user
from resources.banners import WELCOME_BANNER

app = typer.Typer(help="User related stuff: register, login, logout, info, delete")

@app.command()
def register(username: str):
    """Register a new user account.
    
    This command will prompt you for a password securely.
    
    Args:
        username: The username for the new account (must be unique)
    
    Example:
        register myusername
    """
    password = getpass.getpass("Password: ")
    print("Registration began...")
    register_user(username, password)

@app.command()
def login(username: str):
    """Login to your account.
    
    This command will prompt you for your password securely.
    Upon successful login, you'll see the welcome banner.
    
    Args:
        username: Your registered username
    
    Example:
        login myusername
    """
    print(f"Welcome { username }!")
    password = getpass.getpass("Password: ")
    print("Trying to log in...")
    isLogin: bool =login_user(username, password)
    if isLogin:
        print(WELCOME_BANNER)
    else:
        print("Check you username and password")   

@app.command()
def logout():
    """Logout your account.
    
    This command will logout your account. You won't be able to access the protected sections of the app.
    
    Example:
        logout
    """
    print(f"Byeeeee!")
    # TODO: Logout user from the session accordingly


@app.command()
def info():
    """Your Information.
    
    This command will log your info including your username, projects list etc.
    
    Example:
        info
    """
    print(f"User info")
    # TODO: Fetch user info from DB

@app.command()
def delete():
    """Deletes your account
    
    This command will delete your account.
    
    Example:
        info
    """
    print(f"Deleted!")
    # TODO: Delete user from DB