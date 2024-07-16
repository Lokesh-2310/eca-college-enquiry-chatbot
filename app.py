from flask import Flask, render_template, request, jsonify,redirect,url_for, session
from model import cleantext
app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/submit-data', methods=['POST'])
def submit_data():
    data = request.get_json()
    userInput = data['userInput']
    text=cleantext(userInput)
    session['processed_text'] = text
    return redirect(url_for("get_message"))

@app.route('/get-message', methods=['GET'])
def get_message():
    text= session.get('processed_text', 'No message found')
    return jsonify({'message': text})

if __name__ == '__main__':
    app.run(debug=True)
