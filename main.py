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
def usr_data():
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
        except KeyboardInterrupt:
            print("     You can't leave.... please.... play my game....\n")

#This function displays the randomly selected text from the difficulty the user selected and displays options available to the user
def text_area():
    selected_txt = difficulty_select()
    print_center('\n')
    print_center(selected_txt)
    print_center('\n')
    
    while True:
        user_options = option_validator('''
        Please find the options below:

        1 - To begin typing text given text.

        2 - To reset with random text no matter the difficulty.

        3 - To choose new difficulty.

        4 - Exit application.

        ''')

        if user_options == 1:
            print_center("Enter your text below:\n\n")
            start = time.time()
            usr_txt = input("")
            end = time.time()
            break

        elif user_options == 2:
            all_text()
        elif user_options == 3:
            print_center(difficulty_select())
        else:
            print_center("Okay, thank you for playing!\n")
            time.sleep(2)
            sys.exit()

    usr_wpm_acc = wpm_acc(selected_txt, usr_txt, start, end)            
    print_center(f"You're accuracy was {usr_wpm_acc[0]}%\n")
    print_center(f"And you're WPM was {usr_wpm_acc[1]}\n")
    return selected_txt, usr_txt, start, end


#Takes the given text by the selected difficulty and the typed text by the user
#Then calculates the WPM and accuracy after comparing the two texts and taking in the time the user spend typing the text
def wpm_acc(selected_txt, usr_txt, start, end):
    

    txt_count = len(selected_txt.split())

    txt_acc = len(set(usr_txt.split()) & set(selected_txt.split()))
    usr_acc = round(txt_acc / txt_count * 100, 2)

    usr_time = end - start
    usr_wpm = round((txt_count/usr_time), 2)

    # diff1 = ''
    # diff2 = ''

    # max_txt_len = len(typed_txt) if len(given_txt)<len(typed_txt) else len(given_txt)

    # for i in range(max_txt_len):
    #     given_txt_char = given_txt[i:i+1]
    #     typed_txt_char = typed_txt[i:i+1]

    #     if given_txt_char != typed_txt_char:
    #         diff1 += given_txt_char
    #         diff2 += typed_txt_char
    # print(diff1)
    # print(diff2)

    return usr_acc, usr_wpm

#This function calls the easy, med, and hard functions and stores them in a dict as key-value pairs, to be called via their key (most likely will move back into start_test())
def diff_dict():
    difficulties = {
        1 : texts.easy(),
        2 : texts.med(),
        3 : texts.hard()
    }
    return difficulties

#This function asks the user to select the difficulty of the text and stores the selection of the difficulty (clears screen after user selects)
def difficulty_select():
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