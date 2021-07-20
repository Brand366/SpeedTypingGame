#!/bin/bash

import os
import sys
import shutil
import time
from subprocess import call
import texts

if "--about" in sys.argv:
    print('''This application is designed to test a user's typing ability by giving the user the option to select a difficulty. After finishing typing a text, the program will report the user's accuracy and wpm. It also allows the user to see a leader board to compare against another user's score or themselves. For more information please view the help.txt file.''')
    exit()

# Function to clear terminal screen of text


def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

# This function is used to add a transition buffer between different parts of the application


def transition():
    time.sleep(5)
    clear()

# This function is used to begin the application itself by calling the integral/main functions and resets the usr_data variable


def start_test():
    global usr_data
    usr_data = []
    title_screen()
    text_area()


# This global variable collects the user's data (name, accuracy, and WPM) for use in the leader board function
usr_data = []

# Function that is recalled to use a exit function


def exit_test():
    print_center("Okay, thank you for using this speed typing test!\n\n")
    time.sleep(2)
    sys.exit()

# This function is used to prompt the user after viewing the leader board whether they would like to restart or exit the application


def restart_exit():
    re_or_ex = option_validator('''
    1 - To restart test
    
    2 - To exit application
    ''')

    if re_or_ex == 1:
        print_center("Awesome! The test will restart in a moment.")
        transition()
        start_test()
    elif re_or_ex == 2:
        exit_test()

# Simple function that centers printed text in terminal screen


def print_center(txt):
    print(txt.center(shutil.get_terminal_size().columns))

# Validator function that validates user input for numbered options and supplying the user a message when they attempt to leave via "ctl+c"


def option_validator(prompt):
    while True:
        try:
            response = int(
                input(prompt.center(shutil.get_terminal_size().columns)))
            if response in [1, 2, 3, 4, 5]:
                return response
            else:
                print_center("Sorry, please enter a valid number.\n\n")
        except ValueError:
            print_center(
                "Sorry, that appears to not be a number. Please enter a valid number.\n\n")
        except KeyboardInterrupt:
            print_center(
                "Sorry, please use the exit option to leave the application.\n")

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
    print_center("By Brandon Vonhoff\n")
    print_center("This application will test your typing ability with a randomly selected body of text from a range of difficulties. So make sure you're ready!\n")
    print_center("First, please enter your name to begin the test:\n\n")

# This function serves the purpose of grabbing the user's name and raises an assertion in the case of an empty input by the user and prompts for name again


def get_name(name="", prompt="Please enter your name here: "):
    try:
        if not name:
            name = (input(prompt))
            assert len(name) > 0
    except AssertionError:
        get_name(prompt="Please enter a valid name: ")
    return name

# This function displays the randomly selected text from the difficulty the user selected and displays options available to the user


def text_area(name=''):
    # Calling the get_name() function and then appending the user's name to the global variable usr_data to store for use in the leader board
    usr_data.append(get_name())
    print("\nThank you. You will now be taken to the difficulty selection screen. ")
    # Call transition function to add screen time buffer
    transition()
    selected_txt = difficulty_select()

    while True:
        txt_options = option_validator('''
        Please select an option below:

        1 - To show text and begin typing.

        2 - To choose new difficulty.

        3 - Exit application.

        Enter your response below:
        ''')

        # This is where the user types the selected text that is randomly generated, and calculates the time it takes to type the text
        if txt_options == 1:
            print("\nMake sure to press the enter key when finished typing text. The text will appear in a moment, make sure you're ready!\n")
            transition()
            print(f'''
            {selected_txt}\n''')
            print('''
            Enter your text below:\n\n''')
            # Times the user's input to calculate how long the user took to type the selected text that was randomly generated
            start = time.time()
            usr_txt = input('''
            ''')
            end = time.time()
            usr_time = end - start
            break
        elif txt_options == 2:
            difficulty_select()
        elif txt_options == 3:
            exit_test()

    # Call the wpm_acc function to calcualte user's accuracy and WPM, displays the data and then appends to usr_data for use in the leader board
    calc_acc_wpm = acc_wpm(selected_txt, usr_txt, usr_time)
    print("\n\n")
    print_center(f"You're accuracy was {calc_acc_wpm[0]}%\n")
    print_center(f"And you're WPM was {calc_acc_wpm[1]}\n")
    usr_data.extend(calc_acc_wpm)

    get_lb_options()

    return calc_acc_wpm

# This function displays the options for the user to select when they are in the leader boards


def get_lb_options():
    lb_options = option_validator('''
        Please select an option below:

        1 - To record your scores and show the leaderboard

        2 - To restart the test application

        3 - To exit application

        Enter your response below:
        ''')

    if lb_options == 1:
        print_center("Alright, the leader board will display momentarily.")
        transition()
        leader_board()
    elif lb_options == 2:
        print_center("Awesome! The test will restart in a moment.")
        transition()
        start_test()
    else:
        exit_test()
    return get_lb_options

# Takes the given text by the selected difficulty and the typed text by the user in text_area()
# Then calculates the WPM and accuracy after comparing the two texts and taking in the time the user spend typing the text
# Returns the calculations to be used in text_area()


def acc_wpm(selected_txt, usr_txt, usr_time):
    txt_count = len(selected_txt.split())

    txt_acc = len(set(usr_txt.split()) & set(selected_txt.split()))
    calc_acc = round(txt_acc / txt_count * 100, 2)

    calc_wpm = round((txt_count/usr_time * 60), 2)

    return calc_acc, calc_wpm

# I figured I would add a fair amount of comments here to help explain what exactly is being done in this function


def leader_board():
    # This calls the user's data and thows an error if the value for the name is erroneous
    global usr_data
    name = usr_data[0]
    try:
        acc = usr_data[1]
        wpm = usr_data[2]
    except IndexError:
        pass
    # This open with statement opens the user_data.txt file or creates it if it doesn't exist yet
    with open('user_data.txt', 'a+') as f:
        # Points to the beginning of the file and splits the data with a newline
        f.seek(0)
        data = f.read()
        if len(data) > 0:
            f.write("\n")
        # Inserts the user's data into the correct column order and set the headers for the table
        f.write(f"{usr_data[0]}, {usr_data[1]}, {usr_data[2]}")
    table_headers = '| Name |', '| Accuracy (%) |', '| WPM |'
    # Opens the user_data.txt file and sets the table layout by spliting the lines with \n characters
    with open('user_data.txt', 'r') as f:
        usr_data_table = [line.split() for line in f.read().splitlines()]
    # Slices the , character off the end of the user's name and accuracy score
    for n in usr_data_table:
        n[0] = str(n[0][:-1])
        n[1] = float(n[1][:-1])
        #n[2] = float(n[2][:-1])
    # Sorts the columns via the accuracy score using a lambda function and reversing the order to show the top accuracy score first and so on
    usr_data_table.sort(reverse=True, key=lambda x: x[1])
    # Slices the excess entries to only show the top ten accuracy score entries
    usr_data_table = usr_data_table[0:9]
    # Now this long, nested list comprehension line finds the max value/data/header that is to be printed in each column
    col_width = [max(len(str(usr_data)) for usr_data in col)
                 for col in zip(*(usr_data_table + [table_headers]))]
    # Formats the data into correct column/heading while justifying the data under the respective heading with '^' and converts to string representation
    # Then prints the heading followed by the data in the table layout
    format_spec = '{:{col_width[0]}}  {:^{col_width[1]}} {:^{col_width[2]}}'
    print_center(format_spec.format(*table_headers, col_width=col_width))
    for data_fields in usr_data_table:
        print_center(format_spec.format(*data_fields, col_width=col_width))

    restart_exit()

# This function calls the easy, med, and hard functions and stores them in a dict as key-value pairs, to be called via their key (most likely will move back into start_test())


def diff_dict():
    difficulties = {
        1: texts.easy(),
        2: texts.med(),
        3: texts.hard(),
        4: texts.all()
    }
    return difficulties

# This function asks the user to select the difficulty of the text and stores the selection of the difficulty (clears screen after user selects)


def difficulty_select():
    # Resets text stored in variable upon recalling the data
    user_difficulty = None
    difficulty = option_validator(
        "Press '1' for [Easy], '2' for [Medium], '3' for [Hard], and '4' for [Any Text]\n\n\n")

    if difficulty in diff_dict():
        user_difficulty = diff_dict()[difficulty]
        print_center(
            "Alright! You will now be taken to the text area screen.\n")
        transition()
        return user_difficulty


if __name__ == '__main__':
    start_test()
