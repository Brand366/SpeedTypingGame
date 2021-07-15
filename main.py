import sys
import shutil
import time
import random
from quotes import texts

def center_output(row):
    pass

#Center output through print
def print_center(row):
    print(row.center(shutil.get_terminal_size().columns))

#Application introduction
def title_screen():
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
            user_input = int(input(prompt))
            if user_input in [1, 2, 3]:
                return user_input            
            else:
                print_center("Sorry, please enter a valid number.\n")
        except ValueError:
            print_center("Sorry, please enter a valid number.\n")



def start_test():

    difficulties = {
        1 : texts.easy(),
        2 : texts.med(),
        3 : texts.hard()
    }

    difficulty = validator("Press '1' for [Easy], '2' for [Medium], '3' for [Hard]\n\n")

    if difficulty in difficulties.keys():
        print_center(f"Awesome! You have selected {}, Hav fun!\n")
        print_center("Good luck!\n")

if __name__ == '__main__':
    title_screen()
    start_test()