import os
import sys

# Path restructure for imports
script_dir = os.path.dirname( __file__ )
main_dir = os.path.join( script_dir, '..' )
sys.path.append( main_dir )

from web_app.database_functions.Connect import connect
from web_app.database_functions.Get_Value import get_value

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
                            'question': question_package[2],
                            'a': question_package[3],
                            'b': question_package[4],
                            'c': question_package[5],
                            'd': question_package[6],
                            'answer': question_package[7],
                            'error': question_package[8]})

            else:
                # Key missing or value type invalid
                response = jsonify({'error':'question_id key is missing from json file or question_id value is not equal to string.'})

        else:
            # Incorrect content type
            response = jsonify({'error': 'Content-Type not supported!'}) 
   
        return response

    return app