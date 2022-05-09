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
    info_data = {} # dico à utiliser et que sera donné dans le html
    start_time = request.form["start"] # récup des dates (start et end)
    end_time = request.form["end"]
    graphe_to_show = request.form["graphe"] # type de graphe 
    

# paramêtres facultatifs
    try:
        famille = request.form.getlist("familles") # récupération des familles
        info_data["famille_id"] = famille
        
    except:
        famille = []
    try:
        races = request.form.getlist("races")
        info_data["races"] = races
        pourcentage = request.form["percentage"]
        info_data["pourcentage"] = pourcentage 
    except:
        races = []

# autres informations / créations d'informations depuis SQL
    info_data["main_label"] = graphe_to_show
    info_data["famille_name"] = id_famille_to_name(famille)
    info_data["labels"], info_data["data"], info_data["graph"], info_data["background"], info_data["color_familly"] = get_infos(start_time, end_time, famille, graphe_to_show, races, pourcentage) # envoit des infos vers une fonction annexe qui s'en charge

    if info_data["background"] in [[], "", None]:
        info_data["background"] = "'rgba(175, 208, 214, 1)'"

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
    
def id_famille_to_name(list_famille):
    return [famillies[int(i)] for i in list_famille]

global famillies
famillies = {134: 'Margueritte', 45: 'Jonquille', 157: 'Lila', 99: 'Paquerette', 65: 'Agapanthe', 149: 'Bleuet', 61: 'Ciboulette', 141: 'Iris', 161: 'Lavande', 117: 'Lotus', 164: 'Hélène', 123: 'Milka', 16: "Côte d'Or", 77: 'Lindt', 139: 'Toblerone', 1: 'Galak', 92: 'KitKat', 116: 'Kinder', 30: 'Narcisse', 120: 'Orchidée', 47: 'Pissenlit', 96: 'Tournesol', 4: 'Vincent', 79: 'Trompette', 29: 'Minnie', 140: 'Rosette', 85: 'Blondie', 104: 'Caprice', 82: 'Betty', 97: 'Noisette', 10: 'Margot', 2: 'Réglisse', 15: 'Ruby', 126: 'Rustique', 144: 'Raymonde', 152: 'Sky', 110: 'Snow', 146: 'Sauterelle', 111: 'Star', 147: 'Sidonie', 50: 'Saturne', 17: 'Sorbet', 115: 'Sonette', 94: 'Summer', 63: 'Plume', 35: 'Peluche', 84: 'Pamela', 5: 'Panade', 69: 'Perle', 136: 'Papaye', 26: 'Renaud', 39: 'Papyrus', 22: 'Potache', 74: 'Pomme', 25: 'Pascaline', 48: 'Pink', 67: 'Provence', 148: 'Prune', 33: 'Paula', 18: 'Paupiette', 83: 'Pupuce', 21: 'Oasis', 80: 'Ocarina', 12: 'Orange', 91: 'Orage', 32: 'Origami', 20: 'Odile', 108: 'Ollande', 13: 'Olympe', 81: 'Oméga', 145: 'Otaria', 121: 'Okaly', 38: 'Onyx', 73: 'Olive', 106: 'Origan', 54: 'Ovalie', 75: 'Ophélie', 98: 'Ophia', 102: 'Ninette', 28: 'Ayham', 88: 'Ninon', 162: 'Naya', 138: 'Naza', 118: 'Nadine', 66: 'Nitendo', 154: 'Neda', 150: 'Noire', 129: 'Blanche', 142: 'Nairobi', 90: 'Nolvenn', 124: 'Nela', 70: 'Nora', 127: 'Fraise', 100: 'Banane', 72: 'Poire', 46: 'Citron', 119: 'Benoît', 128: 'Normande', 76: 'Norma', 135: 'Neptune', 27: 'Neslie', 40: 'Nancy', 8: 'Nostalgie', 156: 'Nouille', 109: 'Naomi', 11: 'Nourrice', 19: 'Nounou', 95: 'Nice', 9: 'Nubia', 23: 'Nash', 112: 'Numerobis', 114: 'Nuggets', 42: 'Nassma', 87: 'Nya', 163: 'Nilla', 159: 'Nathalia', 158: 'Nina', 36: 'Nima', 6: 'Rubarbe', 31: 'Maserati', 78: 'Mercedes', 43: 'Ferraris', 14: 'Ford', 86: 'Citroenne', 155: 'Jeep', 151: 'Magma', 137: 'Maite', 51: 'Madi', 62: 'Motorola', 24: 'Mirabelle', 59: 'Mazda', 153: 'Fiesta', 122: 'Malaisie', 34: 'Mamamia', 49: 'Météorite', 130: 'Moutarde', 113: 'Mosaic', 132: 'Moselle', 133: 'Mandala', 53: 'Meringue', 58: 'Micheline', 101: 'Midas', 107: 'Mimosa', 3: 'Myrtille', 103: 'Mystic', 41: 'Mushroom', 93: 'Moussaka', 52: 'Moon', 60: 'Mastar', 68: 'Céline', 143: 'Mina', 131: 'Macaroni', 44: 'Madona', 56: 'Majestic', 57: 'Bessie', 37: 'Clarabelle', 125: 'Penny', 105: 'Dottie', 160: 'Tonnerre', 55: 'Oreo', 64: 'Panda', 7: 'Bimbo', 71: 'Moka', 89: 'Mélasse', 500: 'Unknown'}
if __name__ == "__main__":
    app.run(debug=True)
