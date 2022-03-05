from flask import Flask, make_response, jsonify, request

def create_app():
    '''Main app'''
    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def index():
        # Json content type needed
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json

            if 'question_id' in json.keys() and type(json['question_id']) == str:

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

            else:
                response = make_response(
                    'question_id key is missing from json file or question_id value is not equal to string.', 
                     401,
                )
                response.headers["Content-Type"] = "text/plain"
                return response

        else:
            response = make_response(
                'Content-Type not supported!', 
                401,
                )
            response.headers["Content-Type"] = "text/plain"
            return response

    return app