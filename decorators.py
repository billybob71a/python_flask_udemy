'''
An application where decorators can be used is as see below where
we don't want to filter output based on a criteria
'''

user = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
    
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())

In the above example, we made our own funciton called "make_secure"
