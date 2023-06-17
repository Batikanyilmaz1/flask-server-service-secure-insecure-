from flask import Flask, render_template, request
import requests

app = Flask(__name__)

SERVICE_URL = "http://localhost:80"
SECURE_SERVICE_URL = "https://localhost:443"

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/fibonacci/')
def fibonacci():
    num = request.args.get('num')
    response = requests.get(f"{SERVICE_URL}/fibonacci/{num}")
    return response.text

@app.route('/reverse/')
def reverse_string():
    string = request.args.get('str')
    response = requests.get(f"{SERVICE_URL}/reverse/{string}")
    return response.text

@app.route('/secure/fibonacci/')
def secure_fibonacci():
    num = request.args.get('num')
    response = requests.get(f"{SECURE_SERVICE_URL}/fibonacci/{num}", verify=False)
    return response.text

@app.route('/secure/reverse/')
def secure_reverse_string():
    string = request.args.get('str')
    response = requests.get(f"{SECURE_SERVICE_URL}/reverse/{string}", verify=False)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=900)
    app.run(port=901, ssl_context='adhoc')
