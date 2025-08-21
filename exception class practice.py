class NotcorrectError(Exception):
    def __init__(self,password):
        self.password=password
        super().__init__(f"Requirments not met: {password}. Password must be more than 8 characters and not empty.")

def checkpass(password):
    if not len(password) >= 8:
        raise NotcorrectError(password)
    return "pass accepted"

try:
    password= input("Enter password: ")
    print(checkpass(password))
except NotcorrectError as e:
    print(e)

class registerusererror(Exception):
    pass
class Invalidusernameerror(registerusererror):
    pass
class Invalidpassworderror(registerusererror):
    pass
class Invalidemailerror(registerusererror):
    pass
def checkpass(password):
    if not len(password) >= 8:
        raise Invalidpassworderror("Password must be greater than 8 characters",password)
    return "pass accepted"

def checkuser(user):
    if not len(user) >= 5:
        raise Invalidusernameerror("Username must be at least 5 characters long",user)
    return "User name accepted."
def checkemail(email):
    if len(email) < 5 and email.count("@") !=1:
        raise Invalidemailerror("Email must be contain atleast 5 characters which include @",email)
    return "Valid email."

try:
    user= input("Enter username: ")
    print(checkuser(user))
    password= input("Enter password: ")
    print(checkpass(password))
    email= input("Enter email: ")
    print(checkemail(email))
    print("Registration Succesful!")
except registerusererror as e:
    print("Resgistration Failed:",e) 