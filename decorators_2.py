'''
An application where decorators can be used is as see below where
we don't want to filter output based on a criteria
'''
import functools

user = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return "1234"

def make_secure(func):
    #this is another decorator that tells secure_function that it is wrappper for func 
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
    
    return secure_function

@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())

#however there is one problem with decorators
#if we use 
print(get_admin_password.__name__)
#we get the name secure_function instead of the get_admin_password function as the name
#so we will need to solve this problem by using functools
