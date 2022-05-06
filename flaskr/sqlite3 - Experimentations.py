import sqlite3
import datetime

# Accès à la base de données

conn = sqlite3.connect('database.db')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

# utilisation de la base de données
ok = ""
# Si on a fait des modifications à la base de données ATTENTION

# Toujours fermer la connexion quand elle n'est plus utile
start_time = '1996-04-10'
end_time = '1997-04-11'


#Change le format de la date de YYY-MM-DD vers DD/MM/YYYY pour être compatible avec la base de donnée.
#first_date = datetime.datetime.strptime(start_time, "%Y-%m-%d").strftime("%d/%m/%Y")
#last_date = datetime.datetime.strptime(end_time, "%Y-%m-%d").strftime("%d/%m/%Y")

#Query pour chercher les datas (Remplacer le * par les datas à extraire) entre 2 dates. 
for f in cursor.execute('''SELECT
                                    *
                                FROM
                                    velages
                                WHERE
                                    date BETWEEN ? AND ? ''',(start_time, end_time)):

    print(f)
 
 
 
''' 
first_date = '01/01/2020'
last_date = '31/12/2020'
leng  = []
for i in cursor.execute(SELECT
                                    id, date
                                FROM
                                    velages
                                WHERE
                                    date BETWEEN ? AND ? ,(first_date, last_date)):
    print(i[1])
    leng.append(i)
    
print(len(i))
'''












"""
for i in range(1000):
    
    cursor.execute('''INSERT INTO CLASSE (MATRICULE, NOM, PRENOM, AGE, POINTS)
                  VALUES (1, 'Durant', 'Emilie', '8', 73.5)''')

"""
#conn.commit()
'''
lenght = []
for row in cursor.execute(SELECT
                                animaux.id
                            FROM
                                animaux
                            INNER JOIN
                                animaux_types
                            ON
                                animaux_types.type_id = animaux_types.animal_id ):
    
    print(row)
    lenght.append(row)
print(len(lenght))

'''   

# Toujours fermer la connexion quand elle n'est plus utile
conn.close()


'''


prendre id papa, id maman, from id of parents, take race of each parents,
take 50% of each parent race for the child

take all child 

for row in cursor.execute("SELECT  id from animaux "):
    
    print(row)
    lenght.append(row)
print(len(lenght))




'''
