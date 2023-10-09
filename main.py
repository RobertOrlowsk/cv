from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index_1.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
