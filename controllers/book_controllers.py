from models.author import Author
from models.book import Book

 #- Ajouter un nouveau livre
def controllerinsertBook(titre, genre, prix, stock):
    authors = Author.get_author_ids()
    if not authors:
        print("Aucun auteur disponible. Veuillez d'abord ajouter des auteurs.")
        return 0
    
    print("Liste des auteurs disponibles:")
    for author in authors:
        print(f"ID: {author[0]}, Nom: {author[1]}, Prénom: {author[2]}")
    
    id_auteur = input("Entrez l'ID de l'auteur choisi: ")
    
    # Vérifiez si l'ID entré est valide
    valid_ids = [str(author[0]) for author in authors]
    if id_auteur not in valid_ids:
        print("ID d'auteur invalide.")
        return
    
    new_book = Book(titre=titre, id_auteur=id_auteur,genre=genre, prix=prix, stock=stock)
    new_book.insert_book()

def controllerDeleteBook(id):
    id_book = Book(id=id)
    id_book.delete_book()
  
def controllerListbook():
    Book.list_books()


# def controllerUpdateBook():
#     connexion = connect_to_db()
#     if connexion:
#         c = connexion.cursor()
        
#         # Demander à l'utilisateur de fournir l'ID du livre à mettre à jour
#         book_id = input("Entrez l'ID du livre à mettre à jour: ")

#         try:
#             id_book = int(book_id)
#         except ValueError:
#             print("Erreur : L'ID doit être un entier.")
#             return
        
#         # Vérifier si le livre existe
#         c.execute("SELECT * FROM book WHERE id = %s", (id_book,))
#         book = c.fetchone()
        
#         if not book:
#             print("Livre introuvable.")
#             return

#         # Afficher les informations actuelles du livre
#         print("Informations actuelles du livre:")
#         print(f"Titre: {book[1]}")
#         print(f"Auteur ID: {book[2]}")
#         print(f"Genre: {book[3]}")
#         print(f"Prix: {book[4]}")
#         print(f"Stock: {book[5]}")
        
#         return f"Book[Titre={book[1]}, AuteurID={book[2]}, Genre={book[3]}, Prix={book[4]}, Stock={book[5]}]"


