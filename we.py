from flask import Flask

tt = Flask(__name__)

@tt.route('/')
def index():
    return'hello'

tt.run(host='0.0.0.0', port=229)