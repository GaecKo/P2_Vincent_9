

'''
def send_naissance(start_time, end_time, famille, type_de_graphe):
    """to do!!!
    arguments à rajouter, par exemple la race, ...
    ceux-ci seront directement des choix d'utilisateur sur le site
    retourne au minimum les labels (modalité) et leurs données, par exemple:
    labels = ["octobre 2020", "novembre 2020", ...}
    data = [200, 146, ...]
    chaque index correspond à l'un l'autre, donc labels[0] est lié à data[0]. Il me les faut sous cette forme.
    -> 
    Pour cela, ça doit faire appel à du sql
    """
    return labels, data
'''

import sqlite3
import datetime



"""
À faire, la fonction est un exemple. Il faudrait check ce qu'il nous est demandé comme graphe et le faire avec ceux là.

Il me faut pour chaque fonction au moins les labels (l'axe x du graphe en quelque sorte) et leurs données.


-> Je dois encore faire la partie "prise de date" sur le site, en gros que l'utilisateur puisse saisir la date et que je les envoie ici.
"""


def send_naissance(start_time, end_time):
    """to do!!!
    arguments à rajouter, par exemple la race, ...
    ceux-ci seront directement des choix d'utilisateur sur le site
    retourne au minimum les labels (modalité) et leurs données, par exemple:
    labels = ["octobre 2020", "novembre 2020", ...}
    data = [200, 146, ...]
    chaque index correspond à l'un l'autre, donc labels[0] est lié à data[0]. Il me les faut sous cette forme.
    -> 
    Pour cela, ça doit faire appel à du sql
    """
    #Reformatage des dates récupérées sur le site:
    first_date = datetime.datetime.strptime(start_time, "%Y-%m-%d").strftime("%d/%m/%Y")
    last_date = datetime.datetime.strptime(end_time, "%Y-%m-%d").strftime("%d/%m/%Y")
    
    
    # Accès à la base de données
    conn = sqlite3.connect('database.db')

    # Le curseur permettra l'envoi des commandes SQL
    cursor = conn.cursor()
    
    
    
    
    for row in cursor.execute('''SELECT * FROM velages WHERE date BETWEEN ? AND ? '''(first_date, last_date,)):
        print(row)
       


                        
    
    
    
    
    
    
    
    
    
    return "goodluck"


#send_naissance("2002-10-09","2005-05-05")

