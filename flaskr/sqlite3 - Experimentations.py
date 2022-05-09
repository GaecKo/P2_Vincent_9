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
start_time = '1980-04-10'
end_time = '2020-04-11'
leng = []

#Change le format de la date de YYY-MM-DD vers DD/MM/YYYY pour être compatible avec la base de donnée.
#first_date = datetime.datetime.strptime(start_time, "%Y-%m-%d").strftime("%d/%m/%Y")
#last_date = datetime.datetime.strptime(end_time, "%Y-%m-%d").strftime("%d/%m/%Y")



races = ["jersey","holstein"]
pourcentage = 100



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
        


print(data)







# Toujours fermer la connexion quand elle n'est plus utile
conn.close()


