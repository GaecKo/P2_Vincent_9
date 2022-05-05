from flask import Flask, redirect, url_for, render_template, request
from function import *

app = Flask(__name__)

@app.route("/")
def to_home():
    return redirect(url_for("home")) # redirection vers la page d'acceuil automatique 

@app.route("/home")
def home():
    return render_template('home.html') # page d'acceuil

@app.route("/graph", methods=['POST'])
def graph():
    start_time = request.form["start"]
    end_time = request.form["end"]
    try:
        famille = request.form.getlist("familles") # récupération des informations
    except:
        famille = []
    try:
        races = request.form.getlist("races")
        pourcentage = request.form["percentage"]
    except:
        races = []
    
    graphe_to_show = request.form["graphe"]
    labels, data, graph, background = get_infos(start_time, end_time, famille, graphe_to_show, races, pourcentage) # envoit des infos vers des fonctions annexes qui s'en chargent
    somme = sum(data)
    maximum = max(data) # quelques stats des données récupérées pour afficher dans les paragraphes
    if request.method == "POST":
        return render_template('graph.html', type=graph, main_label=graphe_to_show, labels=labels, data=data, somme=somme, max=maximum, background=background) # page de graphe


@app.route("/analytics", methods=['GET', 'POST']) # page de form pour récupérer les infos
def analytics():
    return render_template('analytics.html')


if __name__ == "__main__":
    app.run(debug=True)
