# coding: utf-8
# untitled - runner.py
# 2022-01-07  10:52

import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    with open("1.json", "w") as f:
        json.dump(request.json, f)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
