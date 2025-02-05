from flask import Flask, jsonify
from netlify_lambda import handler

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello from Flask on Netlify!")

if __name__ == '__main__':
    app.run()

# Netlify's handler
handler(app)
