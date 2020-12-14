'''
The main purpose of the decorator is that we don't want to modify the code of the main function itself
So in the example below , we have "get_admin_password" function, which just returns 1234, but let's say
we want to return 1234 only if "access_level" = "admin"
'''
user = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return "1234"

print(get_admin_password())

print(user["access_level"])

'''
So instead of creating an if statement for this function itself , we can use decorators and write it as
'''

def make_secure(func):
    def secure_function():
        print("hello there")
        if user["access_level"] == "admin":
            return func()
        else: 
            return f"No admin permissions for {user['username']}"
    return secure_function


get_admin_password = make_secure(get_admin_password)
get_admin_password()
print(get_admin_password())

The result is:
PS C:\Users\yungp_000> & python c:/Users/yungp_000/OneDrive/Documents/udemy_flask/decorators_4.py
1234
admin
hello there
hello there
1234
PS C:\Users\yungp_000> 

    
'''
Another way to think of this is

'''

def decorator_function(original_function):
    def wrapper_function():
        if user["access_level"] == "admin":
            return original_function()
    return wrapper_function

def get_admin_password():
    return "1234"

get_admin_password = decorator_function(get_admin_password)
print(get_admin_password())

this will yield
1234
    
    
