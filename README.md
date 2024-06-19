### Logiciel de gestion d'une librairie

**Description du Projet:**

Vous allez développer un logiciel de gestion d&#39;une librairie. Ce projet a pour but de vous
permettre de maîtriser le langage Python, d&#39;améliorer la modularité de votre code, d&#39;utiliser
des librairies Python, de gérer des bases de données SQL et de structurer votre code de
manière optimale. Ce logiciel sera sans interface graphique (CLI) et permettra de gérer trois
entités principales : Livre, Auteur et Commande.

**Objectifs du Projet:**

1. **Maîtrise du Code Python:** Écrire du code Python clair, concis et efficace.
2. **Modularité:** Diviser le projet en modules pour faciliter la maintenance et la réutilisation
du code.
3. **Utilisation des Librairies:** Utiliser des bibliothèques Python pour simplifier certaines
tâches (par exemple, `sqlite3` pour la gestion de la base de données).
4. **Gestion de Base de Données SQL:** Créer, lire, mettre à jour et supprimer des
enregistrements dans une base de données SQL.
5. **Structuration du Code:** Adopter une structure de projet claire et logique.

**Description des Entités:**

1. **Livre (Book):**
- ID (identifiant unique)
- Titre
- Auteur (ID de l&#39;auteur)
- Genre
- Prix
- Stock

2. **Auteur (Author):**
- ID (identifiant unique)
- Nom
- Prénom

- Date de naissance

3. **Commande (Order):**
- ID (identifiant unique)
- ID du livre
- Quantité
- Date de commande

**Fonctionnalités à Implémenter:**

1. **Gestion des Livres:**
- Ajouter un nouveau livre
- Mettre à jour les informations d&#39;un livre existant
- Supprimer un livre
- Afficher la liste des livres
- Rechercher un livre par titre ou par auteur

2. **Gestion des Auteurs:**
- Ajouter un nouvel auteur
- Mettre à jour les informations d&#39;un auteur existant
- Supprimer un auteur
- Afficher la liste des auteurs
- Rechercher un auteur par nom ou prénom

3. **Gestion des Commandes:**
- Ajouter une nouvelle commande
- Mettre à jour les informations d&#39;une commande existante
- Supprimer une commande
- Afficher la liste des commandes
- Rechercher une commande par date ou par ID de livre

**Structure du Projet:**

Le projet sera structuré en plusieurs fichiers et dossiers pour améliorer la lisibilité et la
maintenabilité du code:

- `main.py` : Le point d&#39;entrée du programme.
- `db.py` : Gestion de la base de données (connexion, création des tables, etc.).
- `models/` : Dossier contenant les classes représentant les entités (Livre, Auteur,
Commande).
- `book.py`
- `author.py`
- `order.py`
- `controllers/` : Dossier contenant les fonctions de gestion des entités.
- `book_controller.py`
- `author_controller.py`
- `order_controller.py`
- `views/` : Dossier contenant les fonctions d&#39;interaction avec l&#39;utilisateur (affichage des
menus, saisie des données, etc.).
- `book_view.py`
- `author_view.py`
- `order_view.py`
