from flask import Flask, jsonify


app = Flask(__name__)


@app.before_request
def before_request():
    print("Before request")


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/name/<string:name>/')
def hello_name(name):
    return 'Hello {}!'.format(name)


@app.route('/<int:num>/')
def incrementer(num):
    return "Incremented number is {}".format(num + 1)


@app.route('/person/')
def person():
    return jsonify({'name': 'John', 'age': 30})


@app.route('/numbers/')
def numbers():
    return jsonify(list(range(10)))


@app.route('/home/')
def home():
    return "Home Page"


@app.route('/contact/')
def contact():
    return "Contact Page"


@app.route('/teapot/')
def teapot():
    return "Would you like some tea?", 418


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
