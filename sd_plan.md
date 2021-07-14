# Software Development Plan



## Statement of Purpose and Scope

### Application Description:

This terminal application is a speed typing test. The user is able to select the desired difficulty level of the text that is given to them, ranging from easy, medium, and hard. The test begins once the user begins typing. Once the user finshes typing out the given text, the application reports the user's WPM (words per mintue), accuracy of words typed, and the total time accrued. (Possilbe leader board fucntion) The application then asks the user if they want to retake the test at a different difficulty level, randomly select another body of text at the same difficulty level or to exit the program.

### What Problem it is Designed to Solve:

The application is designed to improve the users typing speed and accuracy while testing themselves against different levels of difficulty in text. As I believe that possessing adequete typing skills is essential in many technological aspects in many industries and the importance of having competent typing skills is becoming imperative in the ever-evolving technological industries. It can improve the users working efficiency and in turn the work quality. This allows for time to be spent on other prevelant tasks.

Not only does frequently testing one's own typing ability improve typing efficiency, it can also serve as a form of entertainment. Competing against yourself or other friends can foster a competitive atomsphere and users will possilby stop seeing the application as a test and more as a form of entertainment.

### Target Audience:

The target audience for the application is for people endeavouring to improve their own typing skills. Depending on the difficulty level the user chooses, the range of the target audience changes. Such as, the easy level is more designed towards elementary/primary school students from the grades of 1-6. While the medium difficulty is more suitable for high school/secondary students randing from the grades of 8-12. Finally the hard difficulty level is desgined for college students.

### How a User will use the Application:

The user will use the application on their respective computer device. The program will run through the command line and the user may complete as many tests as they desire. Albeit the application is designed for single user use, the user may compete against another user physically or virtually.

## Features:

• **Creating a menu for user to select difficulty options.**

To begin development on the application, a menu is required to greet the user and offer options. The menu would simply include the title of the application and the difficulty options. The difficulty options are selected via user inputs for each difficulty, these inputs are 1 (easy), 2 (medium), and 3 (hard). The inputs then access a seperate file in the direcrtory of the application to select the respective dictionaries which contain keys to access different bodies of text. I utilized the random module to randomly select different bodies of text. Once the user has selected the desired difficulty, the user is then able to press the enter key to begin the test / then a buffer timer will initiate and the test will begin after the timer has finished (this is accomplished via the time module)


• **WPM System** 

One of the integral parts of a speed typing test is the WPM system, this system records the users words typed per minute. Specifically for this appilcation, it uses the net WPM to accurately report the users words typed per minute and it accomodates the users errors made while typing the given text and the errors that were also corrected while typing. This way it not only encourages speed typing, but to also precisely type the text to improve effiency. Although the gross WPM is used in the formula to calculate the net WPM, such as the following:

![WPM forumla](http://https://www.100utils.com/wp-content/uploads/2018/08/Net_WPM.png/img.png)


• **Accuracy Checker**

Another important feature to a speed typing test is to report the user's accuracy of the typed text. This is similar to the WPM system but is fundamentally different. It takes the total errors made within the user's input to the text, whether it was corrected or not. This can be calculated by taking the correct number of correct characters typed divided by the total characters given, and then mulitplied by 100%. This reports a more organic representaion of a user's typing accuracy.

• **Leaderboard System**

The leaderboard system is nice way for user's to record their WPM after completing a given text. The WPM is recorded and displayed using the pandas module to create a local leaderboard, this way the user can either strive to compete with themselves and aim for a better WPM or use it as a tool to compete with others by sharing their statistics with others.

## Intended User Experience/Interaction

The user will open the application to menu screen with a simple title of the application, accompanied with options of difficulty for the given text and the option to press enter to begin the test / and the application will notify them when the test will begin.

The application will supply the user with a body of text to complete, once the user begins typing the timer will begin. 

Once the user completes the text, the application will display their WPM, accuracy, and time it took to complete that text.

The user will also be given the option to select another difficulty, try another body of text from the same level of diffculty they selected (view the leaderboard) or exit the application.

## Control Flow Diagram

![Application flowchart](./stg_flowchart.drawio) 

## Implementation Plan

To accommodate for the limited time frame of designing and creating this application, I utilized multiple project management tools. This included Trello as the main tool to track the development of the application but this was also accompanied by a workflow table to accurately keep track of time allotted to each task. Find below the tasks/features that were prioritsed in order of importance of implementing and completing the application:

• (Priority 1): Creating a menu-like representation of the test that includes the difficulty selection for users

    1. Displaying the title and the relevant information to the user
    2. Create input validator for user input (num input and key input)
    2. Creating options for the user to select in regards to preffered difficulty using the difficulty selector funtion. 
    3. User press the enter key to begin (timer)
    4. Display option to exit application

• (Priority 2): Displaying the text for the chosen difficulty

    1. Randomly selecting a body of text from the relevant dictionary using the random.choice function in the random module
    2. Determine how to display the text itself to the user
    3. Use while loop to determine when user finishes the given text
    4. Figure out how to iterate over text when user types it out (highlight which character the user is up to)
    5. Implement ability for error-correction by the user while typing the text (e.g. backspacing)
    6. Confirming when the user completes the text
    7. Giving user option to randomly generate another body of text from same difficulty level 
    8. Implement option to return to menu for difficulty selection
    9. Create exit option for user

• (Priority 3): Creating the Net WPM system to record the user's typing productivity
    
    1. Implement timing feature to record speed in WPM (using the time module)
    2. Determine how to accomodate for corrected errors
    3. Figure out how to penalize uncorrected errors
    4. Determine how to accomodate for special characters (e.g. , . ')
    5. Record the calculated WPM and storing that value to be displayed

• (Priority 4): Implementing accuracy checker:

    1. Comparing typed entry to given text entry
    2. Fgure out how to calculate correct accuracy value
    3. Storing and displaying the recorded accuracy value when called
    4. Accomodate for special characters
    5. 

• (Priority 5): Creating local leader board system for user

    1. Display option to proceed to leaderboard after given text is completed
    2. Design leader board layout/format
    3. Storing the correct values in the appropriate column
    4. Give user option to exit, return to diffuclty selection or try again at the same level
    5. Figure out how to keep the stored values and update with new entries once other text bodies are completed