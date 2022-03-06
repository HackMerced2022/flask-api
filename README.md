# ProgramBase API

### Introduction

The ProgramBase API aims to handle all database-related routing in association with the ProgramBase learning web application.

### Usage

**Python Notebooks**

Located in the “notebooks” directory of this repository are the following “.ipynb” files:

-	database_questions.ipynb
-	database_connect.ipynb
-	database_leaderboard.ipynb

These files explore database creation, querying, and connecting. The “database_questions.ipynb” file contains work on creating coding questions to be populated into the questions table of the database. The “database_connect.ipynb” contains work done on database creation. Lastly, the “database_leaderboard.ipynb” file contains all the work done in relation to leaderboard creation and referencing the leaderboard table for rendering on the web page.

**Interactive Web Application**

For demonstration purposes, the outlined process developed within the python notebooks has been implemented into an interactive web application hosted on Heroku. The front end that communicates with the API Is built with an HTML5 template, custom CSS, and JavaScript. The API itself is a python-Flask application.

The deployed web application can be integrated with [Here](HackMerced2022.github.io)

**Calling API**

Example input package POST request to ``https://hackermerced-api.herokuapp.com/``` Content-Type must be equal to ```“application/json”``` in the header.
```
{ 
"question_id": 11
}

```

Example output to be received
```
{
'question_title': 	'Question 1: Basic Operations and Printing in Python',
'Question_lesson':	'''You can use jupyter notebook for python as a basic calculator.
                                    For example, for addition, 2 + 2 = 4. For subtraction, 2 - 2 = 0.
                                    For multiplication, 2 * 4 = 8. For division, 4 / 2 = 2. For exponents,
                                    2 ** 3 = 8. We also have the mod operator, where we divide 2
                                    numbers and receive the remainder as the final answer. 
 For example, if we divide 5 by 2 we get 2.5 which is a 
 quotient, but to get a remainder, we use the mod 
 operator, 5 % 2 which equals 1.''',

'question_desc':'What is the output of 7 % 4?',
'question_a': '3',
'Question_b': ’6’,
'question_c': ‘4’,
'question_d': ‘5’,
'answer': ‘a’,
'error': ‘None’}

```

Example input package POST request to ``https://hackermerced-api.herokuapp.com/leaderboard``` Content-Type must be equal to ```“application/json”``` in the header.
```
{ 
‘username’: ‘Superman’,
‘questions_right’: ‘2’,
‘quesitons_wrong’: ‘3’,
‘question_accuracy’: ‘40.0’,
‘total_time’: ‘25;
}

```

Example output to be received. Populates database with json package
```
{
'error': ‘success’
}

```
