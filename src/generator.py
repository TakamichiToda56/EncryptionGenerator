from flask import Flask, request

app = Flask(__name__)

@app.route('/encryption/<word>')
def encryption(word):
    return word

@app.route('/decoding/<word>')
def decoding(word):
    return word

if __name__ == '__main__':
    app.run()
