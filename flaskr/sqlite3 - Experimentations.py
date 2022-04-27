
import sqlite3

# Accès à la base de données

conn = sqlite3.connect('database.db')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

# utilisation de la base de données

# Si on a fait des modifications à la base de données ATTENTION

# Toujours fermer la connexion quand elle n'est plus utile
"""
for i in range(1000):
    
    cursor.execute('''INSERT INTO CLASSE (MATRICULE, NOM, PRENOM, AGE, POINTS)
                  VALUES (1, 'Durant', 'Emilie', '8', 73.5)''')

"""
#conn.commit()
lenght = []
for row in cursor.execute('''SELECT
                                animaux.id
                            FROM
                                animaux
                            INNER JOIN
                                animaux_types
                            ON
                                animaux_types.type_id = animaux_types.animal_id '''):
    
    print(row)
    lenght.append(row)
print(len(lenght))

   

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
