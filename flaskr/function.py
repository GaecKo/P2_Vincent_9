import sqlite3 as sql
import datetime
from random import randint
from astral.moon import phase

def color_gen():
    return f"({randint(1, 250)}, {randint(1, 250)}, {randint(1, 250)}, 1)"

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
        return  (labels, data, type_graph, None)
    
    if graph == "naissance": # si le graphe choisi est naissance 
        labels, data, colors = send_naissance(start_time, end_time, famille) # envoyer les infos à la fonction send_naissance avec les paramètres entrés ici
        type_graph = "bar" # le type de graphe est un diagramme à barres
        return (labels, data, type_graph, colors)
    
    if graph == "races": # si le graphe choisi est races
        labels, data = send_race(start_time, end_time, races, pourcentage) # envoyer les infos à la fonction send_race avec les paramètres entrés ici
        type_graph = "bar" # le type de graphe est un diagramme à barres
        return (labels, data, type_graph, None)

    if graph == "repartition":
        labels, data = send_population()
        type_graph = "polarArea"
        return (labels, data, type_graph, None)

    return None, None, None # si aucun de ces 4 choix-là, ne rien return

def send_race(start_time, end_time, races, pourcentage):
    """
    Afficher la distribution des races dans la base de données. On demande en entrée plusieurs races ainsi 
    que le pourcentage minimum de ces dernières et on affiche sur le graphe le nombre d’animaux respectant 
    ces critères par race.
    :pre: start-time sous forme day-month-year

    :post:

    TO DO!
    """
    return None, None

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
    # au cas où les dates ne seraient pas définies, cela ne pose pas de probème. On reformate les dates
    if start_time != "": #Si la date de départ n'est pas vide
        first_date = datetime.datetime.strptime(start_time, "%Y-%m-%d").strftime("%d/%m/%Y")
    else:
        first_date = None
    if end_time != "": #Si la date de fin n'est pas vide
        last_date = datetime.datetime.strptime(end_time, "%Y-%m-%d").strftime("%d/%m/%Y")
    else:
        last_date = None

    # connexion
    conn = sql.connect('database.db')
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    for i in cursor.execute('''SELECT
                                    id, date
                                FROM
                                    velages
                                WHERE
                                    date BETWEEN ? AND ? ''',(first_date, last_date)):
        # if famille != [] and i[0] not in famille:
        #     continue
        if is_full_moon(i[1]) : # si c'est un jour de pleine lune
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

    #Reformatage des dates récupérées sur le site:
    if start_time != "":
        first_date = datetime.datetime.strptime(start_time, "%Y-%m-%d").strftime("%d/%m/%Y")
    else:
        first_date = None
    if end_time != "":
        last_date = datetime.datetime.strptime(end_time, "%Y-%m-%d").strftime("%d/%m/%Y")
    else:
        last_date = None
    # Accès à la base de données
    conn = sql.connect('database.db')

    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    


    color_familly = [color_gen() for _ in range(len(famille))]
    colors = []


    for i in cursor.execute('''SELECT
                                    id, date
                                FROM
                                    velages
                                WHERE
                                    date BETWEEN ? AND ? ''',(first_date, last_date)):

        # colors.append(color_familly[color_familly.index(i[0])])
        if i[1] not in dict: # ajoute une nouvelle date en cas de naissance à un nouveau jour
            dict[i[1]] = 1
        else: # sinon ajoute une nouvelle naissance à la date
            dict[i[1]] += 1

    for key, value in dict.items(): # pour remettre tout dans la liste labels et data
        labels.append(key) 
        data.append(value)
    conn.close()
    return labels, data, colors

def is_full_moon(date):
    """
    :pre: date sous forme "jour/mois/année"
    :post: retourne True si à cette date c'était une pleine Lune, False sinon
    """
    year_date, month_date, day_date = int(date.split("/")[2]), int(date.split("/")[1]), int(date.split("/")[0])
    date = datetime.date(year_date, month_date, day_date)
    moon = phase(date)
    if moon >= 14 and moon < 21:
        return True
    return False

def send_population():
    """
    Fonction permettant de retourner les labels, data correspondant à:
    la population totale de la ferme
    :pre:  start_time est la période de début 
           end_time est la période de fin
           famille est la famille de vaches qu'il faut regarder 
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