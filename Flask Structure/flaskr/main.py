from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def to_home():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()