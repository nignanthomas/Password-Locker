from user import User
from credential import Credential

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



################USER#############
def create_user(uname, pword):
    '''
    Function to create a new user
    '''
    new_user = User(uname, pword)
    return new_user
#end create_user


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
#end save_users


def log_user(usearch, psearch):
    '''
    Function to authenticate a user
    '''
    return User.find_by_userpass(usearch, psearch)
#end log_user


###########CRED#############
def create_cred(uname, appname, uaccount, pwaccount):
    '''
    Function to create a new credential
    '''
    new_cred = Credential(uname, appname, uaccount, pwaccount)
    return new_cred
#end create_cred


def save_creds(cred):
    '''
    Function to save user
    '''
    cred.save_cred()
#end save_creds


def find_creds(uname, appname):
    '''
    Function to search for specific credentials
    '''
    return Credential.search_cred(uname, appname)
#end find_creds


def display_all(uname):
    '''
    Function to logged user credentials
    '''
    return Credential.display_creds(uname)
#end display_all


def del_cred(cred):
    '''
    Function to delete a credential
    '''
    return cred.delete_cred()
#end del_cred




################GENERIC##############

def header():
    print("""

                       .---.
              o`  o   /    |\________________
             o`   'oooo()  | ________   _   _)
             `oo   o` \    |/        | | | |
               `ooo'   `---'         "-" |_|
                              _                _
                             | |              | |
          _ __   __ _ ___ ___| |     ___   ___| | _____ _ __
         | '_ \ / _` / __/ __| |    / _ \ / __| |/ / _ \ '__|
         | |_) | (_| \__ \__ \ |___| (_) | (__|   <  __/ |
         | .__/ \__,_|___/___/______\___/ \___|_|\_\___|_|
         | |
         |_|          ____   _                 by nignanthomas
         Note: Press |CTRL|+|C| to leave at anytime !

    """)
#end header


def menu():
    cls()
    header()
    print("Hello, Welcome to you accounts manager!")
    print('\n')
    print('\n')
    print("What would you like to do?")
    print('\n')
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
#end menu

def log_menu():
    print("a. Add Credential")
    print("b. Search Credential")
    print("c. Display all Credentials")
    print("d. Delete Credential")
    print("e. Logout")
#end log_menu


def session_header(u_name):
    cls()
    header()
    print ('\n')
    login_header()
    print(f"USER SESSION: {u_name}")
    print ('\n')
#end session_header



def signup_header():
    print("""

             __     __                   __
            /__` | / _` |\ |       |  | |__)
            .__/ | \__> | \|       \__/ |

        ====================================

    """)

#end signup_header


def login_header():
    print("""

                  __   __
            |    /  \ / _` | |\ |
            |___ \__/ \__> | | \|

        ==============================

    """)

#end login_header









############  MAIN  ###############

def main():
    header()
    menu_choice = 0
    while menu_choice != 3:
        menu()
        try:
            menu_choice = int(input())
        except:
            print("Please Make a Valid Choice !")
            print ('Press Enter to continue')
            input()

        if menu_choice == 3:
            print ('Thanks For Using --passlocker--')
            print ('Press Enter Quit')
            input()
            break
        #end if menu_choice = 3

        elif menu_choice == 1:
            cls()
            header()
            print ('\n')
            signup_header()
            print ('\n')

            print("New User")
            print("="*10)
            print ('\n')

            print("Username:")
            u_name = input()

            print("Password:")
            p_word = input()

            save_users(create_user(u_name, p_word))  # create and save new user.
            print ('\n')
            print(f"New User {u_name} / Password: {p_word} created")
            print ('Press Enter to continue')
            input()
        #end if menu_choice = 1

        elif menu_choice == 2:
            cls()
            header()
            print ('\n')
            login_header()
            print ('\n')

            print("Enter Your Username and Password")
            print("="*10)
            print ('\n')

            print("Username:")
            u_name = input()

            print("Password:")
            p_word = input()

            logged = log_user(u_name, p_word)
            if logged :
                u_name = logged.username

                session_header(u_name)

                login_choice = ""
                while login_choice != "e":
                    session_header(u_name)

                    log_menu()
                    login_choice = input()

                    if login_choice == "a":
                        session_header(u_name)

                        print("       Add Credential")
                        print("     "+"="*20)
                        print ('\n')



                        print("App Name:")
                        app_name = input()

                        print("User Account:")
                        u_account = input()

                        print("Password:")
                        pw_account = input()

                        save_creds(create_cred(u_name, app_name, u_account, pw_account))  # create and save new credential.
                        print ('\n')
                        print(f"New Credential for {app_name} / User Account : {u_account}/ Password: {pw_account} created")
                        print ('Press Enter to continue')
                        input()
                    #end choice = a (Add Cred)
                    elif login_choice == "b":
                        session_header(u_name)

                        print("       Search Credential")
                        print("     "+"="*20)
                        print ('\n')

                        app_name = input("Enter App Name:")
                        found_cred = find_creds(u_name, app_name)
                        if found_cred:
                            print(f"Here are the credentials for {found_cred.cred_app}:")
                            print(f"User Account: {found_cred.cred_user}")
                            print(f"Password: {found_cred.cred_pass}")
                        else:
                            print(f"Credentials Not Found for {app_name}!")
                        print("Press Enter to continue")
                        input()
                    #end choice = b (Search Cred)
                    elif login_choice == "c":
                        session_header(u_name)

                        print("       Display All")
                        print("     "+"="*20)
                        print ('\n')

                        if display_all(u_name):
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credential in display_all(u_name):
                                print(f"App Name: {credential.cred_app}")
                                print(f"User Account: {credential.cred_user}")
                                print(f"Password: {credential.cred_pass}")
                                print("*"*25)

                            print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')
                        print("Press Enter to continue")
                        input()
                    #end choice = c (Display All)
                    elif login_choice == "d":
                        session_header(u_name)

                        print("       Delete Credential")
                        print("     "+"="*20)
                        print ('\n')

                        app_name = input("Enter App Name:")
                        found_cred = find_creds(u_name, app_name)
                        if found_cred:
                            print(f"Here are the credentials for {found_cred.cred_app}:")
                            print(f"User Account: {found_cred.cred_user}")
                            print(f"Password: {found_cred.cred_pass}")
                            if input("Are you sure you want to delete it? (Y/N) ").upper() == "Y":
                                del_cred(found_cred)
                                print()
                            print("Press Enter to continue")
                            input(f"Credentials for {found_cred.cred_app} deleted.")
                        else:
                            print(f"Credentials Not Found for {app_name}!")
                            print("Press Enter to continue")
                            input()

                    #end choice = d (Delete Cred)




            else:
                print("User Not Found, Try Again!")
                print("Press Enter to continue")
                input()
            #end if logged (user authenticated)









if __name__ == '__main__':

    main()





    #
