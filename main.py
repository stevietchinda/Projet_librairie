from views import author_view, book_view, order_view
def main():
    
    while True:
        
        print(""""""""""""""""""""""1 = Gestion des auteurs""""""""""""""""")
        print(""""""""""""""""""""""2 = Gestion des livres""""""""""""""""")
        print(""""""""""""""""""""""3 = Gestion des commandes""""""""""""""""")

        choix = input("Choisissez une option : ")

        if choix == '1':
             author_views=author_view.menu()
             
        elif choix =='2':
             book_views=book_view.menu()
             
        elif choix =='3':
             book_views=order_view.menu()
             break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
   main()
    

