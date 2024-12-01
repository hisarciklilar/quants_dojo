![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Quants Dojo

Quants Dojo is a game-like True/False quiz targeting lerners of Econometrics. It is designed to test user's knowledge in certain concepts in Econometrics and help them practise and learn as they answer questions.   

The quiz consists of 10 questions. These are designed to test and clarify the confusions and the most commonly made mistakes by the learners.   

Each ccomcept tested is phrased in two alternative ways: (i) the correct answer is True; (ii) the correct answer is false. 

The quiz questions are created once the user provides a correct id. the tru and false versions of the concept teted is chosen rtandomly for each concept. 

Users may take the quiz repeteadly. In order for them not to just enter the memorised answers from the previous round, the 

## Existing Features

### QuizGenerator

- Allows the owner of the platform to choose the quiz length
- Each True/False question in the question bank is phrased in two alternative ways, one with "True" as the correct answer and the other alternative version with "False" as the correct answer. The QuizGenerator randomly selects from these two alternatives while appending each question to the quiz question list. 

- Allows users to quit if they want to before the completion of the quiz.
- Print the number total questions answered up to the progress level and the number of correct answer after each response. Print score up to the point of progress at the end of each question response
- Clear screen for better visibility when revealing the next question.
- Makes a list of individual question scores as user proceeds in the quiz. This list of responses are coded as zero for the wrong and as one for the correct user answers. This allows for easy data store and also a straightforward calculation of the quiz score. 
- In case of a user quitting before the end of survey, scores up until quit are still recorded in a list, adding zero to the questions not answered (those which would be listed post-quit). These scores are written into the spreadsheet.
  
## Features to add

- Creating a databank of questions for different topics and allow the users to choose in which topic they test their skills.
- For those who genueniely do not know their user id, add a user option to exit the quiz during validation.
- Add a time stamp for completion of the quiz
- Comparison with the latest previous score and giving feedback

## Things to do

- Work in the code for easy ready - in particular while importing packages
- Clean redundant lines
- check for the definitions before submission
    
## Bugs

- Code written so that owner can choose the quiz length. In the current form, the quiz length is set to be 10 questions with a global variable. The spreadsheet created on google drive is designed to hold information for 10 questions. If the owner changes the value of the QUIZ_LENGTH variable to a different value, the functions will run, but the scores written to the spreadsheets will be labelled wrong in spreadsheet. One way to get around this issue would be to re-create a worksheet that would match the set quiz length.
- Registered users may use code 999 to practice and then come back to take it using their own id's. Though this is a bug, implications on learning is not bad. Users will learn as they practice.  

## Credits

- Logo is obtained from [ASCII](https://ascii.co.uk). Chosen font type: "stop". Image is cropped from "temples"