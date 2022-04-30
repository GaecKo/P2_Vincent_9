from flask import Flask, redirect, url_for, render_template, request

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
    # appel de la fonction avec la db
    # récupération des données 
    nom = f"{start_time} | {end_time} | {famille}"
    graph = 'line' #"le type de graphe en fonction des choix données"
    labeles = ["a", "b", "c"] #"donnés par la fonction"
    datas = [10, 20, 30] #"donnés par la fonction"
    if request.method == "POST":
        return render_template('graph.html', type=graph, main_label = nom, labels=str(labeles), data=datas)

@app.route("/analytics", methods=['GET', 'POST'])
def analytics():
    return render_template('analytics.html')


if __name__ == "__main__":
    app.run(debug=True)