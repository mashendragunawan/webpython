from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Akhirnya Aku Bisa Juga MENAMPILKAN WEB dengan python'

app.run(host='0.0.0.0', port=229)