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
   
#Validator function that validates user input for numbered options
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


#This function displays the randomly selected text from the difficulty the user selected and displays options available to the user
def text_area():
    selected_txt = difficulty_select()
    all_txt = diff_dict().get(4)
    random_txt = random.choice(all_txt)
    
    while True:
        user_options = option_validator('''
        Please find the options below:

        1 - To show text and begin typing.

        2 - To reset with randomly selected text.

        3 - To choose new difficulty.

        4 - Record your WPM & accuracy in the leaderboard.

        5 - Exit application.

        Enter your response below:\n
        ''')
        
        #Adds time buffer to ensure user is ready to type given text before it appears
        time.sleep(1)
        clear()
        if user_options == 1:
            print(selected_txt)
            print('')
            print("Enter your text below:\n\n")
            #Records the user's time it took to type text
            start = time.time()
            usr_txt = input("")
            end = time.time()
            break
        elif user_options == 2:
            print(random_txt)
            print('')
            print("Enter your text below:\n\n")
            start = time.time()
            usr_txt = input("")
            end = time.time()
            break
        elif user_options == 3:
            print_center(difficulty_select())
        elif user_options == 4:
            print("The Leader board will show in a moment.")
            time.sleep(1)
            clear()
            leader_board(selected_txt, calc_acc, calc_wpm)
            break
        else:
            print_center("Okay, thank you for playing!\n")
            time.sleep(2)
            sys.exit()
            
    calc_wpm_acc = wpm_acc(selected_txt, usr_txt, start, end)
    print_center(f"You're accuracy was {calc_wpm_acc[0]}%\n")
    print_center(f"And you're WPM was {calc_wpm_acc[1]}\n")
    
 
#Takes the given text by the selected difficulty and the typed text by the user
#Then calculates the WPM and accuracy after comparing the two texts and taking in the time the user spend typing the text
def wpm_acc(selected_txt, usr_txt, start, end):
    txt_count = len(selected_txt.split())

    txt_acc = len(set(usr_txt.split()) & set(selected_txt.split()))
    calc_acc = round(txt_acc / txt_count * 100, 2)

    usr_time = end - start
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

#This will call and store the user data used for the leader board feature
# def usr_data():
#     

#     return name

def leader_board(selected_txt, calc_acc, calc_wpm):
    with open ('user_data.txt', 'a+') as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        f.write(selected_txt, calc_acc, calc_wpm)

    table_headers = '| Name |', '| Accuracy |', '| WPM |'
    with open ('user_data.txt', 'r') as f:
        usr_data_table = [line.split() for line in r.read().splitlines()]

    col_width = [max(len(usr_data) for usr_data in col) for col in zip(*(usr_data_table + [headers]))]

    format_spec = '{:{col_width[0]}}  {:^{col_width[1]}} {:^{col_width[2]}}'
    print_center(format_spec.format(*headers, col_width=col_width))
    for data_fields in usr_data_table:
        print(format_spec.format(*data_fields, col_width=col_width))

#This function calls the easy, med, and hard functions and stores them in a dict as key-value pairs, to be called via their key (most likely will move back into start_test())
def diff_dict():
    difficulties = {
        1 : texts.easy(),
        2 : texts.med(),
        3 : texts.hard(),
        4 : texts.all_text()
    }
    return difficulties

#This function asks the user to select the difficulty of the text and stores the selection of the difficulty (clears screen after user selects)
def difficulty_select():
    difficulty = option_validator("Press '1' for [Easy], '2' for [Medium], '3' for [Hard]\n\n\n")

    if difficulty in diff_dict():
        user_difficulty = diff_dict()[difficulty]
        #print_center(f"Awesome! You have selected {user_difficulty}, Have fun!\n")
        print_center("You will now be taken to the next screen.\n")
        time.sleep(2)
        clear()
        return user_difficulty
        
if __name__ == '__main__':
    title_screen()
    text_area()