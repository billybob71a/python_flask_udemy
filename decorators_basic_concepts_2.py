#here we are using the at sign for the decorator 

user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    def secure_function():
        print("hello there")
        if user["access_level"] == "admin":
            return func()
        else: 
            return f"No admin permissions for {user['username']}"
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())
