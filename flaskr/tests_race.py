import sqlite3
import datetime

# Accès à la base de données

conn = sqlite3.connect('database.db')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

#Holestein, Blanc bleu belge, Jersey


for row in cursor.execute('''
                            SELECT
                                *
                            FROM
                                animaux_types
                            
                            '''):
    print(row)




'''
for row in cursor.execute(SELECT
                                animaux.id
                            FROM
                                animaux
                            INNER JOIN
                                animaux_types
                            ON
                                animaux_types.type_id = animaux_types.animal_id ):
'''    




















conn.close()






