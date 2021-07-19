import os
import sys
import shutil
import time
import random
import texts
import textwrap as tw
from subprocess import call

# Function to clear terminal screen of text
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

# This function is used to add transition buffer between different parts of the application 
def transition():
    time.sleep(3)
    clear()

# Function that is recalled to use a exit function
def exit_test():
    print_center("Okay, thank you for using this speed typing test!\n\n")
    time.sleep(2)
    sys.exit()

# Simple function that centers printed text in terminal screen
def print_center(txt):
    print(txt.center(shutil.get_terminal_size().columns))

# Validator function that validates user input for numbered options
def option_validator(prompt):
    while True:
        try:
            response = int(input(prompt.center(shutil.get_terminal_size().columns)))
            if response in [1, 2, 3, 4, 5]:
                return response
            else:
                print_center("Sorry, please enter a valid number.\n\n")         
        except ValueError:
            print_center("Sorry, that appears to not be a number. Please enter a valid number.\n\n")
        except KeyboardInterrupt:
            print("     You can't leave.... please.... play my game....\n")
    
# May just get rid of (placeholder)
# def input_center(row):
#    cols, rows = shutil.get_terminal_size()
#    for line in tw.wrap(row + usr_input, cols):
#        print(line.center(cols))

# Application introduction that displays title, author, and short description of the app
def title_screen():
    print_center("\n")
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

# This global variable collects the user's data (name, accuracy, and WPM) for use in the leader board function
usr_data = []

# This function serves the purpose of grabbing the user's name and raises and assertion in the case of an empty input by the user
def get_name(name="", prompt="Please enter your name here for the leader board: "):
    try:
        if not name: 
            name = (input(prompt))
            assert len(name) > 0
    except AssertionError:
        get_name(prompt="Enter a valid name.")
    return name

# This function displays the randomly selected text from the difficulty the user selected and displays options available to the user
def text_area(name=''):
    # Calling the get_name() function and then appending the user's name to the global variable usr_data to store for use in the leader board
    usr_data.append(get_name())
    print("\nThank you, you will now be shown some options before beginning :) \n")
    selected_txt = difficulty_select()
    transition()
    
    while True:
        txt_options = option_validator('''
        Please select an option below:

        1 - To show text and begin typing.

        2 - To choose new difficulty.

        3 - Exit application.

        Enter your response below:\n
        ''')
        
        # Call transition function to add screen time buffer
        
        if txt_options == 1:
            print("Make sure to press the enter key when finished typing text. The text will appear in a moment, make sure you're ready!\n")
            transition()
            print_center(f"{selected_txt}\n")
            print("Enter your text below:\n\n")
            start = time.time()
            usr_txt = input("")
            end = time.time()
            usr_time = end - start
            break
        elif txt_options == 2:
            text_area()
        elif txt_options == 3:
            exit_test()

    # Call the wpm_acc function to calcualte user's accuracy and WPM, displays the data and then appends to usr_data for use in the leader board
    calc_acc_wpm = acc_wpm(selected_txt, usr_txt, usr_time)
    print_center(f"You're accuracy was {calc_acc_wpm[0]}%\n")
    print_center(f"And you're WPM was {calc_acc_wpm[1]}\n")
    usr_data.extend(calc_acc_wpm)

    return calc_acc_wpm
 
# Takes the given text by the selected difficulty and the typed text by the user
# Then calculates the WPM and accuracy after comparing the two texts and taking in the time the user spend typing the text
def acc_wpm(selected_txt, usr_txt, usr_time):
    txt_count = len(selected_txt.split())

    txt_acc = len(set(usr_txt.split()) & set(selected_txt.split()))
    calc_acc = round(txt_acc / txt_count * 100, 2)

    calc_wpm = round((txt_count/usr_time * 60), 2)
     
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

    return calc_acc, calc_wpm

# This function displays the options for the user to select when they are in the leader boards 
def get_lb_options():
    lb_options = option_validator('''
        Please select an option below:

        1 - To record your scores and show the leaderboard

        2 - To restart the test application

        3 - Exit application
        ''')

    if lb_options == 1:
        leader_board()
    elif lb_options == 2:
        print_center("Awesome! The test will restart in a moment.")
        transition()
        start_test()
    else:
        exit_test()
    return get_lb_options
# 
def leader_board():
    global usr_data
    name = usr_data[0]
    try:
        acc = usr_data[1]
        wpm = usr_data[2]
    except IndexError:
        pass

    with open ('user_data.txt', 'a+') as f:
        f.seek(0)
        data = f.read()
        if len(data) > 0:
            f.write("\n")
        f.write(f"{usr_data[0]}, {usr_data[1]}, {usr_data[2]}")
    table_headers = '| Name |', '| Accuracy |', '| WPM |'
    with open ('user_data.txt', 'r') as f:
        usr_data_table = [line.split() for line in f.read().splitlines()]
    for n in usr_data_table:
        n[1] = float(n[1][:-1])
        n[2] = float(n[2][:-1])
    usr_data_table.sort(reverse=True, key=lambda x: x[1])
    usr_data_table = usr_data_table[0:9]      
    col_width = [max(len(str(usr_data)) for usr_data in col) for col in zip(*(usr_data_table + [table_headers]))]

    format_spec = '{:{col_width[0]}}  {:^{col_width[1]}} {:^{col_width[2]}}'
    print_center(format_spec.format(*table_headers, col_width=col_width))
    for data_fields in usr_data_table:
        print_center(format_spec.format(*data_fields, col_width=col_width))

# This function calls the easy, med, and hard functions and stores them in a dict as key-value pairs, to be called via their key (most likely will move back into start_test())
def diff_dict():
    difficulties = {
        1 : texts.easy(),
        2 : texts.med(),
        3 : texts.hard(),
        4 : texts.all()
    }
    return difficulties

# This function asks the user to select the difficulty of the text and stores the selection of the difficulty (clears screen after user selects)
def difficulty_select():
    # Resets text stored in variable upon recalling the data 
    user_difficulty = None
    difficulty = option_validator("Press '1' for [Easy], '2' for [Medium], '3' for [Hard], and '4' for [Any Text]\n\n\n")

    if difficulty in diff_dict():
        user_difficulty = diff_dict()[difficulty]
        print_center("Alright! You will now be taken to the text area screen.\n")
        transition()
        return user_difficulty

# This function is used to begin the application itself by calling the integral/main functions
def start_test():
    title_screen()
    text_area()
        
if __name__ == '__main__':
    start_test()