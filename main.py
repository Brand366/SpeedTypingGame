import os
import sys
import shutil
import time
import random
import texts
from subprocess import call

#Fucntion to clear screen of text
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls') 

def center_output(row):
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
                print_center("Sorry, please enter a valid number.\n")
        except ValueError:
            print_center("Sorry, please enter a valid number.\n")


def text_area():
    pass



#This function is used to display the difficulty selection to user 
def start_test():

    difficulties = {
        1 : texts.easy(),
        2 : texts.med(),
        3 : texts.hard()
    }

    difficulty = validator("Press '1' for [Easy], '2' for [Medium], '3' for [Hard]\n\n")

    if difficulty in difficulties.keys():
        #print_center(f"Awesome! You have selected {}, Hav fun!\n")
        selected_text = difficulties[difficulty]
        print_center("Good luck!\n\n")
        time.sleep(1)
        clear()
        return selected_text
    

if __name__ == '__main__':
    title_screen()
    start_test()
    text_area()