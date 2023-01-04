import re
import time, datetime
from prettytable import PrettyTable


###########################################################################################################################

email_regx = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
phone_regx = re.compile(r'^(?:\+?01)?[09]\d{10,10}$')

###########################################################################################################################

def Main_Menu():
    print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print ('$$----------------------------------------$$')
    print ('$$    Welcome to the Crowd Funding App    $$')
    print ('$$----------------------------------------$$')
    print ('$$    Press 1 to Registeration            $$')
    print ('$$    Press 2 to Login !                  $$')
    print ('$$    Press 0 to Exit                     $$')
    print ('$$                                        $$')
    print ('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    while True:
        user_input = input('Enter Your selection: ')
        try:
            user_input = int(user_input)
            if user_input == 1:
                Rgstr()
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

###########################################################################################################################

def loginMenu(usr_id):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(f'$$ Welcome {mail} , You are now logged in   $$')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('$$   Press 1 to View All projects            $$')
    print('$$   Press 2 to Create New Project           $$')
    print('$$   Press 3 to Delete a Project             $$')
    print('$$   Press 4 to Search for a Project by date $$')
    print('$$   Press 5 to Edit a Project               $$')
    print('$$   Press 6 to go to the Main Menu          $$')
    print('$$   Press 0 to Exit                         $$')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    while True:
        user_input = input('Enter Your selection: ')
        try:
            user_input = int(user_input)
            if user_input == 1:
                getProjects()
                loginMenu(usr_id)
            elif user_input == 2:
                CreateProject(usr_id)
                loginMenu(usr_id)
            elif user_input == 3:
                delProject(usr_id)
                loginMenu(usr_id)
            elif user_input == 4:
                SearchProject()
                loginMenu(usr_id)
            elif user_input == 5:
                editProject(usr_id)
                loginMenu(usr_id)
            elif user_input == 6:
                Main_Menu()
            elif user_input == 0:
                print("Exit Now ........ !")
                exit()
            else:
                print("Please Choose from the Menue !")
        except ValueError:
            print("Pleaes Enter a vaild Number !")

###########################################################################################################################

def Login():
    global mail

    mail = input("Enter Your Email: ")
    passwd = input("Enter Your Password: ")
    fileobject = open("data/db.txt", "r")

    data = fileobject.readlines()
    for line in data:

        if mail == line.split(":")[2] and passwd == line.split(":")[3]:
            usr_id = line.split(":")[5]

            fileobject.close()

            loginMenu(usr_id)
            break

    print("Wrong Email or Password !")
    Login()

###########################################################################################################################

def isValidDate(msg):
    date = input(msg)
    try:
        datetime.datetime.strptime(date, '%d-%m-%Y')
        return date
    except ValueError:
        #raise ValueError()
        isValidDate("Incorrect data format, should be DD-MM-YYYY: ")


def isValidEmail(msg):
    email = input(msg)
    if re.fullmatch(email_regx, email):
        return email
    else:
        return isValidEmail("Enter a Valid email: ")


def isValidPhone(msg):
    phone = input(msg)
    if re.fullmatch(phone_regx, phone):
        return phone
    else:
        return isValidPhone("Enter a Valid phone number: ")


def isValidName(msg):
    name = input(msg)
    if not any(char.isdigit() for char in name):
        return name
    else:
        isValidName("Enter a Valid Name: ")
    return name

###########################################################################################################################

def Rgstr():
    ts = time.time()
    usr_id = int(ts)
    f_name = isValidName("Enter Your First Name: ")
    l_name = isValidName("Enter Your Last Name: ")
    email = isValidEmail("Enter Your email: ")
    passwd = input("Enter Your Password: ")
    confirmpswd = input("Enter Your Password Again: ")
    while confirmpswd != passwd:
        print("Password doesnot match !")
        passwd = input("Enter Your Password: ")
        confirmpswd = input("Please Confirm Your Password: ")

    phone = isValidPhone("Enter Your phone number: ")

    print("You Have Registered Successfully!")
    print(f"Your data (Name:{f_name} {l_name} Mail:{email} Password:{passwd} Phone Number:{phone} id:{usr_id}")

    fileobject = open("data/db.txt", "a")
    fileobject.writelines(f_name + ":" + l_name + ":" + email + ":" + passwd + ":" + phone + ":" + str(usr_id) + "\n")
    fileobject.close()

###########################################################################################################################

def CreateProject(usr_id):

    ts = time.time()
    p_id = int(ts)
    title = input("Enter Project title: ")
    details = input("Enter Project details: ")
    taregt = input("Enter Project total taregt: ")

    start_date = isValidDate("Enter Project start date (date format DD-MM-YYYY like): ")
    end_date = isValidDate("Enter Project end date (date format like DD-MM-YYYY): ")

    print("You Have Created a Project Successfully!")
    print(
        f"Your data (id:{p_id} title {title} details:{details} taregt:{taregt} start date:{start_date} end date:{end_date} usr_id: {usr_id})")

    fileobject = open("data/db_projects.txt", "a")
    fileobject.writelines(str(p_id) + ":" + title + ":" + details + ":" + taregt + ":" + str(start_date) + ":" + str(end_date) + ":" + str(usr_id))
    fileobject.close()

def getProjects():
    file = open("data/db_projects.txt", 'r')
    data = file.readlines()
    file.close()
    table = PrettyTable(['ID', 'Title', 'Description', 'Total Taregt', 'Start', 'End', 'Owner ID'])
    for line in data:
        list = line.split(":")
        table.add_row(list)
    print(table)

def delProject(usr_id):
    id = input("Enter id of the project you want to delete: ")
    flag = False
    file = open("data/db_projects.txt", 'r')
    data = file.readlines()
    file.close()
    for line in data:
        if line.split(":")[0] == id:
            if line.split(":")[6] == usr_id:
                print(line)
                del data[data.index(line)]
                print("Project Deleted !")
                flag = True
            else:
                print("Sorry You can only delete Your own projects !")
                delProject(usr_id)
    file = open("data/db_projects.txt", 'w')
    file.writelines(data)
    file.close()
    if flag == False:
        print("Not Found !")



def editProject(usr_id):
    id = input("Enter id of the project you want to edit: ")
    flag = False
    file = open("data/db_projects.txt", 'r')
    data = file.readlines()
    file.close()
    for line in data:
        if line.split(":")[0] == id:
            if line.split(":")[6] == usr_id:
                print(line)
                del data[data.index(line)]
                title = input("Enter Project title: ")
                details = input("Enter Project details: ")
                taregt = input("Enter Project total taregt: ")
                start_date = isValidDate("Enter Project start date (date format DD-MM-YYYY like): ")
                end_date = isValidDate("Enter Project end date (date format like DD-MM-YYYY): ")

                data.append(str(id) + ":" + title + ":" + details + ":" + taregt + ":" + str(start_date) + ":" + str(end_date) + ":" + str(usr_id))

                file = open("data/db_projects.txt", "a")
                file.writelines(data)
                file.close()

                print("Project Edited !")
                flag = True
            else:
                print("Sorry You can only edit Your own projects !")
                loginMenu(usr_id)
    file = open("data/db_projects.txt", 'w')
    file.writelines(data)
    file.close()
    if flag == False:
        print("Not Found !")


def SearchProject():
    pass








Main_Menu()