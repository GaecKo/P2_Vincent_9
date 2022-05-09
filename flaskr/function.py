import sqlite3 as sql
import datetime
from random import randint
from astral.moon import phase

def get_infos(start_time, end_time, famille, graph, races, pourcentage):
    """
    Cette fonction récupère les infos et les rediriges vers les fonctions qui récupèrent les données.
    :pre: start_time la date de commencement sous forme year-month-day
          end_time la date de fin sous même forme
          famille est la famille à récupérer dans la base de donnée
          graph le graph du genre naissance ou moon, ...
    
    :post: labels: les modalités du graph (axe des x) -> liste
           data: le data associé à chaque modalité -> liste
           type_graph: le type de graph pour ce genre de donnée ('bar', 'pie', 'line')
    """
    if graph == "moon": # si le graph choisi est le moon
        labels, data = send_moon(start_time, end_time, famille) # envoyer les infos à la fonction send_moon avec les paramètres entrés ici
        type_graph = "pie" # le type de graphe est un graphique circulaire
        return  (labels, data, type_graph, None, None)
    
    if graph == "naissance": # si le graphe choisi est naissance 
        labels, data, colors, colors_familly = send_naissance(start_time, end_time, famille) # envoyer les infos à la fonction send_naissance avec les paramètres entrés ici
        type_graph = "bar" # le type de graphe est un diagramme à barres
        return (labels, data, type_graph, colors, colors_familly)
    
    if graph == "races": # si le graphe choisi est races
        labels, data = send_races(races, pourcentage) # envoyer les infos à la fonction send_race avec les paramètres entrés ici
        type_graph = "pie_race" # le type de graphe est un diagramme à barres
        return (labels, data, type_graph, None, None)

    if graph == "repartition":
        labels, data = send_population()
        type_graph = "polarArea"
        return (labels, data, type_graph, None, None)

    return None, None, None, None, None # si aucun de ces 4 choix-là, ne rien return

def send_races(races, pourcentage): 
    """
    Afficher la distribution des races dans la base de données. On demande en entrée plusieurs races ainsi 
    que le pourcentage minimum de ces dernières et on affiche sur le graphe le nombre d’animaux respectant 
    ces critères par race.

    :pre:  races: liste contenant les races choisies ([Holstein, ..., Blanc-bleu-belge) (3 possibilités de races donc liste de taille 3 max)
           pourcentage: Le pourcentage minimum que le vache doit contenir de cette/ces races pour être affichés sur le graphe
        
    :post: labels = modalités (axe des x)
           data = valeurs de ces modalités 

    """
    
    # connexion
    conn = sql.connect('database.db')
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    
    if races[0] == "blanc_bleu_belge":
        type_ = 2
    if races[0] == "holstein":
        type_ = 1
    if races[0] == "jersey":
        type_ = 3

    id_present = []
    type_present = []
    for row in cursor.execute('''SELECT id FROM animaux WHERE presence=1 '''):
        id_present.append(row[0])
        
    for animal in id_present:
        for row in cursor.execute('''SELECT DISTINCT animal_id
                                     FROM animaux_types WHERE animal_id=?
                                     AND type_id=? AND pourcentage>=? ''',(animal,type_,pourcentage)):
            type_present.append(row[0])
            
    if len(races) >1:
        if races[1] == "blanc_bleu_belge":
            type_ = 2
        if races[1] == "holstein":
            type_ = 1
        if races[1] == "jersey":
            type_ = 3


        for animal in type_present:
            for row in cursor.execute('''SELECT DISTINCT animal_id
                                         FROM animaux_types WHERE animal_id=?
                                         AND type_id=? AND pourcentage=? ''',(animal,type_,pourcentage)):
                type_present.append(row[0])
    if len(races) >2:
            
        if races[2] == "blanc_bleu_belge":
            type_ = 2
        if races[2] == "holstein":
            type_ = 1
        if races[2] == "jersey":
            type_ = 3

        

        for animal in type_present:
            for row in cursor.execute('''SELECT DISTINCT animal_id
                                         FROM animaux_types WHERE animal_id=?
                                         AND type_id=? AND pourcentage=? ''',(animal,type_,pourcentage)):
                type_present.append(row[0])
            
            
            
            
            
    type_non_present = []

    for row in cursor.execute('''SELECT DISTINCT animal_id FROM animaux_types'''):
        type_non_present.append(row)
        
        
    nombre_present_total = len(type_non_present) - len(type_present)

    data = [0,0]   
    data[0],data[1] = len(type_present), nombre_present_total        
             

    labels = ["Respectent les conditions", "Ne respectant pas les conditions"]
        
    conn.close()

    return labels, data, None, None


def send_moon(start_time, end_time, famille):
    """
    Cette fonction doit retourner les labels, data correspondant à:
    Afficher pour une année ou un mois, les animaux nés en période de pleine lune et ceux en nés en dehors. 
    Donner l’option à l’utilisateur d’affiner sa recherche en ajouter un champ famille qui est optionnel.
    :pre: start_time est la période de début
          end_time est la période de fin
          famille est la famille de vaches qu'il faut regarder = liste

    :post: labels : les modalités du graph (axe des x) -> liste
           datas : le data associé à chaque modalité -> liste
    """
    labels = ["Pleine Lune", "Autres Lunes"] # les deux labels
    data = [0, 0] # les deux datas

    # au cas où les dates ne seraient pas définies, cela ne pose pas de probème. On vérifie tout ça ici
    if start_time == "":
        start_time = "1990-01-01"
    if end_time == "":
        end_time = "2020-12-31"

    # connexion
    conn = sql.connect('database.db')
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    id_date = []
    for i in cursor.execute('''SELECT id, date FROM velages WHERE date BETWEEN ? AND ? ''', (start_time, end_time)):
        id_date.append(i)

    animal_id = []
    for i in range(len(id_date)):
        for a in cursor.execute(f'''SELECT animal_id, velage_id FROM animaux_velages WHERE (velage_id = {id_date[i][0]} )'''):
            if i != 0:
                if animal_id[-1][1] != a[1]:
                    animal_id.append(a)
            else:
                animal_id.append(a)
    
    for a in range(len(animal_id)):
        for f in cursor.execute(f'''SELECT famille_id, id FROM animaux WHERE (id = {animal_id[a][0]} )'''):
            if famille == [] or str(f[0]) in famille:
                if is_full_moon(id_date[a][1]) : # si c'est un jour de pleine lune
                    data[0] += 1
                else:
                    data[1] += 1 # si ça ne l'est pas 
        
    conn.close()
    return labels, data

def send_naissance(start_time, end_time, famille):
    """
    Fonction permettant de récuperer les naissances dans une période temps
    :pre:  start_time est la période de début 
           end_time est la période de fin
           famille est la famille de vaches qu'il faut regarder
    
    :post: labels : les modalités du graph (axe des x) -> liste
           datas : le data associé à chaque modalité -> liste
    """
    dict = {} #On créée un dictionnaire vide, ainsi qu'une liste labels et data vide 
    labels = []
    data = []

    # au cas où les dates ne seraient pas définies, cela ne pose pas de probème. On vérifie tout ça ici
    if start_time == "":
        start_time = "1990-01-01"
    if end_time == "":
        end_time = "2020-12-31"
    # Accès à la base de données
    conn = sql.connect('database.db')

    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    

    # code à utiliser pour quand les familles auront un intêret 
    color_familly = [color_gen() for _ in range(len(famille))]
    colors = []

    id_date = []
    for i in cursor.execute('''SELECT id, date FROM velages WHERE date BETWEEN ? AND ? ''', (start_time, end_time)):
        id_date.append(i)

    animal_id = []
    for i in range(len(id_date)):
        for a in cursor.execute(f'''SELECT animal_id, velage_id FROM animaux_velages WHERE (velage_id = {id_date[i][0]} )'''):
            if i != 0:
                if animal_id[-1][1] != a[1]:
                    animal_id.append(a)
            else:
                animal_id.append(a)
    
    for a in range(len(animal_id)):
        for f in cursor.execute(f'''SELECT famille_id, id FROM animaux WHERE (id = {animal_id[a][0]} )'''):
            if famille == [] or str(f[0]) in famille:
                if id_date[a][1] not in dict: # ajoute une nouvelle date en cas de naissance à un nouveau jour
                    dict[id_date[a][1]] = [[f[1]]]
    
                else: # sinon ajoute une nouvelle naissance à la date
                    dict[id_date[a][1]].append([f[1]])
                if famille != []:    
                    index = famille.index(str(f[0]))
                    colors.append(color_familly[index])

    for key, value in dict.items(): # pour remettre tout dans la liste labels et data
        labels.append(key) 
        data.append(len(value))
    conn.close()

    return labels, data, colors, color_familly

def send_population():
    """
    Fonction permettant de retourner les labels, data correspondant à:
    la population totale de la ferme
    :pre:  None
    :post: Retourne labels étant Males / femelle
                    data étant le nombre total d'animaux chaque sexe
    """
    labels = ["Femelles","Mâles"] #Les 2 labels
    data = [0, 0] #La data va être une liste composée des valeurs pour chaque sexe
    # Accès à la base de données
    conn = sql.connect('database.db')
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()

    for i in cursor.execute("SELECT sexe FROM animaux"): #On parcourt tout les éléments sexe de la table animaux
        if i[0] == "M": #Si i vaut une lettre M, cela veut dire que l'élément itéré est un mâle
            data[1] += 1
        elif i[0] == "F": #Si i vaut une lettre F, cela veut dire que l'élément itéré est une femelle
            data[0] += 1
    conn.close()

    return labels, data

def is_full_moon(date):
    """
    :pre: date sous forme "jour/mois/année"
    :post: retourne True si à cette date c'était une pleine Lune, False sinon
    """
    year_date, month_date, day_date = int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[2])
    date = datetime.date(year_date, month_date, day_date)
    moon = phase(date)
    if moon >= 14 and moon < 21:
        return True
    return False

def color_gen():
    return f"rgba({randint(1, 250)}, {randint(1, 250)}, {randint(1, 250)}, 1)"
