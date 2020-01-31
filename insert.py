import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",user="corentinB",password="E8af035aab", database="herboriste")
cursor = conn.cursor()

def insert_action():
    id = input("saisir l'ID de la plante à ajouter: ")
    nom = input("saisir le nom de la plante à ajouter: ")
    indication = input("saisir l'indication de la plante à ajouter: ")
    partie_utilisee = input("saisir la partie utilisée de la plante à ajouter: ")
    prix = input("saisir le prix de la plante à ajouter: ")

    sql = ("INSERT INTO plantes (id, nom, indication, partie_utilisee, prix) VALUES ('{}', '{}', '{}', '{}', '{}')".format(id, nom, indication, partie_utilisee, prix))

    cursor.execute(sql)

def read_action():
    cursor.execute("SELECT id, nom, indication, partie_utilisee, prix FROM plantes")
    rows = cursor.fetchall()

    for row in rows:
        print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))





insert_action()
read_action()

conn.commit()
conn.close()