
from db import connect_to_db

class Author:
    def __init__(self, id=None, nom=None, prenom=None, date_naissance=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def __str__(self):
        return f"Author[ID={self.id}, Nom={self.nom}, Prenom={self.prenom}, DateNaissance={self.date_naissance}]"

    @staticmethod
    def list_authors():
        connexion = connect_to_db()
        if connexion:
            c = connexion.cursor()
            c.execute("SELECT id_author as id, nom, prenom, date_naissance FROM author")
            rows = c.fetchall()
            authors = [Author(*row) for row in rows]

            for author in authors:
                print(author)

            c.close()
            connexion.close()

    def delete_author(self):
        connexion = connect_to_db()
        if connexion:
            c = connexion.cursor()
            # Assurez-vous que la colonne `id` existe dans la table `author`
            #%s generalement utilisé pour les chaine de charactère et %d pour les nombres decimals
            c.execute("DELETE FROM author WHERE id_author = %s", (self.id,))
            connexion.commit()
            c.close()
            connexion.close()
            print("Auteur supprimé avec succès.")

    def insert(self):
        try:
            connexion = connect_to_db()
            if connexion:
                c = connexion.cursor()
                c.execute('''
                INSERT INTO author (nom, prenom, date_naissance)
                VALUES (%s, %s, %s)
                ''', (self.nom, self.prenom, self.date_naissance))
                connexion.commit()
                c.close()
                connexion.close()
                print("Auteur ajouté avec succès.")
                return 0, "ok"
        except Exception as err:
            print(err)
            return 1, str(err)
        
@staticmethod
def get_author_ids():
        connexion = connect_to_db()
        if connexion:
            c = connexion.cursor()
            c.execute("SELECT id_author, nom, prenom FROM author")
            rows = c.fetchall()
            c.close()
            connexion.close()
            return rows