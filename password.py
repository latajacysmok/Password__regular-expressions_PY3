#Program password.py is used to detect a strong password. 
#The slogan can be said to be strong, if it consists of at least eight characters,
#it contains both uppercase and lowercase letters and at least one digit and a special character.


import re
import sys
import time

while True:
    password = input("Enter your password: ")
    e = 0
    while True:
        if e > 0:
            break
        else:
            if len(password) >= 8:
                passRegex = re.compile(r'[a-z]+')
                if passRegex.findall(password):
                    passRegex1 = re.compile(r'[A-Z]+')
                    if passRegex1.findall(password):
                        passRegex2 = re.compile(r'[0-9]+')
                        if passRegex2.findall(password):
                            passRegex3 = re.compile(r'[!@.,#$%^&*()<>?/:;"\']+')
                            if passRegex3.findall(password):
                                print(20*'-')
                                print("It has succeeded Your password is strong!!!")
                                while True:
                                    quit = input(
                                        "\nTo finish the program, enter [yes], otherwise enter [no]: ")
                                    if quit.lower() == "yes":
                                        print("We say goodbye and see you :)")
                                        time.sleep(1)
                                        sys.exit(0)
                                    elif quit.lower() == "no":
                                        print("Welcome back to the program.")
                                        time.sleep(1)
                                        e += 1
                                        break
                                    else:
                                        print("You must select [yes] or [no]!")

                            else:
                                print("The password must contain at least one special character, e.g. '!@.,#$%^&*()<>?/:;\"\\'.")
                                e += 1
                                break
                        else:
                            print("The password must contain numbers!")
                            e += 1
                            break
                    else:
                        print("The password must contain uppercase letters!")
                        e += 1
                        break
                else:
                    print("The password must contain lowercase letters!")
                    e += 1
                    break
            else:
                print("The password should contain at least 8 characters!")
                break









