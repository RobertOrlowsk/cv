import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index_1.html')


if __name__ == '__main__':
    app.run(debug=False)
