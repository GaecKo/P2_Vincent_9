import sqlite3
import datetime

# Accès à la base de données

conn = sqlite3.connect('database.db')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

#Holestein, Blanc bleu belge, Jersey  (0,0,0)
all_id = []
step = 0
mere_id = []
pere_id = []
race_mere = []
race_pere = []
race_enfant = []

def get_papa(id_ani):
   # print(id_ani[2])
    for row in cursor.execute('''SELECT type_id FROM animaux_types WHERE animal_id = ?''',(id_ani[2],)):
        return row
    
def get_maman(id_ani):
    #print(id_ani[1])
    for row in cursor.execute('''SELECT type_id FROM animaux_types WHERE animal_id = ?''',(id_ani[1],)):
        print(row)
        return row





for enfant in cursor.execute('''SELECT id, mere_id, pere_id FROM velages'''):
    all_id.append(enfant)
    

print(len(all_id))
count = []
for i in range (len(all_id)):
    tp = get_papa(all_id[2])
    tm = get_maman(all_id[1])

    p = [0,0,0]
    #print(int(tp[0]))
    #print(int(tp[0]))
    #print(tp,tm)
    p[int(tp[0])-1] = 1
    p[int(tm[0])-1] = 1
        
    
    p = str(p)
        

    #print(pourcentage)
    cursor.execute('''UPDATE animaux_types SET pourcentage=? WHERE animal_id=?''',(p,all_id[i][0],))
    count.append(p)

    
    
check = []
for row in cursor.execute('''SELECT pourcentage FROM animaux_types'''):
    print(row)
    check.append(row)
print(len(check))
    
    

    







#print(all_id[step][0])






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






