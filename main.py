from urllib import request
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/single_reviewer_summary', methods=['GET', 'POST'])
def single_summary():
    if request.method == 'POST':
        title = request.json['title']
        content = request.json['content']
        return get_single_summary()
    else:
        return "empty result"
    
@app.route('/all_reviewers_summary', methods=['GET', 'POST'])
def all_summary():
    if request.method == 'POST':
        return get_all_summary()
    else:
        return "empty result"
    
@app.route('/disagreement_summary', methods=['GET', 'POST'])
def disagreement_summary():
    if request.method == 'POST':
        return get_disagreement_summary()
    else:
        return "empty result"
    
@app.route('/review_comments', methods=['GET', 'POST'])
def review_comments():
    if request.method == 'POST':
        return get_review_comments()
    else:
        return "empty result"
