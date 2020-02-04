import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",user="corentinB",password="E8af035aab", database="herboriste")
cursor = conn.cursor()
sql = "INSERT INTO plante (id, nom, indication, partie_utilisee, prix) VALUES (%s, %s, %s, %s, %s)"

id = input("saisir l'ID de la plante à ajouter")
nom = input("saisir le nom de la plante à ajouter")
indication = input("saisir l'indication de la plante à ajouter")
partie_utilisee = input("saisir la partie utilisée de la plante à ajouter")
prix = input("saisir le prix de la plante à ajouter")

val = (id, nom, indication, partie_utilisee, prix)
cursor.execute(sql, val)
conn.commit()
conn.close()



def fn_displayed_familly_identified():
    displayed_familly_identified = Plantes.select(Familly.name, fn.COUNT(Plantes.name).alias("dis"))


def fn_min_max_sub_class():
    min_max_sub_class = Plantes.select(Sub_class.name, fn.MAX(Plantes.price).alias("max"), fn.MIN(Plantes.price).alias("max")).join(Familly).join(Sub_class)