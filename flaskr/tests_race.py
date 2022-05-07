import sqlite3
import datetime

# Accès à la base de données

conn = sqlite3.connect('database.db')

# Le curseur permettra l'envoi des commandes SQL
cursor = conn.cursor()

#Holestein, Blanc bleu belge, Jersey
enfant_id = []
step = 0
mere_id = []
pere_id = []
race_mere = []
race_pere = []
ra_enfant = []

for enfant in cursor.execute('''SELECT id FROM velages'''):
    enfant_id.append(enfant)

for ra_enf in cursor.execute('''SELECT type_id FROM animaux_types WHERE animal_id=?''',(enfant_id[step])):
    step += 1
    ra_enfant.append(ra_enf)
    
step = 0


for parents in cursor.execute('''SELECT mere_id FROM velages WHERE id=? ''',(enfant_id[step])):
    step += 1
    mere_id.append(parents)
    #print(parents)

step = 0

for parents in cursor.execute('''SELECT pere_id FROM velages WHERE id=? ''',(enfant_id[step])):
    step += 1
    pere_id.append(parents)
    #print(parents)

step = 0

#print(mere_id[0], pere_id[0])

for ra_mere in cursor.execute('''SELECT type_id FROM animaux_types WHERE animal_id=?''',(mere_id[step])):
    step += 1
    race_mere.append(ra_mere)
    
step = 0
    
for ra_pere in cursor.execute('''SELECT type_id FROM animaux_types WHERE animal_id=?''',(pere_id[step])):
    step += 1
    race_pere.append(ra_pere)
    
#for i in range (len(enfant_id)):
 #   print(enfant_id[i],ra_enfant[i],mere_id[i],pere_id[i],race_mere[i],race_pere[i])
    


count_parent_dif = 0
c_m_d = 0
c_p_d = 0

print(len(ra_enfant),len(race_pere))

for i in range (len(ra_enfant)):
    if ra_enfant[i] != race_mere[i] and ra_enfant[i] != race_pere[i]:
        print("!!!")
        count_papa_dif += 1
    if ra_enfant[i] != race_mere[i]:
        print("!!!")
        c_m_d += 1
    if ra_enfant[i] != race_pere[i]:
        print("!!!")
        c_p_d += 1
        



print(count_parent_dif,c_m_d, c_p_d)
    





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






