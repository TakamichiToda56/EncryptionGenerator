from flask import Flask, request, render_template
from func import *

app = Flask(__name__)

key_num = 4

@app.route('/')
def index():
    return "About: https://github.com/TakamichiToda56/EncryptionGenerator"

@app.route('/encryption/<word>')
def encryption(word):
    binary_list = ascii2binary(word)
    cipher_list = encryption_list(binary_list,key_num)
    cipher = bind_cipher(cipher_list)
    return cipher

@app.route('/decoding/<cipher>')
def decoding(cipher):
    cipher_list = split_cipher(cipher)
    binary_list = decode_list(cipher_list,key_num)
    word = binary2ascii(binary_list)
    return word

if __name__ == '__main__':
    #app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
