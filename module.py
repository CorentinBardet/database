import mysql.connector


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

    print("id: nom - indication - partie_utilisee - prix")
    for row in rows:
        print('{0} : {1} - {2} - {3} - {4}'.format(row[0], row[1], row[2], row[3], row[4]))

def update_action():
    cursor.execute("UPDATE plantes SET partie_utilisee = 'feuilles' WHERE partie_utilisee = 'feuiles")

def delete_action():
    cursor.execute("DELETE FROM plantes WHERE id = " + input_del_plante)

def rechercher_action():
    cursor.execute("SELECT * FROM plantes WHERE nom LIKE ('{}')".format(input_search_plante))
    rows = cursor.fetchall()
    print(rows)

#------------------------------------

if __name__ == '__main__':

    conn = mysql.connector.connect(host="127.0.0.1", user="corentinB", password="E8af035aab", database="herboriste")
    cursor = conn.cursor()

    while True:

        read_action()

        choice_option_user = input("Taper (a)jouter une plante, (s)upprimer une plante, (q)uitter: ")

        if choice_option_user == "a":
            insert_action()
        elif choice_option_user == "s":
            input_del_plante = input("ID de la plante a supprimer: ")
            delete_action()
        elif choice_option_user == "r":
            input_search_plante = input("Nom de la plante a rechercher: ")
            rechercher_action()
        elif choice_option_user == "q":
            break
        else:
            print("Entrée invalide")

        conn.commit()

    conn.close()

