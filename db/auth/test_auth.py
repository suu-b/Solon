from auth import register_user, login_user

def test_register_and_login():
    test_username = "testuser"
    test_password = "testpassword123"

    print("Attempting to register user...")
    register_user(test_username, test_password)

    print("Attempting to login user...")
    login_user(test_username, test_password)

if __name__ == "__main__":
    test_register_and_login()