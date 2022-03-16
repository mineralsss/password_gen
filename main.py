import random
import string
import time

character= list(string.ascii_letters+ string.digits + "~!@#$%^&*()_+-=[]{}|\:;'<>?,./")
def Create_Password():
    User_Input = int(input("Password length: "))
    random.shuffle(character)
    password= []
    for i in range(User_Input):
        password.append(random.choice(character))
    print("".join(password))
Create_Password()
time.sleep(5)

        


      