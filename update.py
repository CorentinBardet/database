import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",user="corentinB",password="E8af035aab", database="herboriste")
cursor = conn.cursor()




cursor.execute("UPDATE plantes SET partie_utilisee = feuile ")


conn.commit()
conn.close()