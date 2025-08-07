import bcrypt
from db.client import supabase

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def register_user(username: str, password: str) -> bool:
    hashed = hash_password(password)
    exisiting = supabase.table("users").select("id").eq("username", username).execute()
    if exisiting.data:
        print("Username already exists")    
        return False
    res = supabase.table("users").insert({
        "username": username,
        "password_hash": hashed
    }).execute()
    print("User registered successfully.")
    return True    


def login_user(username: str, password: str) -> bool:
    res = supabase.table("users").select("*").eq("username", username).execute()
    if not res.data:
        print("User not found.")
        return False
    user = res.data[0]
    if verify_password(password, user["password_hash"]):
        print("Login successful.")
        return True
    else:
        print("Incorrect password.")
        return False       