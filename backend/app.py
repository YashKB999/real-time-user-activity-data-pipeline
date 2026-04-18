from flask import Flask, request, render_template
from producer import send_event


# Sending activity to kafka

app = Flask(__name__, template_folder='../frontend')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/log', methods=['POST'])
def log():

    event = request.json

    # print("EVENT RECEIVED:", event)

    send_event(event)
    print("EVENT SENT TO KAFKA:", event)

    return {"status":"received"}

app.run(debug=True)