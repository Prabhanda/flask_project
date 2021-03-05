# importing flask module fro
from flask import Flask, render_template

# initializing a variable of Flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
