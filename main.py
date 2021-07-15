import os
import sys
import shutil
import time
import random
import texts
from subprocess import call

#Function to clear screen of text
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls') 

def center(row):
    pass 

#Center output through print
def print_center(row):
    print(row.center(shutil.get_terminal_size().columns))

#Application introduction
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
    


#validator for user options
def validator(prompt):
    while True:
        try:
            response = int(input(prompt.center(shutil.get_terminal_size().columns)))
            if response in [1, 2, 3]:
                return response            
            else:
                print_center("Sorry, please enter a valid number.\n\n")
        except ValueError:
            print_center("Sorry, please enter a valid number.\n\n")

#This function displays the randomly selected text from the difficulty the user selected 
def text_area():
    selected_text = start_test()
    print_center("\n\n")
    print_center(selected_text)

    user_option = validator('''
            Please find options below:

            1  - Reset text

            2 - Exit application

            \n\n''')
        
    if user_option == 1:
        return text_area()

    elif user_option == 2:
        print_center("Thanks for playing!\n\n")
        time.sleep(1)
        sys.exit()


    

def compare_texts():
    pass

def wpm():
    pass

def acc():
    pass


#This function is used to display the difficulty selection to user and store the selection of the difficulty (clears screen after user selects)
def start_test():

    difficulties = {
        1 : texts.easy(),
        2 : texts.med(),
        3 : texts.hard()
    }

    difficulty = validator("Press '1' for [Easy], '2' for [Medium], '3' for [Hard]\n\n")

    if difficulty in difficulties.keys():
        user_difficulty = difficulties[difficulty]
        #print_center(f"Awesome! You have selected {user_difficulty}, Hav fun!\n")
        print_center("Good Luck!")
        time.sleep(2)
        clear()
        return user_difficulty
        

if __name__ == '__main__':
    title_screen()
    text_area()

