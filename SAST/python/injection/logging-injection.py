import logging
from flask import Flask, request

app = Flask(__name__)

@app.route('/example')
def log():
    data = request.args.get("data", "")
    app.logger.critical("%r", data)

if __name__ == '__main__':
    app.run()