import openai_test
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/summary_response', methods=['GET', 'POST'])
def single_summary():
    if request.method == 'POST':
        title = request.json['title']
        content = request.json['content']
        return 'post'
    else:
       return openai_test.get_summary_response()
    
