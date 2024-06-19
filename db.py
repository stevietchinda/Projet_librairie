import mysql.connector
from mysql.connector import Error

# Connexion à la base de données MySQL
def connect_to_db ():
    try:
        connexion =mysql.connector.connect(host='localhost',user="root",password="",database='librairie_bdd' )

        # Vérification de la connexion
        if connexion.is_connected():
            print("Connexion réussie à la base de données MySQL")

        # Création d'un curseur
        c = connexion .cursor()
        return connexion
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL : {e}")
        return None, None

# déConnexion à la base de données MySQL
def deconnect_to_db ():
    try:
         connect_to_db.close()
    except Error as e:
        print(f"Erreur lors de la déconnexion à MySQL : {e}")
    return None



