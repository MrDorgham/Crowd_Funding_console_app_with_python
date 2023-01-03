

def Register():
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