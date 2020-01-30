import mysql.connector

conn = mysql.connector.connect(host="127.0.0.1",user="corentinB",password="E8af035aab", database="herboriste")
cursor = conn.cursor()


cursor.execute("SELECT id, nom, indication, partie_utilisee, prix FROM plantes")
rows = cursor.fetchall()


for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

conn.close()