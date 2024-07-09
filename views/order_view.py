from controllers import order_controllers, book_controllers

def menu():
    while True:
        print("\n--- Gestion des commandes ---")
        print("1. Ajouter une commande")
        print("2. Afficher la liste des commandes")
        print("3. Supprimer une commande")
        print("4. Mettre à jour les informations d'une commande")
        print("5. Rechercher une commande")
        print("6. Retour au menu principal")

        choix = input("Choisissez une option : ")

        if choix == '1':
            book_controllers.controllerListbook()
            
            id_book = input("id du livre à commander : ")
            quantité = input("quantité : ")
            dateCommande = input("entrer la date de la commande : ")
         
            order_controllers.controllerinsertOrder(id_book,quantité, dateCommande)
        elif choix == '2':
            order_controllers.controllerListOrder()
        
        elif choix == '3':
            order_controllers.controllerListOrder()
            id_order = input("Entrer l'id de la commande à suprimer: ")
            order_controllers.controllerDeleteOrder(id_order)    
        
        elif choix == '6':
            break
        else:
            print("Option invalide. Veuillez réessayer.")