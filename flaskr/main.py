from flask import Flask, redirect, url_for, render_template, request
from function import *

app = Flask(__name__)

@app.route("/")
def to_home():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/graph", methods=['POST'])
def graph():
    start_time = request.form["start"]
    end_time = request.form["end"]
    famille = request.form["familles"]
    graphe_to_show = request.form["graphe"]
    labels, data, graph = get_infos(start_time, end_time, famille, graphe_to_show)
    if request.method == "POST":
        return render_template('graph.html', type=graph, main_label = graphe_to_show, labels=labels, data=data)

@app.route("/analytics", methods=['GET', 'POST'])
def analytics():
    return render_template('analytics.html')


if __name__ == "__main__":
    app.run(debug=True)
