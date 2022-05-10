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



for row in cursor.execute("SELECT * FROM animaux_types"):
    print(row)
    



# Toujours fermer la connexion quand elle n'est plus utile
conn.close()


