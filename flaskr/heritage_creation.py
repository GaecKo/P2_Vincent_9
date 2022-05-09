#Programme pour ajouter l'héritage génétique de chaque vache dans la table animaux types



import sqlite3
import datetime

# Accès à la base de données

conn = sqlite3.connect('database.db')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()


def type_id(id_animal):
    try:
        for row in cursor.execute('''SELECT type_id FROM animaux_types WHERE animal_id=?''',(id_animal,)):
            type_idd = row[0]
        return type_idd
    except:
        return -1

def pourcentage(id_animal):
    try:
        for row in cursor.execute('''SELECT pourcentage FROM animaux_types WHERE animal_id=?''',(id_animal,)):
            pourcentage = row[0]
        return pourcentage
    except:
        return -1

#Holestein, Blanc bleu belge, Jersey  (0,0,0)
count = 0
id_animaux = []
id_animaux_types = []

for row in cursor.execute('''SELECT id FROM animaux'''):
    id_animaux.append(row[0])


for row in cursor.execute('''SELECT animal_id FROM animaux_types'''):
    id_animaux_types.append(row[0])
    
for enfant in id_animaux:
    mere_id = []
    pere_id = []
    if enfant not in id_animaux_types:
        for row in cursor.execute('''SELECT velage_id FROM animaux_velages WHERE animal_id=?''',(enfant,)):
            velage_enfant = row[0]
        for row in cursor.execute('''SELECT mere_id FROM velages WHERE id=?''',(velage_enfant,)):
            mere_id.append(row[0])
        for row in cursor.execute('''SELECT pere_id FROM velages WHERE id=?''',(velage_enfant,)):
            pere_id.append(row[0])
        for ids in mere_id:
            mere_race = type_id(ids)
            mere_pourcentage = pourcentage(ids)
            if (mere_race or mere_pourcentage) == -1:
                print('-1 still left')
            if (mere_race or mere_pourcentage) != -1:
                cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,mere_race, mere_pourcentage/2))
        for ids in pere_id:
            pere_race = type_id(ids)
            pere_pourcentage = pourcentage(ids)
            if (mere_race or mere_pourcentage) == -1:
                print('-1 still left')
            if (pere_race or pere_pourcentage) != -1:
                cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,pere_race, pere_pourcentage/2))

            
#conn.commit()


conn.close()

