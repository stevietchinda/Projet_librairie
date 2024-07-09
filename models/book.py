from db import connect_to_db
from controllers import book_controllers
#from author import Author

class Book:
    def __init__(self, id=None, titre=None, id_auteur=None,  genre=None, prix=None, stock=None):
        self.id= id
        self.titre = titre
        self.id_auteur = id_auteur
        self.genre = genre
        self.prix = prix
        self.stock = stock

    
    def insert_book(self):
        connexion = connect_to_db()
        if connexion:
            c = connexion.cursor()
            c.execute('''
            INSERT INTO book (titre, id_author, genre, prix, stock)
            VALUES (%s, %s, %s, %s, %s)
            ''', (self.titre, self.id_auteur, self.genre, self.prix, self.stock))

            connexion.commit()
            c.close()
            connexion.close()
            print("Livre ajouté avec succès.")

    @staticmethod
    def list_books():
        connexion = connect_to_db()
        if connexion:
            c = connexion.cursor()
            c.execute("SELECT * FROM book")
            rows = c.fetchall()
            books = [Book(*row) for row in rows]
            
            for book in books:
                print(book)

            c.close()
            connexion.close()

    
    def update_book(self):
        connexion = connect_to_db()
        if connexion:
            c = connexion.cursor()


            # Demander les nouvelles informations
            id_book = input("Choisir l'id du livre à modifier: ")
            titre = input(f"Nouveau titre actuel: ") 
            auteur_id = input(f"Nouvel ID de l'auteur actuel: ") 
            genre = input(f"Nouveau genre actuel: ") 
            prix = input(f"Nouveau prix actuel:  ") 
            stock = input(f"Nouveau stock actuel:") 
            c.execute('''
            UPDATE book
            SET titre = %s, auteur_id = %s, genre = %s, prix = %s, stock = %s
            WHERE id = %s
            ''', (titre, auteur_id, genre, prix, stock,id_book))
            livre = c.fetchone()
            print(livre)
            connexion.commit()
            c.close()
            connexion.close()
            print("Livre mis à jour avec succès.")

    
    def delete_book(self):
        connexion = connect_to_db()
        if connexion:
            c = connexion.cursor()
            # Supprimer le livre
            c.execute("DELETE FROM book WHERE id_book = %s", (self.id,))
        
            connexion.commit()
            c.close()
            connexion.close()
            print("Livre supprimé avec succès.")

    def __str__(self):
        return f"Book[ID={self.id}, Titre={self.titre}, AuteurID={self.id_auteur}, Genre={self.genre}, Prix={self.prix}, Stock={self.stock}]"