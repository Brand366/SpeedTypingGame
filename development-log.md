## Status Update 1:

 Currently I have completed the statement of purpose and the scope of the application, I have listed 4 features so far, this includes the menu/difficulty selection, WPM system, Accuracy system, and leader board feature (the leader board is tentative). I also outlined the intended user experience and interaction regarding the features of the app. I implemented a flowchart diagram that displays the flow of the program and will be altered if needed, as with the documentation.

The implmentation plan was completed earlier this morning, this was due yesterday but due to circumstances in IRL, I was unable to (fell sick... but I should be okay at this point). I am utilizing Trello and a workflow table to keep track of tasks, applying deadlines to each, and prioritising the integral features first. I also included a checklist for each feature/task which is also prioritised.

What I found so far is that prevalent modules exist already to keep track of WPM (wpm 1.51.5) and that is somewhat discouraging but I will attempt to create my own. At this point I feel I will have the most trouble integrating/creating my WPM system, and the leader board feature as well. But I will delve deeper into both subjects to accomplish these tasks.


## Status Update 2:

For this update, I have completed the difficulty functions to extract the appropriate text and then store that text in the relevant list based on length of text. Those lists are then stored in their respective functions and used in the start_test function to select the difficulty and begin the test. So far the text displays after the user selects the text with the screen being cleared beforehand with a function called clear. The clear function simply does what the name implies and clears the screen of all text. This is to prevent visual text overload on the user. 

The function that displays the text have options to either reset the text or exit the program. Will need to do revise slightly to get working as desired. Also implemented the time.sleep() function along with importing from subpross to use the call function to make the transitions a bit smoother for user experience.

So for the struggles of the application... right now it's the general flow of program that is getting me stuck essentially. I am writing out multiple flow charts, and writing pseudo code to kick-start my thought process on the flow but it never seems to click as "there are many ways to skin a cat". I know I simply have to produce a MVP at the very least and then refactor from there.