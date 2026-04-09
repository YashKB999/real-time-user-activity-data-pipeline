from flask import Flask, request, render_template

app = Flask(__name__, template_folder='../frontend')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/log', methods=['POST'])
def log():

    event = request.json

    print("EVENT RECEIVED:", event)

    return {"status":"received"}

app.run(debug=True)