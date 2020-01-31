import mysql.connector
import module as mod

def main():
    conn = mysql.connector.connect(host="127.0.0.1", user="corentinB", password="E8af035aab", database="herboriste")
    mod.cursor = conn.cursor()

    while True:

        mod.read_action()

        choice_option_user = input("Taper (a)jouter une plante, (s)upprimer une plante, (r)echercher une plante, (q)uitter: ")

        if choice_option_user == "a":
            mod.insert_action()
        elif choice_option_user == "s":
            mod.input_del_plante = input("ID de la plante a supprimer: ")
            mod.delete_action()
        elif choice_option_user == "r":
            mod.input_search_plante = input("Nom de la plante a rechercher: ")
            mod.rechercher_action()
        elif choice_option_user == "q":
            break
        else:
            print("Entrée invalide")

        conn.commit()
    conn.close()

if __name__ == '__main__':
    main()


