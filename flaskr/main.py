from crypt import methods
from email.policy import default
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
    info_data = {}
    start_time = request.form["start"] # récup des dates (start et end)
    end_time = request.form["end"]
    graphe_to_show = request.form["graphe"]
    info_data["main_label"] = graphe_to_show

# paramêtres facultatifs
    try:
        famille = request.form.getlist("familles") # récupération des familles
    except:
        famille = []
    try:
        races = request.form.getlist("races")
        pourcentage = request.form["percentage"]
    except:
        races = []

# autres informations / créations d'informations depuis SQL

    info_data["labels"], info_data["data"], info_data["graph"], info_data["background"] = get_infos(start_time, end_time, famille, graphe_to_show, races, pourcentage) # envoit des infos vers une fonction annexe qui s'en charge

    if info_data["background"] in [[], "", None]:
        info_data["background"] = "'rgba(0, 240, 0, 1)'"

    if len(info_data["data"]) > 0 :
        info_data["somme"] = sum(info_data["data"])
        info_data["maximum"] = max(info_data["data"]) # quelques stats des données récupérées pour afficher dans les paragraphes
        if start_time != "":
            info_data["start_time"] = start_time.split("-")[2] + "/" + start_time.split("-")[1] + "/" + start_time.split("-")[0]
        else:
            info_data["start_time"] = "01/01/1990"
        if end_time != "":
            info_data["end_time"] = end_time.split("-")[2] + "/" + end_time.split("-")[1] + "/" + end_time.split("-")[0]
        else:
            info_data["end_time"] = "31/12/2020"

    if len(info_data["data"]) == 0 or (info_data["data"][0] == 0 and info_data["data"][1] == 0):
        return render_template('analytics.html', no_graph=True)

    if request.method == "POST":
        return render_template('graph.html', info_data=info_data) # page du graphe avec un dictionnaire ayant toutes les infos.


@app.route("/analytics", methods=['GET', 'POST']) # page de form pour récupérer les infos
def analytics():
    return render_template('analytics.html', no_graph=False)
    
    


if __name__ == "__main__":
    app.run(debug=True)
