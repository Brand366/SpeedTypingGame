import os
import sys
import shutil
import time
import random
import textwrap as tw
import texts
from subprocess import call

#Function to clear terminal screen of text
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls') 

#Simple function that centers printed text in terminal screen
def print_center(txt):
    print(txt.center(shutil.get_terminal_size().columns))
    
#May just get rid of (placeholder)
#def input_center(row):
#    cols, rows = shutil.get_terminal_size()
#    for line in tw.wrap(row + usr_input, cols):
#        print(line.center(cols))

#Application introduction that displays title, author, and short description of the app
def title_screen():
    print_center("\n\n")
    print_center("                                          ▄▄                                      ▄▄                                                         ")
    print_center(" ▄█▀▀▀█▄█                               ▀███     ███▀▀██▀▀███                     ██                        ███▀▀██▀▀███                ██   ")
    print_center("▄██    ▀█                                 ██     █▀   ██   ▀█                                               █▀   ██   ▀█                ██   ")
    print_center("▀███▄   ▀████████▄  ▄▄█▀██  ▄▄█▀██   ▄█▀▀███          ██    ▀██▀   ▀██▀████████▄▀███ ▀████████▄  ▄█▀█████        ██      ▄▄█▀██ ▄██▀████████ ")
    print_center("  ▀█████▄ ██   ▀██ ▄█▀   ██▄█▀   ██▄██    ██          ██      ██   ▄█   ██   ▀██  ██   ██    ██ ▄██  ██          ██     ▄█▀   ████   ▀▀ ██   ")
    print_center("▄     ▀██ ██    ██ ██▀▀▀▀▀▀██▀▀▀▀▀▀███    ██          ██       ██ ▄█    ██    ██  ██   ██    ██ ▀█████▀          ██     ██▀▀▀▀▀▀▀█████▄ ██   ")
    print_center("██     ██ ██   ▄██ ██▄    ▄██▄    ▄▀██    ██          ██        ███     ██   ▄██  ██   ██    ██ ██               ██     ██▄    ▄█▄   ██ ██   ")
    print_center("█▀█████▀  ██████▀   ▀█████▀ ▀█████▀ ▀████▀███▄      ▄████▄      ▄█      ██████▀ ▄████▄████  ████▄███████       ▄████▄    ▀█████▀██████▀ ▀████")
    print_center("          ██                                                  ▄█        ██                      █▀     ██                                    ")
    print_center("        ▄████▄                                              ██▀       ▄████▄                    ██████▀                                      \n\n")
    print_center("By Brandon Vonhoff\n\n")
    print_center("This application will test your typing ability, so make sure you're ready!\n\n")
    print_center("First, please select the desired level of difficulty:\n\n")
   
#This will call and store the user data used for the leader board feature
def user_data():
    name = input("Please enter your name to be added to the leader board: ")
    #call wpm and acc funtions here and then append to external txt file to be called when user finishes test
    return name

#May just get rid of (placeholder)
def str_validator(prompt):
    pass


#Validator function that validates user input for numbered options
def option_validator(prompt):
    while True:
        try:
            response = int(input(prompt.center(shutil.get_terminal_size().columns)))
            if response in [1, 2, 3, 4]:
                return response
            else:
                print_center("\nSorry, please enter a valid number.\n\n")         
        except ValueError:
            print_center("\nSorry, that appears to not be a number. Please enter a valid number.\n\n")

#This function displays the randomly selected text from the difficulty the user selected and displays options available to the user
def text_area():
    selected_txt = start_test()
    print_center('\n')
    print_center(selected_txt)
    print_center('\n')
    
    while True:
        
        user_options = option_validator('''
        Please find the options below:

        1 - Reset given text.

        2 - Reset with new difficulty.

        3 - To begin typing text given text.

        4 - Exit application.

        ''')

        if user_options == 1:
            reset_txt = texts.easy()
            print_center(reset_txt)

        elif user_options == 2:
            print_center(start_test())

        elif user_options == 3:
            print_center("Enter your text below:\n\n")
            usr_txt = input("")
            break
        else:
            print_center("Okay, thank you for playing!\n")
            time.sleep(2)
            sys.exit()

    print_center(acc(selected_txt, usr_txt))

    return selected_txt, usr_txt 

#Displays the users options within the text area
def usr_txt_options():
    pass
    

#Calculates the users wpm after comparing text
def wpm():
    pass

#Calculates accuracy of typed text by the user when compared to given text
def acc(selected_txt, usr_txt):

    given_txt = selected_txt
    typed_txt = usr_txt
    
    same_charcters = ''

    try:
        for i in range(len(given_txt)):
            if given_txt[i] == typed_txt[i]:
                same_charcters += given_txt[i]
    except IndexError:
        pass
             
    txt_acc = len(same_charcters) / len(given_txt) * 100

    return str(txt_acc)

#This function calls the easy, med, and hard functions and stores them in a dict as key-value pairs, to be called via their key
def diff_dict():
    difficulties = {
        1 : texts.easy(),
        2 : texts.med(),
        3 : texts.hard()
    }
    return difficulties

#This function asks the user to select the difficulty of the text and stores the selection of the difficulty (clears screen after user selects)
def start_test():

    difficulty = option_validator("Press '1' for [Easy], '2' for [Medium], '3' for [Hard]\n\n")

    if difficulty in diff_dict():
        user_difficulty = diff_dict()[difficulty]
        #print_center(f"Awesome! You have selected {user_difficulty}, Hav fun!\n")
        print_center("Good Luck!\n")
        time.sleep(2)
        clear()
        return user_difficulty
        

if __name__ == '__main__':
    title_screen()
    text_area()