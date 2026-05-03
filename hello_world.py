#!/usr/bin/env python3
"""
Hello World sample script with Flask
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Simple hello world route"""
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
