# imports the specific modules that I use in the project
import string
import random
from random import choice

# tries to open a text file as read and write, but will create one if it doesnt yet work
try:
    password_list = open("password_list.txt", 'r+')
except:
    password_list = open("password_list.txt", 'a')
    password_list = open('password_list.txt', 'r+')
        
# Asks if the user wants to see saved passwords
show = input("Do you want to see saved passwords on this device? (y/n)   ")

# if the user responds with yes, then it shows the passwords and shows a little graphic that says tells the user that the code is moving on, else the code automatically moves on
if show == 'y':
    print(password_list.read())
    print( )
    print("Moving on to password generator >>>>>>")
else:
    print("Moving on to password generator >>>>>>")
run = True  # initializes the variable
print('Welcome to a totally secure password generator!')
letters = string.ascii_letters # creates the letters variable using the ascii letters function
numbers = string.digits  # creates the numbers variable using ascii
characters = string.punctuation  # creates the punctuation variable
passnum_length = int(input("Amount of passwords you want to create (only numbers): "))  # asks the user how many passwords they want and stores it as an int in a variable
try: 
    pass_length = input("Input desired password length: ")  # asks the user how long the passwords should be
    if pass_length == int:  # checks to see if the password length is an integer
        print("_________________________________________________________")  # prints a graphic
except:  # If the code raises an error/the user inputs an invalid data type then this code will be run
    while pass_length is not int:  # as long as the password length is not an integer, then the user will have to keep entering the length until it is an int
        print("Invalid input, please only input numbers")  # shows an error message 
        pass_length = int(input("Character length: "))

print('''Choose character set for password from the following (more than one is allowed):  
         1. Digits
         2. Letters
         3. Special characters
         4. Start''')  # gives the user the choices they can choose from. 
 
characterList = []  # initalizes some variables
password = ""
amount = 1
for i in range(passnum_length): # run the loop as many times as the password's length
    while run == True:  # a variable to control wether the loop stops
        password = ""  # blanks the password vairable to stop them from appending the passwords to one another
        choice = int(input("Pick a number: "))  # asks for a choice and then looks to see what the choice was and then adds the respective character set to the list of used characters
        if choice == 1:
            characterList.extend(letters)
        elif choice == 2:
            characterList.extend(numbers)
        elif choice == 3: 
            characterList.extend(characters)
        elif choice == 4:   # this is where the codee breaks from the loop
            print('___________________________________________________________')
            for x in range(int(pass_length)):  
                randomchar = random.choice(characterList)  # chooses a random character
                password += randomchar  # adds it to the password
            password_list.write('\n' + password)  # writes the password to the file
            print(str(amount) + " = " + ''.join(password))  # prints the password with some other text to show what number password it was. 
            characterList = []  # resets the passwordlist
            amount += 1  # changes the amount varirable 
            if amount -  1 >= passnum_length:  # if the amount of passwords to make has been reached, stop the code
                run = False
            
        else:
            print('Invalid option, please try again')  # error message for choosing an option

password_list.close()  # closes the document to keep it saved