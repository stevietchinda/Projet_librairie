from controllers import author_controllers

def menu():
    while True:
        print("\n--- Gestion des auteurs ---")
        print("1. Ajouter un auteur")
        print("2. Mettre à jour un auteur")
        print("3. Supprimer un auteur")
        print("4. Afficher la liste des auteurs")
        print("5. Rechercher un auteur")
        print("6. Retour au menu principal")

        choix = input("Choisissez une option : ")
        
        if choix == '1':
             
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            date_naissance = input("Date de naissance (YYYY-MM-DD): ")
            author_controllers.controllerAddAuthor(nom,prenom,date_naissance)
        
        elif choix == '3':
            author_controllers.controllerListAuthor()
            id_author = input("Entre l'id de l'auteur que vous voulez supprimer: ")
            author_controllers.controllerDeleteAuthor(id_author)
            print(id)
            
            
        elif choix == '4':
            author_controllers.controllerListAuthor()
            break
        else:
            print("Option invalide. Veuillez réessayer.")