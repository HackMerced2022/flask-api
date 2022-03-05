from flask import Flask, make_response, jsonify

def create_app():
    '''Main app'''
    app = Flask(__name__)

    @app.route('/')
    def index():
         # Response output
        response = make_response(
                jsonify(
                    {'question_title': 'Question 1',
                     'question': 'What is the output of 7%4',
                     'a': '3',
                     'b': '6',
                     'c': '4',
                     'd': '5',
                     'answer': 'a'}
                ),
                401,
            )

        response.headers["Content-Type"] = "application/json"
        return response

    return app