import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",user="corentinB",password="E8af035aab", database="herboriste")
cursor = conn.cursor()


#cursor.execute("UPDATE plantes SET partie_utilisee = 'feuilles' WHERE partie_utilisee = 'feuile' ")

cursor.execute("UPDATE plantes SET prix = '2.2' WHERE prix = '2'")


conn.commit()
conn.close()