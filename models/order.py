from db import connect_to_db
from mysql.connector import Error
class Order:
    def __init__(self, id_order=None, id_book=None, quantite=None, date_commande=None):
        self.id_order = id_order
        self.id_book = id_book
        self.quantite = quantite
        self.date_commande = date_commande

    def __str__(self):
        return f"Order[ID={self.id}, BookID={self.id_book}, Quantite={self.quantite}, DateCommande={self.date_commande}]"
    
    
    def insert_order(self):
     
        connexion = connect_to_db()
        if connexion:
            try:
                c = connexion.cursor()
                c.execute('''
                SELECT book.id_book, book.titre, author.nom, author.prenom
                FROM book
                LEFT JOIN author ON book.id_author = author.id_author
                WHERE book.id_book = %s
                ''', (self.id_book,))
                book = c.fetchone()
                if not book :
                    print("Livre non trouvé.")
                    return

                # Si le livre existe, insérez la commande
                c.execute('''
                INSERT INTO commande (id_book, quantite, date_commande)
                VALUES (%s, %s, %s)
                ''', (self.id_book, self.quantite, self.date_commande))
                connexion.commit()
                print("Commande ajoutée avec succès.")
            except Error as e:
                print(f"Erreur lors de l'insertion de la commande : {e}")
            finally:
                  
             c.close()
        connexion.close()
        
    @staticmethod  
    def selectOrder():
        connexion = connect_to_db
        if connexion:
            try:
                c = connexion.cursor()
                c.execute('''
                SELECT * FROM commande ''')
                rows = c.fetchall()
                orders = [Order(*row) for row in rows]
            
                for order in orders:
                   print(order)

                print("affichage des commandes reussies.")
            except Error as e:
                print(f"Erreur lors de l'insertion de la commande : {e}")
            finally:
                  
                  c.close()
        connexion.close()
                
    def deleteOrder(self):
        connexion = connect_to_db
        
        if connexion:
            
                c=connexion.cursor()
                c.execute("DELETE * FROM commande WHERE id_order = %s",(self.id_order,))
                connexion.commit()
                c.close()
        connexion.close()
        print("commande supprimé avec succès.")

            