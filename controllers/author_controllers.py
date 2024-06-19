from models.author import Author

def controllerAddAuthor(nom, prenom, date_naissance):
    new_author = Author(nom=nom, prenom=prenom, date_naissance=date_naissance)
    code, msg = new_author.insert()

def controllerDeleteAuthor(id):
    id_author = Author(id=id)
    id_author.delete_author()

def controllerListAuthor():
    Author.list_authors()