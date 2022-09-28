# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:37:02 2022

@author: rrock
"""
def register():
    db = open("Register.txt", "r")
    a = input("Enter your EmailID: ")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if a in d:
        print("Try Again!! with other EmailID")
        register()

    elif a.count('@') != 1 and a.count('.') != 1:
        print("Please enter in a proper format")
        register()

    elif ((a.index('@'))-(a.index('.')))==1:
        print("The Email do nat match the requirments")
        register()

    elif a[0] in range(0, 9):
        print("Try starting with characters!")
        register()

    elif (a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*' or a[
        0] == '&'):
        print("Start with only characters")
        register()

    else:
        print("Username created")

    b = input("Please Enter your password: ")
    c = False

    if len(b) < 5 and len(b) > 16:
        print("Create Password with length between 5 an 16, Try Again")
        register()

    if len(b) > 5 and len(b) < 16:
        w, x, y, z = 0, 0, 0, 0
        for i in b:
            if i.isdigit():
                z += 1
            if i.islower():
                w += 1
            if i.isupper():
                x += 1
            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                y += 1
            if (w >= 1 and x >= 1 and y >= 1 and z >= 1 and w + x + y + z== len(b)):
                c = True

    if c:
        c = input("Confirm Password: ")
        while (c!= b):
            print("Password not match, Try Again")
            c = input("PLease try Again carefully: ")

    else:
        print("Try again!!")
        register()

    file = open("register.txt", "a")
    file.write(a + "," + b + "\n")
    file.close()
    login()

def login():
    A=input("Login using EmailID: ")
    A = A.strip()
    db = open("Register.txt", "r")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if A in d:
        Y=input("Please Enter your password: ")
        Y=Y.strip()
        file1=open("Register.txt","r").readlines()
        for x in file1:
            x=x.strip()
            info=x.split(",")
            if A== info[0] and Y==info[1]:
                print("Welcome to GUVI")
               
            
            else:
                F = input("Forgot Password [Y/N] : ")

                if F == "N":
                    print("try")
                    login()

                if F == "Y":
                    b = input("Create your new password with atleast one capital letter one integer and one special character: ")
                    c = False

                    if len(b) < 5 and len(b) > 16:
                        print("Create Password with length between 5 an 16, Try Again")
                        register()

                    if len(b) > 5 and len(b) < 16:
                        w, x, y, z = 0, 0, 0, 0
                        for i in b:
                            if i.isdigit():
                                z += 1
                            if i.islower():
                                w += 1
                            if i.isupper():
                                x += 1
                            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                z += 1
                            if (w >= 1 and x >= 1 and y >= 1 and z >= 1 and w + x + y + z == len(b)):
                                c = True

                    if c:
                        cp = input("Confirm Password: ")
                        while (cp != b):
                            print("Password not match, Try Again")
                            c = input("Try Again: ")

                    else:
                        print("Sorry,Try again to login")
                        login()

                    file = open("Register.txt", "w")
                    file.write(A + "," + B + "\n")
                    file.close()

    else:
        print("Unregister user you need to register first")
        register()

def welcome():
    print("Welcome to GUVI")
    print("Inorder to access you need to login and Incase your a new user then please Register")
    W=input("Login|Register[L/R]: ")
    if W=="L":
        login()
    elif W=="R":
        register()
    else:
        print("Please chose either Login or Register!!")
        welcome()
welcome()