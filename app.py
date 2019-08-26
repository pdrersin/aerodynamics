
from flask import Flask, render_template, session

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("aeroplots.html")


if __name__=='__main__':
    app.run(debug=True)
