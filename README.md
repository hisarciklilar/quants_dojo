---
output:
  html_document: default
  word_document: default
---
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Quants Dojo

Quants Dojo is a game-like True/False quiz designed for learners of Econometrics at the beginner to intermediate level. It is designed to test users' knowledge of certain concepts in Econometrics and help them practice and learn as they answer questions.

Through an API connection to a Google Drive spreadsheet, tracking of user performance for each question in each of their attempt also helps the instructors (who will be referred to as the "owner" from this point onwards) to track the progress of the learners and in which topics they tend to struggle the most.

The quiz consists of 10 questions. These are designed to test and clarify the confusions about the most commonly made mistakes by the learners.

Each concept tested is phrased in two alternative ways: (i) the correct answer is `True`; (ii) the correct answer is `False`. The true and false versions of each concept being tested are chosen randomly. This will ensure a different combination of questions each time a user calls the quiz. Because it is only the phrasing of the concept that is being changed (rather than a random selection of questions from a wider pool), changes in the user's performance will be measured accurately by tracking the scores posted on a spreadsheet.

The quiz questions are created once the user provides a correct ID. The valid ID's for testing are listed below:
  - 123, 234, 345, 456, 567, 678, 789, 890, and 912.
  - 999 is also listed as one of the registered `user id`'s, allowing guest access. This allows for a person outside the user registry to attempt the quiz.

The app is created using the Code Institutes Python Project template, which can be obtained from <https://github.com/Code-Institute-Org/p3-template>

## App's Location:

- Quants Dojo Live link: 
  -  <https://quants-dojo-20a4c624877b.herokuapp.com/>

- quants_dojo GitHub Repository: 
  -  <https://github.com/hisarciklilar/quants_dojo/>

![Quiz mockup](./readme_assets/images/quiz_mockup.png)

_Note_: The above images are obtained through http://ami.responsivedesign.is/

## User Experience

The target audience for this app is UG students of social sciences who are halfway through their degree.

### User Stories

Users of this web application expect the following:

- Navigate around the site easily without frustration.
- Easily read and understand the information provided in the pages.
- Receive immediate feedback about their performance on individual questions and an overall quiz score.
- Receive immediate feedback about the change in their progress over time.

![Welcome screen](./readme_assets/images/welcome_screen.png)
![Information screen](./readme_assets/images/information_screen.png)
![Question feedback screen](./readme_assets/images/question_feedback_screen.png)
![Quiz feedback screen](./readme_assets/images/quiz_feedback_screen.png)

### App Owner's Goals

- To break the anxiety around learning and application of econometrics by providing fun routes to learning
- Track each user's attempts (frequency and dates) to understand their work patterns better.
- Develop an understanding of the topics/concepts that the users most struggle with

## Existing Features

### Quiz Start

- The quiz is designed assuming the owner has a list of registered users in a spreadsheet. It starts with an ASCII image and a welcome message. Below these, it asks for the user's input for the `user id`
- The registered `user id`'s are stored in a spreadsheet on Google Drive. The user's input is checked against the register on the worksheet. Their progress is tracked and recorded throughout the quiz.
  
- Guest access is possible with a user of 999.
- The second page has the quiz logo. It provides brief information about the quiz and user instructions.

### Quiz Generator Module

- The Quiz Generator allows the platform owner to choose the quiz length and store it in a global variable.
- Each True/False question in the question bank is phrased in two alternative ways, one with "True" as the correct answer and the other alternative version with "False" as the correct answer. The QuizGenerator randomly selects from these two alternatives while appending each question to the quiz question list. In this way, it becomes improbable that the user will work on the same quiz in repeated attempts.

### Quiz Module

- Following the user ID check and instructions, the quiz presents the questions. One question is presented at a time by clearing the screen for a better focus.
- Users move on to the next question by pressing enter, which clears the screen for the next question. Users also have the choice of quitting the quiz by typing `quit`.
- The user receives a value error if they type anything other than `True` or `False`.
- Particular sections of the question screen are color-coded, such as the question number, the words `True` and `False`, the number of questions, and the current score.
- The user receives immediate feedback after submitting their answer. The feedback includes:
  - a message stating 'correct' or 'incorrect' with a relevant emoji
  - what the correct answer was
  - the number of correct answers and total questions answered up to the point of progress.
  - The current score is calculated based on the questions answered up to that point
- Saves a list of individual question scores as the user completes the quiz. This response list is coded as 'zero' for the wrong and 'one' for the correct user answers. This allows for easy data storage and straightforward calculation of the quiz score.
- In the case of a user quitting before the end of the survey, scores up until quitting are still recorded in a list, adding a 'zero' point to the questions not answered (those which would be listed post-quit).
- A quiz score is calculated and printed on the console at the end of the quiz. If the user is revisits the site, their latest previous score and attempt date are also printed to the console. A score  comparison is provided with an appropriate emoji.
- A progress bar is provided at the end of the quiz, running through the final calculations and tasks.
- At the very end, the user is given the option to go back to the quiz start.
- Scores are written into the spreadsheet through an API connection.

### API Connection

- A spreadsheet saved in Google Drive holds information on two worksheets: The `user_list` worksheet includes a list of registered `user id`'s who are expected to take the quiz, while the `quiz_response` worksheet tracks the performance of users for each question and the date-time they attempt the quiz. Tracking scores for each question allows the owner to analyze which questions the users struggle with the most.  
- For revisiting users, the previous scores are called from the spreadsheet, and the most recent previous score is compared with the current score.

## Data Model

The code for the app is a mixture of procedural and object-oriented programming (OOP), with more weight placed on OOP. There are three modules created for this app, each working in collaboration.

### Module 1 - Quiz Generator

This relatively smaller module is designed to create the quiz by randomly selecting a version of the question from an existing question data bank.

- Attributes:
  - quiz_questions (_list_)
  - question_data (_list of dictionaries_)
  - quiz_length (_global integer_)
- Method:
  - generate_quiz
  
### Module 2 - Quiz

This module performs operations concerning running the quiz.

- Attributes:
  - question_index (_question list index value_)
  - question_list (_list of selected questions_)
  - response (_response received_)
  - score (_quiz score_)
  - question_progress (_Boolean for quiz progress_)
  - score_list (_list of scores for individual questions_)
  
- Methods:
  - clear_terminal
  - end_of_quiz
  - reveal_question
  - check_answer
  - track_score

### Module 3 - User Database

- Attributes:
  - user_id (_integer, 3 digits_)
  - score_list (_user list of scores for individual questions_)
  - quiz_score (_user quiz score_)
  - previous_score (_user previous quiz score_)
  - previous_date_time (_most recent previous date/time of attempt_)
  - first_attempt (_Boolen for first versus revisiting user_)
- Methods:
  - call_user_id_list
  - calculate_final_score
  - calculate_quiz_score
  - add_date_to_quiz_record
  - call_previous_score
  - print_score
  - provide_feedback

Screenshots of the spreadsheet on user information are provided below:

![User List](./readme_assets/images/quants_dojo_user_list.png)
![Quiz Response](./readme_assets/images/quants_dojo_quiz_response.png)

### External Libraries Used:

- `rich`: is integrated into the project to add color and style to an otherwise black-white screen. It helps to make the look of the quiz more game-like for the user experience
- `gspread`: is used to have API functionality. Communication with a spreadsheet in Google Drive is necessary for this app to access user information and track user progress. 
- `random`: is used for random number generation during the creation of the quiz
- `os`: is used to clear the screen on enter when questions are being displayed.
- `datetime`: is used to stamp the date and time of the user's attempt on the quiz.
- `time`: is used to program the progress bar that shows at the end of the quiz. Something to show the user that calculations are running in the background.

## Future Features

- Creating a data bank of questions for different topics allows the users to choose the subject they want to test their skills.
- Add a well-functioning user database management system where users can register and create their usernames and passwords.

## Flowchart

Below is a flowchart that I created before I started the coding. The final code produced follows this logic.

![flowchart](./readme_assets/images/flowchart.png)

## Manual Testing

I tested the code both in my local workspace and on the Heroku terminal as I progressed.

### Quiz Start

| FEATURE BEING TESTED | TESTING PERFORMED                                                           | EXPECTATION                                                           | RESULT |
|----------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------|--------|
| User id input        | User presses `enter` without typing                                         | ValueError raised reminding user to input a number with 3 digits      | Pass   |
| User id input        | User types a number with more than 3 digits                                 | A ValueError is raised reminding user to input a number with 3 digits | Pass   |
| User id input        | User inputs a non-numeric value                                             | ValueError raised reminding user to input a number with 3 digits      | Pass   |
| User id input        | User inputs a valid 3 digit number but with space around (on the left or right) | Quiz proceeds to the next page; correct ID is recorded on spreadsheet     | Pass   |
| User id input        | User inputs a number with 3 digits that is not in the user register list | A message tells the user to input a value that is in the register list but also gives them the option to use 999 if they are not registered | Pass   |

### Quiz

| FEATURE BEING TESTED                                        | TESTING PERFORMED                                | EXPECTATION                              | RESULT    |
|-------------------------------------------------------------|--------------------------------------------------|------------------------------------------|-----------|
| Correctly receive user input of `True` or `False`           | Type true or false in various combinations using lowercase and capital letters as well as space on left and right of the word  | Accepts the input and triggers calculation of a score, which is presented on screen | Pass |
| Rejection of keyboard entries other than `True` and `False` | Type different combinations of letter and numbers as an input | User receives a Value Error with a reminder of the valid responses; screen clears and prints the same question on enter for the user to respond | Pass |
| Rejection of keyboard entries other than `True` and `False` | Press enter without typing any answer | User receives a Value Error with a reminder of the valid responses; screen clears and prints the same question on enter for the user to respond | Pass |
| Question number increments| Moving along the quiz providing different combinations of answers | Displayed question number increasing by one as user moves on to the next question | Pass |
| Counts of correct answers and questions responded           | Moving along the quiz providing different combinations of answers | Correct counting of correct answers and questions responded | Pass |
|Current score calculation | Moving along the quiz providing different combinations of answers | Correct calculation of score up to the point of progress | Pass |

### End of Quiz

| FEATURE BEING TESTED       | TESTING PERFORMED                                   | EXPECTATION                                                                       | RESULT    |
|----------------------------|---------------------------------------|-------------------------------------------------------------------------------------------------|-----------|
| Progress bar | Completed the quiz under various scenerios | The progress bar showing progress as background calculations and tasks progress | Pass |
| Quiz results information.  | Answered all questions in quiz as a first attempt   | Quiz score printed correctly on terminal                                          | Pass      |
| Quiz results information   | Answered all questions in quiz as a revisiting user | Quiz score printed correctly on terminal                                          | Pass      |
| Previous score information | Answered all questions in quiz as a revisiting user | Latest previous quiz score and date-time of attempt printed correctly on terminal | Pass      |
| Previous score information | Answered all questions in quiz as first attempt     | No mention of a previous quiz score on terminal. A message is printed instead, encouraging user to come back | Pass |
| Feedback based on comparison of current and previous scores                      | Took the quiz as a revisiting user | A feedback is produced and displayed based on a comparison of current and latest previous scores with a relevant emoji | Pass|
| Go back to start           | Pressed enter in response to 'Restart quiz?' question provided at the very end | Screen returns to start of the quiz on `Enter`         | Pass      |

### User Database API Connection

| FEATURE BEING TESTED | TESTING PERFORMED                                                    | EXPECTATION                                                          | RESULT    |
|----------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|-----------|
| API connection       | Data from each of the two worksheets are called and saved as lists during programming of the quiz | Correct data is exported in list format | Pass      |
| API connection       | Writing of user-specific data to `quiz_response` worksheet           | User id's, user's quiz performance for each question, total quiz score and the date-time of attempt are written to rows in worksheet | Pass | 

### Operating Systems

- The app runs without issues on the following:
  - Google Chrome on MacOS, Linux and Windows
  - Firefox on Linux
  - Android phone
- It fails to run on
  - MacOS Safari
  - iPhone (iOS) Safari and Google

## Code Institute Python Linter

The code used for the app is validated using the linter provided on <https://pep8ci.herokuapp.com/>. Below are the screenshots of these validations. No errors were returned.

### run.py

![run_py_pep8](./readme_assets/images/run_py_pep8.png)

### quiz_generator.py

![quiz_generator.py](./readme_assets/images/quiz_generator_py_pep8.png)

### quiz_start.py

![quiz_start_py](./readme_assets/images/quiz_start_py_pep8.png)

### quiz.py

![quiz.py](./readme_assets/images/quiz_py_pep8.png)

### user_database.py

![user_database.py](./readme_assets/images/user_database_py_pep8.png)

## Bugs

### Bugs Resolved

The main issue I had during the validations was the text length on a row. So I split the text and used text concatenation. I tried text wrapping but it did not produce the result I was after. Using `rich` module's panel brought an extra challenge for this. The text concatenation worked fine; it was simple but effective.

### Remaining Bugs

- The code for the app is written in a way that the owner can choose the quiz length. This is an advantage. However, the spreadsheet created on Google Drive is designed to hold information for 10 questions. If the owner changes the value of the QUIZ_LENGTH variable from 10 to a different value, the functions will run, but the scores written to the spreadsheets will be labelled wrong in the spreadsheet. One way to resolve this issue would be to recreate a worksheet matching the set quiz length. A better way to do it is to integrate the creation of the spreadsheet into the program.
- Registered users may use code 999 (instead of their own) to practice and then come back to take the quiz using their ID's, leading to a misleading understanding of their performance. Though this is a bug, the implications on learning are not dire. Users will learn as they practice.  
  
## Deploying the app on Heroku

Below are the steps that need to be followed for deployment. See [ReadMe Appendix Deployment](./readme_assets/ReadMe_Appendix_Deployment.md) for more information with screenshots.

- Place the main code for running the app in the `run.py` file
- Place the dependencies in the `requirements.txt` file using `pip3 freeze > requirements.txt`. 
- Create an account on Heroku
- Click on the `Create New App` button
- Provide an app name and choose location: Europe for residents of Europe.
- Go to the `Settings` tab.
- In the `Config Vars` section, click on `Reveal Config Vars` button.
- In the `KEY` field, type `CREDS` in capital letters. In the `VALUE` field, copy-paste the contents of the `creds.json` file
- In the new `KEY` field that appears below, type `PORT` and type `8000` in the corresponding value field
- Click `Add buildpack` button. Two buildpacks will be needed:
  
  1. `heroku/python`
  2. `heroku/nodejs`

    Ensure that Python is listed before nodejs.

- Find and select `python` from the officially supported buildpacks. Click `Add buildpack` button.
- Do the same for `nodejs`.
- Go to `Deploy` tab on top. Choose `GitHub` as the `Deployment method`. Heroku will try to establish a connection with GitHub account. Authorize the connection.
- Search for the repository name that you want to deploy and click `connect`.
- Choose `Deploy branch` for manual deployment, where one can see the progress of the deployment. Click `Enable Automatic Deploys` for automatic deployment. This will update the files as GitHub is being updated.  

## Creating a Fork

On GitHub, users may fork this repository by navigating to "Fork" and selecting "Create a new fork". One cannot fork from their repository. Hence, below, a screenshot of how this could be done is provided using a repository created by a different user:

![](./assets/images/readme-images/create-fork.png)

## Cloning a Repository

Users may clone this repository by navigating to "Code" and copying the clone link. This link can then be used in Gitpod or a local code editor.  A screenshot of the links is provided below:

![](./assets/images/readme-images/clone_repository.png)


(Please note this is not the only way to clone a repository)

## Establishing an API connection

As of November 2024, below are the steps that need to be followed to establish an API connection with a Google sheet document. See [ReadMe Appendix API Connection](./readme_assets/ReadMe_Appendix_Deployment.md) for more information with screenshots.

- Log in to `Google Cloud` and select `New Project`. Link to Google Cloud Platform <https://console.cloud.google.com/>
- Give the project a name and click `Create`
- From the left-hand-side menu, choose `APIs and services` and select `Library`
- Search for the `Google Drive API` in the `API Library`
- Select `Google Drive API` and click `Enable`
- As `Google Drive API` is selected, click on the `Create Credentials` button
- Under `Which API are you using?`, choose `Google Drive API` and select `Application data`. Click `Next`.
- Under `Service account details`, provide a `Service account name`. You will see a `Service account ID` being created with an email address for the service account. Click `Create and Continue`.
- Under `Grant this service account to the project`, choose `Project` and `Editor` as role.
- Under `Credential`, `Service Accounts`, choose the account you want to work with.
- Under `Service accounts`, ensure the service account is enabled.
- Under `Service accounts`, select the `KEY` tab at the top and then on the `KEY` page, select `ADD KEY` --> `Create new key`.
- In the opening window, choose `JSON` as the `Key type`.
- Once complete, go to `APIs and services` again and choose `Library`.
- This time, search for `Google Sheets API`. Select and `Enable` `Google Sheets API`.
- Once your `JSON` file is downloaded, copy it into your project folder and rename it `creds.json`. Add this file to `.gitignore` so private sensitive information is not publicly shared.
- Open the `creds.json` file and copy the `client_email` address to the clipboard. Paste this address on the Google sheet's `Share` window. Confirm share. This will establish of a connection between the workspace and Google Sheets.
  
## Credits

### ASCII Art

ASCII Art was used to make the app look more engaging. It is hoped that this will get the attention of potential users.

- [ASCII](https://ascii.co.uk) is used for the logo text and logo picture.
  - Logo text: Chosen font type: "stop",
  - Logo image: Cropped from "temples" image.

### Python's Rich Module

- Thanks to my mentor, Matt Bodden, for directing me to this module
- Color, formatting and emoji insertions are done through the `Rich Module`. 
  - Install the module using `pip install rich`
  - On the terminal, type `python -m rich` to access the manual
  - Documentation is provided on < https://github.com/textualize >. 
- Usage examples and explanations: 
  - [Python Rich YouTube Video by DevOps Journey](https://www.youtube.com/watch?v=JrGFQp9njas)
  - Chat GPT and Microsoft Co-Pilot for Rich Module Progress Bar
  
### Templates

- Code Institute