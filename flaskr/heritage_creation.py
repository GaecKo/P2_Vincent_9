#Programme pour ajouter l'héritage génétique de chaque vache dans la table animaux types

#Ce code n'est pas la meilleure solution en terme d'efficacité de concision, nous en avons conscience. 



import sqlite3
import datetime

light = 0
counter = 0

# Accès à la base de données

conn = sqlite3.connect('database.db')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

leng = []
for row in cursor.execute("SELECT * FROM animaux_types"):
    #print(row)
    leng.append(row)
    
print(len(leng))

#Fonction qui retourne le type de l'animal quand on l'appelle avec un id d'animal présent dans la table animaux_types
#Pre: un id d'animal présent dans la base animaux_types
#Post: le pourcentage de cet animal 
def type_id(id_animal):
    try:
        for row in cursor.execute('''SELECT type_id FROM animaux_types WHERE animal_id=?''',(id_animal,)):
            type_idd = row[0]
        return type_idd
    except:
        return -1


#Fonction qui retourne le pourcentage de l'animal quand on l'appelle avec un id d'animal présent dans la table animaux_types
#Pre: un id d'animal présent dans la base animaux_types
#Post: le pourcentage de cet animal 
def pourcentage(id_animal):
    try:
        for row in cursor.execute('''SELECT pourcentage FROM animaux_types WHERE animal_id=?''',(id_animal,)):
            pourcentage = row[0]
        return pourcentage
    except:
        return -1

id_animaux = []
id_animaux_types = []


for row in cursor.execute('''SELECT id FROM animaux'''):
    id_animaux.append(row[0])


for row in cursor.execute('''SELECT animal_id FROM animaux_types'''):
    id_animaux_types.append(row[0])
    
for enfant in id_animaux:
    mere_id = []
    pere_id = []
    p = []
    r = []
    
    #Fonction pour trouver quel animal n'est pas encore encodé dans le tableau animaux_types. Et trouve ses parents
    if enfant not in id_animaux_types:
        for row in cursor.execute('''SELECT velage_id FROM animaux_velages WHERE animal_id=?''',(enfant,)):
            velage_enfant = row[0]
            for row in cursor.execute('''SELECT mere_id FROM velages WHERE id=?''',(velage_enfant,)):
                mere_idd = row[0]
            for row in cursor.execute('''SELECT pere_id FROM velages WHERE id=?''',(velage_enfant,)):
                pere_idd = row[0]
            for row in cursor.execute('''SELECT animal_id FROM animaux_types WHERE animal_id=?''',(mere_idd,)):
                mere_id.append(row[0])
            for row in cursor.execute('''SELECT animal_id FROM animaux_types WHERE animal_id=?''',(pere_idd,)):
                pere_id.append(row[0])
                
        #Ajouter à une liste tout les id et pourcentage des parents de l'enfant 
        for ids in mere_id:
            mere_race = type_id(ids)
            mere_pourcentage = pourcentage(ids)
            
            if (mere_race or mere_pourcentage) == -1:
                print('-1 still left')
                light += 1
            if (mere_race or mere_pourcentage) != -1:
                p.append(mere_pourcentage)
                r.append(mere_race)
        for ids in pere_id:
            pere_race = type_id(ids)
            pere_pourcentage = pourcentage(ids)
            if (mere_race or mere_pourcentage) == -1:
                print('-1 still left')
                light += 1
            if (pere_race or pere_pourcentage) != -1:
                p.append(pere_pourcentage)
                r.append(pere_race)
                
                
                
        if r.count(1) == len(r):
            cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,1,100))
        if r.count(2) == len(r):
            cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,2,100))
        if r.count(3) == len(r):
            cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,3,100))
            
        
        
        if len(r) == 2:
            if 1 in r:
                if 2 in r:
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,1,p[r.index(1)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,2,p[r.index(2)]/2))
                if 3 in r:
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,1,p[r.index(1)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,3,p[r.index(3)]/2))

            if 2 in r:
                if 3 in r:
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,2,p[r.index(2)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,3,p[r.index(3)]/2))
                    
                    
                    
        if len(r) == 3:
            
            if (1 in r) and (2 in r) and (3 in r):
                cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,1,p[r.index(1)]/3))
                cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,2,p[r.index(2)]/3))
                cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,3,p[r.index(3)]/3))
            if ((1 and 2) in r) and (3 not in r):
                if r.count(1) == 2:
                    index = r.index(1)
                    pour = p[r.index(1)] + p[r[index:].index(1)]
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,2,p[r.index(2)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,1,pour/2))
                if r.count(2) == 2:
                    index = r.index(2)
                    pour = p[r.index(2)] + p[r[index:].index(2)]
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,1,p[r.index(1)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,2,pour/2))
                    
                    

            if ((1 and 3) in r) and (2 not in r):
                if r.count(1) == 2:
                    index = r.index(1)
                    pour = p[r.index(1)] + p[r[index:].index(1)]
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,3,p[r.index(3)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,1,pour/2))
                if r.count(3) == 2:
                    index = r.index(3)
                    pour = p[r.index(3)] + p[r[index:].index(3)]
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,1,p[r.index(1)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,3,pour/2))
                    


            if ((2 and 3) in r) and (1 not in r):
                if r.count(2) == 2:
                    index = r.index(2)
                    pour = p[r.index(2)] + p[r[index:].index(2)]
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,3,p[r.index(3)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,2,pour/2))
                if r.count(3) == 2:
                    index = r.index(3)
                    pour = p[r.index(3)] + p[r[index:].index(3)]
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,2,p[r.index(1)]/2))
                    cursor.execute('''INSERT INTO animaux_types VALUES (?,?,?)''',(enfant,3,pour/2))
            

         

                

                        
                        
            
            
conn.commit()
    

conn.close()

