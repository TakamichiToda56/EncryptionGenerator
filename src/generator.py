from flask import Flask, request
from func import *

app = Flask(__name__)

@app.route('/encryption/<word>')
def encryption(word):
    return word

@app.route('/decoding/<word>')
def decoding(word):
    return word

if __name__ == '__main__':
    app.run()
