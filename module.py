import mysql.connector


def insert_action():
    id = input("saisir l'ID de la plante à ajouter: ")
    name = input("saisir le nom de la plante à ajouter: ")
    indication = input("saisir l'indication de la plante à ajouter: ")
    use_part = input("saisir la partie utilisée de la plante à ajouter: ")
    price = input("saisir le prix de la plante à ajouter: ")
    familly_familly_id = input("saisir le numero de la famille: ")


    sql = ("INSERT INTO plantes (id, name, indication, use_part, price, familly_familly_id,) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(id, name, indication, use_part, price, familly_familly_id))

    cursor.execute(sql)

def read_action():
    cursor.execute("SELECT id, name, indication, use_part, price, familly_familly_id FROM plantes")
    rows = cursor.fetchall()

    print("id: name - indication - use_part - price - familly_familly_id")
    for row in rows:
        print('{0} : {1} - {2} - {3} - {4} - {5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))

def update_action():
    cursor.execute("UPDATE plantes SET use_part = 'feuilles' WHERE use_part = 'feuiles")

def delete_action():
    cursor.execute("DELETE FROM plantes WHERE id = " + input_del_plante)

def rechercher_action():
    cursor.execute("SELECT * FROM plantes WHERE nam LIKE ('{}')".format(input_search_plante))
    rows = cursor.fetchall()
    print(rows)

def average_price():
    cursor.execute("SELECT AVG(price) FROM plantes WHERE indication = 'Anesthésiant' ")
    rows = cursor.fetchall()
    print(rows)

    cursor.execute("SELECT AVG(price) FROM plantes WHERE indication = 'Antiseptique'")
    rows = cursor.fetchall()
    print(rows)

    cursor.execute("SELECT AVG(price) FROM plantes WHERE indication = 'Digestion'")
    rows = cursor.fetchall()
    print(rows)

    cursor.execute("SELECT AVG(price) FROM plantes WHERE indication = 'Diurétique'")
    rows = cursor.fetchall()
    print(rows)

#------------------------------------

if __name__ == '__main__':

    conn = mysql.connector.connect(host="127.0.0.1", user="corentinB", password="E8af035aab", database="herboriste")
    cursor = conn.cursor()

    while True:

        read_action()

        choice_option_user = input("Taper (a)jouter une plante, (s)upprimer une plante, (p)rix moyen, (q)uitter: ")

        if choice_option_user == "a":
            insert_action()
        elif choice_option_user == "s":
            input_del_plante = input("ID de la plante a supprimer: ")
            delete_action()
        elif choice_option_user == "r":
            input_search_plante = input("nom de la plante a rechercher: ")
            rechercher_action()
        elif choice_option_user == "p":
            average_price()
        elif choice_option_user == "q":
            break
        else:
            print("Entrée invalide")

        conn.commit()

    conn.close()

