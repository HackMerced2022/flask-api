import os
import sys

# Path restructure for imports
script_dir = os.path.dirname( __file__ )
main_dir = os.path.join( script_dir, '..' )
sys.path.append( main_dir )

from web_app.database_functions.Connect import connect
from web_app.database_functions.Get_Value import get_value
from web_app.database_functions.Execute_Command import execute_command
from web_app.database_functions.Create_Table import create_table

from os import getenv
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, make_response, jsonify, request
from flask_cors import CORS

ELEPHANTSQL_DATABASE = getenv('ELEPHANTSQL_DATABASE')
ELEPHANTSQL_USERNAME = getenv('ELEPHANTSQL_USERNAME')
ELEPHANTSQL_PASSWORD = getenv('ELEPHANTSQL_PASSWORD')
ELEPHANTSQL_HOST = getenv('ELEPHANTSQL_HOST')

def create_app():
    '''Main app'''

    app = Flask(__name__)
    cors = CORS(app)    # Set up Flask to bypass CORS at the front end:

    @app.route('/', methods=['POST'])
    def index():

        # Json content type needed
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json

            # Question_id key and value type str needed
            if 'question_id' in json.keys() and type(json['question_id']) == str:

                question_id = int(json['question_id'])
    
                # Database connection
                elephantsql_client = connect(ELEPHANTSQL_DATABASE, ELEPHANTSQL_USERNAME, ELEPHANTSQL_PASSWORD, ELEPHANTSQL_HOST)

                command = '''SELECT * FROM questions_table WHERE question_id = {}'''.format(question_id)
                question_package = get_value(elephantsql_client, command)
                question_package = question_package[0]

                # Close the connection
                elephantsql_client.close()
                print('Connection is closed.')

                # Response output
                response = jsonify(
                            {'question_title': question_package[1],
                             'question_lesson': question_package[2],
                             'question_desc': question_package[3],
                             'question_a': question_package[4],
                             'question_b': question_package[5],
                             'question_c': question_package[6],
                             'question_d': question_package[7],
                             'answer': question_package[8],
                             'error': question_package[9]})

            else:
                # Key missing or value type invalid
                response = jsonify({'error':'question_id key is missing from json file or question_id value is not equal to string.'})

        else:
            # Incorrect content type
            response = jsonify({'error': 'Content-Type not supported!'}) 
   
        return response

    @app.route('/leaderboard', methods=['POST'])
    def leaderboard():

        # Json content type needed
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json

            # Question_id key and value type str needed
            if 'username' in json.keys() and type(json['username']) == str:

                username = json['username']
                questions_right = int(json['questions_right'])
                questions_wrong = int(json['questions_wrong'])
                question_accuracy = int(json['question_accuracy'])
                total_time = int(json['total_time'])
    
                # Testing username/ grabbing elements
                # Database connection
                elephantsql_client = connect(ELEPHANTSQL_DATABASE, ELEPHANTSQL_USERNAME, ELEPHANTSQL_PASSWORD, ELEPHANTSQL_HOST)

                command = '''SELECT * FROM usernames_table WHERE username = '{}';'''.format(username)
                username_package = get_value(elephantsql_client, command)

                # Close the connection
                elephantsql_client.close()
                print('Connection is closed.')

                # Quary failed
                if username_package == []:
                    # Username has not yet been created

                    # Database connection
                    elephantsql_client = connect(ELEPHANTSQL_DATABASE, ELEPHANTSQL_USERNAME, ELEPHANTSQL_PASSWORD, ELEPHANTSQL_HOST)

                    command = "INSERT INTO usernames_table (username, questions_right, questions_wrong, question_accuracy, total_time) VALUES ('{}', '{}', '{}', '{}', '{}')".format(username,
                                                                                                                                                                                    questions_right,
                                                                                                                                                                                    questions_wrong,
                                                                                                                                                                                    question_accuracy,
                                                                                                                                                                                    total_time)
                    execute_command(elephantsql_client, command)

                    # Close the connection
                    elephantsql_client.close()
                    print('Connection is closed.')

                #Quarry succeded
                else:
                    print(username_package)
                    questions_right += int(username_package[0][1])
                    questions_wrong += int(username_package[0][2])
                    question_accuracy = (questions_right / (questions_right + questions_wrong)) * 100
                    total_time += int(username_package[0][4])

                    # Convert to string
                    questions_right = str(questions_right)
                    questions_wrong = str(questions_wrong)
                    question_accuracy = str(question_accuracy)
                    total_time = str(total_time)

                    # Database connection
                    elephantsql_client = connect(ELEPHANTSQL_DATABASE, ELEPHANTSQL_USERNAME, ELEPHANTSQL_PASSWORD, ELEPHANTSQL_HOST)

                    command = "UPDATE usernames_table SET questions_right = '{}', questions_wrong = '{}', question_accuracy = '{}', total_time = '{}' WHERE username = '{}';".format(questions_right,
                                                                                                                                                                                    questions_wrong,
                                                                                                                                                                                    question_accuracy,
                                                                                                                                                                                    total_time,
                                                                                                                                                                                    username)
                    execute_command(elephantsql_client, command)

                    # Close the connection
                    elephantsql_client.close()
                    print('Connection is closed.')

                response = jsonify({'error': 'success'})


            else:
                # Key missing or value type invalid
                response = jsonify({'error':'username key is missing from json file or username value is not equal to string.'})

        else:
            # Incorrect content type
            response = jsonify({'error': 'Content-Type not supported!'}) 
   
        return response

    return app