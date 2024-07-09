from controllers import book_controllers

def menu():
    while True:
        print("\n--- Gestion des Livres ---")
        print("1. Ajouter un livre")
        print("2. Mettre à jour un livre")
        print("3. Supprimer un livre")
        print("4. Afficher la liste des livres")
        print("5. Rechercher un livre")
        print("6. Retour au menu principal")

        choix = input("Choisissez une option : ")

        if choix == '1':
            titre = input("Titre du livre: ")
            genre = input("Genre du livre: ")
            prix = input("entrer le prix: ")
            stock = input("entrer le stock: ")
            book_controllers.controllerinsertBook(titre, genre,prix,stock)
            
        elif choix == '2':
            book_controllers.controllerListbook()
        
        elif choix == '3':
            book_controllers.controllerListbook()
            id_book=input("Entrer l'id de l'auteur à supprimer: ")
            book_controllers.controllerDeleteBook(id_book)
        # elif choix == '4':
        #     Book.list_books()
        # elif choix == '5':
        #     Book.search_book()  
        elif choix == '6':
            break
        else:
            print("Option invalide. Veuillez réessayer.")