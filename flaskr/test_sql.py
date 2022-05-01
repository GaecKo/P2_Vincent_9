import sqlite3 as sql

class DataBase:

    def __init__(self, database):
        self.database = database
        self.liste = []

    def famille(self):
        
        conn = sql.connect(self.database)

        mycursor = conn.cursor()

        mycursor.execute("SELECT * FROM familles")

        myresult = mycursor.fetchall()

        for line in myresult:
            Id = line[0]
            Nom = line[1]
            self.liste.append((Id, Nom))

        return self.liste

    ''' Pour prendre le ID des familles, il faut faire une boucle 
    for x in liste et prendre x[0]

    et pour prendre le nom de la famille il faut faire x[1]'''

    def Id_famille(self):
        id = []
        for i in self.liste:
            id.append(i[0])
        return id

    def Nom_famille(self):
        id = []
        for i in self.liste:
            id.append(i[1])
        return id

test = DataBase('database.db').famille()
print(test)
