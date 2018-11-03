#        Password-Locker

An application that allows users to create and store their passwords for various accounts.


## Created by [nignanthomas](https://github.com/nignanthomas)
02/11/2018

## Description

An application that allows us to create  and store passwords for various accounts.
Password Locker stores a user's password for their various accounts. It also allows the user to generate random password and various credentials and stores them. This ensures that a user's password is strong enough and stored safely for easy retrieval.

## User Specifications

* I will have to Sign Up in order to login
* To create a password locker account with my details - log in and password
* Store my existing login credentials. For example, I would want to store my twitter account credentials.
* Generate a password for a new credential/account. For example, let's assume that I have not yet signed up for an Instagram account, I can generate a password that I will use when I sign up for an Instagram account.

## Behaviours
| Behaviour | Input | Output |
| ------------ |:----------:| -------: |
| 1. Create user account | User: Nyakio <br> Password: mashakura| User Nyakio / Password: mashakura created|
| 2. User Login|  User: Nyakio <br> Password: mashakura |  User session : nyakio. |
| a. Add Credential|    instagram <br> Site user_name: nyak-insta <br> Site Password: 7kDzR6^l | New credential created <br> Appname:facebook <br> User Name:nyak-insta <br> Password: 7kDzR6^l  |
| Genearate or Enter existing passord|ep or gp  |Ep: None <br> or <br> gp: 99rEzR5^j |
| b. Search Credential |Appname: instagram  |Credential for instagram <br> User: Nyakio <br> Password: mashakura  |
| c. Display Credentials | DA| Appname: instagram <br> User Name: nyak-insta <br> Password:7kDzR6^l|
| d. Delete Credentials | Appname: instagram <br> Sure: Y| Credential deleted|
| 3. Exit Application | 3  | It was nice having you.......You're welcome to come again!!!! |

## Installation

Clone this using the command below:

`git clone  https://github.com/nignanthomas/Password-Locker.git`

Run the `./run.py` script on the terminal to open.

## Technologies Used

* Python 3.6
* Git version Control

## License

MIT (C) 
