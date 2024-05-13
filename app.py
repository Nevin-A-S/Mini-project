from flask import Flask, render_template, request, jsonify
from scraper import scraper
from summarizer import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    message = request.json['message']
    # Call your chat bot function to get the response
    response = "This is a sample response for the message: " + message
    return jsonify({'response': response})

@app.route('/get_summary', methods=['POST'])
def get_summary():
    url = request.json['url']
    # Call your scraper and summarizer functions
    text = scraper(url)
    summary = summarizer(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)