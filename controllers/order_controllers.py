
from models.order import Order
     
def controllerinsertOrder(id_book, quantite, date_commande):
     new_commande = Order(id_book=id_book, quantite=quantite, date_commande=date_commande)
     new_commande.insert_order()
     
def controllerListOrder():
     Order.selectOrder()
    
     
def controllerDeleteOrder(id):
    delete_id=Order(id=id)
    delete_id.deleteOrder()
    