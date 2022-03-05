import sys
import psycopg2
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

                # Response output
                response = jsonify(
                            {'question_title': 'Question 1',
                            'question': 'What is the output of 7%4',
                            'a': '3',
                            'b': '6',
                            'c': '4',
                            'd': '5',
                            'answer': 'a',
                            'error': 'None'})

            else:
                # Key missing or value type invalid
                response = jsonify({'error':'question_id key is missing from json file or question_id value is not equal to string.'})

        else:
            # Incorrect content type
            response = jsonify({'error': 'Content-Type not supported!'}) 
   
        return response

    return app