from flask import Flask

app_http = Flask(__name__)
app_https = Flask(__name__)

@app_http.route('/')
def index_http():
    return "HTTP Service is running."

@app_https.route('/')
def index_https():
    return "HTTPS Service is running."

# Routes for the HTTP server
@app_http.route('/fibonacci/<int:num>', methods=['GET'])
def fibonacci_http(num):
    if num <= 0:
        return "Invalid input"
    elif num == 1:
        return "0"
    elif num == 2:
        return "0 1"
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < num:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return ' '.join(map(str, fib_seq))

@app_http.route('/reverse/<string:string>', methods=['GET'])
def reverse_string_http(string):
    return string[::-1]

# Routes for the HTTPS server
@app_https.route('/fibonacci/<int:num>', methods=['GET'])
def fibonacci_https(num):
    if num <= 0:
        return "Invalid input"
    elif num == 1:
        return "0"
    elif num == 2:
        return "0 1"
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < num:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return ' '.join(map(str, fib_seq))

@app_https.route('/reverse/<string:string>', methods=['GET'])
def reverse_string_https(string):
    return string[::-1]

if __name__ == '__main__':
    app_http.run(host='0.0.0.0', port=80)
    app_https.run(host='0.0.0.0', port=443, ssl_context='adhoc')
