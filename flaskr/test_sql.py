import sqlite3 as sql

class DataBase:
    def __init__(self, database):
        self.database = database
        

    def famille(self):
        
        conn = sql.connect(self.database)

        mycursor = conn.cursor()

        mycursor.execute("SELECT id, nom FROM familles")

        myresult = mycursor.fetchall()
        
        self.liste = {}
        
        for line in myresult:
            #Id = line[0]
           # Nom = line[1]
            self.liste[line[0]] = line[1]

        return self.liste

    ''' Pour prendre le ID des familles, il faut faire une boucle 
    for x in liste et prendre x[0]

    et pour prendre le nom de la famille il faut faire x[1]'''

    '''def Id_famille(self):
        id = []
        for i in self.liste:
            id.append(i[0])
        return id'''

    def Nom_famille(self):
        id = []
        nom = ""
        for key, value in self.famille().items():
            nom += "<option value="+str(key)+">"+value+"</option>\n"
        return nom

DataBase('database.db').famille()
test = DataBase('database.db').Nom_famille()
print(test)
