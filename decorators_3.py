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
    def secure_function(panel):
        if user["access_level"] == "admin":
            return func(panel)
    
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))

#"billing" gets passed to secure_fuction
