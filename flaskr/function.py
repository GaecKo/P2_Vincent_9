import sqlite3 as sql
import datetime

def get_infos(start_time, end_time, famille, graph):
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
    if graph == "moon":
        labels, data = send_moon(start_time, end_time, famille)
        type_graph = "pie"
        return  (labels, data, type_graph)
    
    if graph == "naissance":
        labels, data = send_naissance(start_time, end_time, famille)
        type_graph = "bar"
        return (labels, data, type_graph)
    
    if graph == "races":
        labels, data = send_race(start_time, end_time, famille)
        type_graph = "bar"
        return (labels, data, type_graph)
    return None, None, None

def send_race(start_time, end_time, famille):
    """
    Afficher la distribution des races dans la base de données. On demande en entrée plusieurs races ainsi 
    que le pourcentage minimum de ces dernières et on affiche sur le graphe le nombre d’animaux respectant 
    ces critères par race.

    TO DO!
    """
    return None, None

def send_moon(start_time, end_time, famille):
    """
    Cette fonction doit retourner les labels, data correspondant à:
    Afficher pour une année ou un mois, les animaux nés en période de pleine lune et ceux en nés en dehors. 
    Donner l’option à l’utilisateur d’affiner sa recherche en ajouter un champ famille qui est optionnel.
    """
    labels = ["Pleine Lune", "Autres Lunes"] # les deux labels
    data = [0, 0] # les deux datas
    # au cas où les dates ne seraient pas définies, cela ne pose pas de probème. On reformate les dates
    if start_time != "":
        first_date = datetime.datetime.strptime(start_time, "%Y-%m-%d").strftime("%d/%m/%Y")
    else:
        first_date = None
    if end_time != "":
        last_date = datetime.datetime.strptime(end_time, "%Y-%m-%d").strftime("%d/%m/%Y")
    else:
        last_date = None

    # connexion
    conn = sql.connect('database.db')
    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    for i in cursor.execute("SELECT id, date FROM velages"):
        if not (in_range(i[1], first_date, last_date)): # au cas où la date récupérée ne serait pas dans la range du start et end
            continue
        if is_full_moon(i[1]) : # si c'est un jour de pleine lune
            data[0] += 1
        else:
            data[1] += 1 # si ça ne l'est pas 
    conn.close()
    return labels, data

    

def send_naissance(start_time, end_time, famille):
    """
    Permet de récuperer les naissances dans une période temps
    """
    dict = {}
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
    
    for i in cursor.execute("SELECT id, date FROM velages"):
        if not (in_range(i[1], first_date, last_date)): # si ce n'est pas dans la range du start et end
            continue
        if i[1] not in dict: # ajoute une nouvelle date en cas de naissance à un nouveau jour
            dict[i[1]] = 1
        else: # sinon ajoute une nouvelle naissance à la date
            dict[i[1]] += 1

    for key, value in dict.items(): # pour remettre tout dans la liste labels et data
        labels.append(key) 
        data.append(value)
    conn.close()
    return labels, data


def in_range(date, start, end): # fonction déterminant si une date est entre deux autres
    given_year = int(date.split("/")[2])
    given_month = int(date.split("/")[1])
    given_day = int(date.split("/")[0])
    if start != None:
        start_year = int(start.split("/")[2])
        start_month = int(start.split("/")[1])
        start_day = int(start.split("/")[0])
    if end != None:
        end_year = int(end.split("/")[2])
        end_month = int(end.split("/")[1])
        end_day = int(end.split("/")[0])

    if start !=None:
        if start_year > given_year:
            return False
        if start_year == given_year:
            if start_month > given_month:
                return False
            if start_month == given_month:
                if start_day > given_day:
                    return False
    if end != None:  
        if end_year < given_year:
            return False             
        if end_year == given_year:
            if end_month < given_month:
                return False
            if end_month == given_month:
                if end_day < given_day:
                    return False
    return True

def is_full_moon(date):
    """
    Fonction regardant si un jour est en full moon, True si oui False sinon
    -> Fonction dédicacé à Lucas Marzullo qui m'a aidé à comprendre comment faire. 
    
    """
    year_date, month_date, day_date = int(date.split("/")[2]), int(date.split("/")[1]), int(date.split("/")[0])
    first_moon = datetime.date(1990, 1, 11)
    to_check = datetime.date(year_date, month_date, day_date)
    diff = to_check - first_moon
    print(diff.days % 29.53 < 1)
    return diff.days % 29.53 < 1


