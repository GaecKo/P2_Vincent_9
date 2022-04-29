from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def to_home():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/analytics")
def analytics():
    return render_template('analytics.html')


# def set_graph(type_chart, color, main_label):
#     return (type_chart ,color, main_label, labels, data)


if __name__ == "__main__":
    app.run(debug=True)