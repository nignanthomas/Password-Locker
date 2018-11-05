#!/usr/bin/env python3.6


from user import User
from credential import Credential

import pyperclip
import random
import string

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
    '''
    Function to display a header
    '''

    print(""" \033[1;35;47m

                       .---.                                                   #
              o`  o   /    |\________________                                  #
             o`   'oooo()  | ________   _   _)                                 #
             `oo   o` \    |/        | | | |                                   #
               `ooo'   `---'         "-" |_|                                   #
                              _                _                               #
                             | |              | |                              #
          _ __   __ _ ___ ___| |     ___   ___| | _____ _ __                   #
         | '_ \ / _` / __/ __| |    / _ \ / __| |/ / _ \ '__|                  #
         | |_) | (_| \__ \__ \ |___| (_) | (__|   <  __/ |                     #
         | .__/ \__,_|___/___/______\___/ \___|_|\_\___|_|                     #
         | |                                                                   #
         |_|          ____   _                 by nignanthomas                 #
         Note: Press |CTRL|+|C| to leave at anytime !                          #
                                                                               #\033[0;0m
    """)
#end header


def menu():
    '''
    Function to display the Main Menu
    '''

    cls()
    header()
    print("Hello, Welcome to your accounts manager!")
    print('\n')
    print('\n')
    print("What would you like to do?")
    print('\n')
    print("1. Sign Up")
    print('\n')
    print("2. Login")
    print('\n')
    print("3. Exit")
#end menu

def log_menu():
    '''
    Function to display the menu for a logged in user
    '''

    print("a. Add Credential")
    print("b. Search Credential")
    print("c. Display all Credentials")
    print("d. Delete Credential")
    print("e. Logout")
#end log_menu


def session_header(u_name):
    '''
    Function to display the header, the login title and the name logged user
    '''

    cls()
    header()
    # print ('\n')
    login_header()
    print(f"            \033[1;33;40m USER SESSION: {u_name} \033[0;0m ")
    print ('\n')
#end session_header


def generate_password(pass_length):
    '''
    Function to generate a random password with a custom length
    '''
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
    gen_pass = "".join(random.choice(char) for _ in range(pass_length))
    return gen_pass
#end generate_password



def signup_header():
    '''
    Function to display sign up title
    '''
    print("""
             __     __                   __
            /__` | / _` |\ |       |  | |__)
            .__/ | \__> | \|       \__/ |

        ====================================
    """)

#end signup_header


def login_header():
    '''
    Function to display login title
    '''
    print("""
                  __   __
            |    /  \ / _` | |\ |
            |___ \__/ \__> | | \|

        ==============================
    """)

#end login_header









############  MAIN  ###############

def main():
    # header()
    menu_choice = 0
    while menu_choice != 3:
        menu()
        print("\n Your Choice: ")
        try:
            menu_choice = int(input())
        except:
            print("\033[1;31;40m Please Make a Valid Choice ! \033[0;0m")
            print ('Press Enter to continue')
            input()

        if menu_choice == 3:
            print ('\033[1;31;40m Thanks For Using --passlocker-- \033[0;0m ')
            print ('Press Enter Quit')
            input()
            break
        #end if menu_choice = 3

        elif menu_choice == 1:
            cls()
            header()
            # print ('\n')
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
            print(f"\033[1;32;40m New User {u_name} / Password: {p_word} created \033[0;0m")
            print ('Press Enter to continue')
            input()
        #end if menu_choice = 1

        elif menu_choice == 2:
            cls()
            header()
            # print ('\n')
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
                    print ('\n Your Choice: ')
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

                        print ('\n')
                        print("Password:")
                        pass_choice = ""
                        while pass_choice !="gp" or pass_choice !="ep":
                            pass_choice = input("gp. Generate Password \n ep. Enter Password \n Choice: ")
                            if pass_choice == "ep":
                                pw_account = input()
                                break
                            elif pass_choice == "gp":
                                pass_length = 0
                                while pass_length < 8:
                                    pass_length = int(input("Enter the password length(>=8): "))
                                pw_account = generate_password(pass_length)
                                break

                        save_creds(create_cred(u_name, app_name, u_account, pw_account))  # create and save new credential.
                        print ('\n')
                        print(f" \033[1;32;40m New Credential for {app_name} / User Account : {u_account}/ Password: {pw_account} created \033[0;0m ")
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
                            print(f" \033[1;32;40m Credentials for {found_cred.cred_app} Found and Copied to Clipboard: \033[0;0m ")
                            print(f"User Account: {found_cred.cred_user}")
                            print(f"Password: {found_cred.cred_pass}")
                            to_copy = f"Appname: {found_cred.cred_app} @@ User Account: {found_cred.cred_user}  @@ Password: {found_cred.cred_pass}"
                            pyperclip.copy(to_copy)
                        else:
                            print(f" \033[1;31;40m Credentials Not Found for {app_name}! \033[0;0m ")
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
                            print(" \033[1;31;40m You dont seem to have any credentials saved yet. \033[0;0m ")
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
                            if input("\033[1;31;40m Are you sure you want to delete it? (Y/N) \033[0;0m ").upper() == "Y":
                                del_cred(found_cred)
                                print()
                            print("Press Enter to continue")
                            input(f" \033[1;32;40m Credentials for {found_cred.cred_app} deleted. \033[0;0m ")
                        else:
                            print(f" \033[1;31;40m Credentials Not Found for {app_name}! \033[0;0m ")
                            print("Press Enter to continue")
                            input()

                    #end choice = d (Delete Cred)




            else:
                print("\033[1;31;40m User Not Found, Try Again! \033[0;0m ")
                print("Press Enter to continue")
                input()
            #end if logged (user authenticated)









if __name__ == '__main__':

    main()





    #
