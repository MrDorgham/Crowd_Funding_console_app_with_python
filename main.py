import re

email_regx = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
phone_regx = re.compile(r'^(?:\+?01)?[09]\d{10,10}$')


def email_check(msg):
    email = input(msg)
    if re.fullmatch(email_regx, email):
        return email
    else:
        return email_check("Enter a Valid email: ")


def phone_check(msg):
    phone = input(msg)
    if re.fullmatch(phone_regx, phone):
        return phone
    else:
        return phone_check("Enter a Valid phone number: ")


def name_check(msg):
    name = input(msg)
    if not any(char.isdigit() for char in name):
        return name
    else:
        name_check("Enter a Valid Name: ")
    return name


def Register():

    f_name = name_check("Enter Your First Name: ")
    l_name = name_check("Enter Your Last Name: ")
    email = email_check("Enter Your email: ")

    password = input("Enter Your Password: ")
    confirm_password = input("Enter Your Password Again: ")

    while confirm_password != password:
        print("Passwords match !")
        password = input("Enter Your Password: ")
        confirm_password = input("Please Confirm Your Password: ")

    phone = phone_check("Enter Your phone number: ")

    print("You Have Registered Successfully!")
    print(f"Your data (Name:{f_name} {l_name} Mail:{email} Password:{password} Phone Number:{phone} ")

    fileobject = open("data/db.txt", "a")
    fileobject.writelines(f_name + ":" + l_name + ":" + email + ":" + password + ":" + phone + "\n")
    fileobject.close()


    print("reg")
    pass
def Login():
    print("log")
    pass


def Main_Menu():
    print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print ('$$----------------------------------------$$')
    print ('$$  Welcome to the Crowd Funding Program  $$')
    print ('$$----------------------------------------$$')
    print ('$$  Press 1 to Registeration              $$')
    print ('$$  Press 2 to Login !                    $$')
    print ('$$  Press 0 to Exit                       $$')
    print ('$$                                        $$')
    print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    while True:
        user_input = input('Enter Your selection: ')
        try:
            user_input = int(user_input)
            if user_input == 1:
                Register()
                Main_Menu()
            elif user_input == 2:
                Login()
                Main_Menu()
            elif user_input == 0:
                print("Exit Now ........ !")
                exit()
            else:
                print ("Please Choose from the Menue !")
        except ValueError:
                print ("Pleaes Enter a vaild Number !")

Main_Menu()