# Description du projet
Le présent repository GitHub concerne un produit digital conçu pour estimer le Diagnostic de Perfomrance Énergétique (DPE) d'un appartement. Le produit s'articule autour d'un fichier Excel livré à l'utilisateur et qui permet à celui-ci de rentrer les informations relatives à son logement par le biais d'un formulaire. La validation du formulaire Excel permet de lancer l'exécution d'un script Python (sans action de l'utilisateur) qui calcule le DPE du logement à l'aide de modèles prédictifs et qui réalise des graphiques en guise de résultats. Ces derniers sont retransmis au classeur Excel et affichés immédiatement à l'utilisateur.

# Organisation des fichiers du repository
Ce repository est constitué des trois principaux dossiers suivants :
- docs
- src
- test
On retrouve égalament le présent README expliquant la structure du repository et un fichier requirements.txt qui a pour but d'indiquer les différentes librairies nécessaires pour ce projet ainsi que leur version.

Le dossier docs contient les différents comptes-rendus réalisés au cours de l'avancée du projet.

Le dossier src contient à sa racine le fichier formulaire.xlsm qui est le fichier Excel du projet à destination de l'utilisateur, c'est ce fichier qui lance le formulaire et exécute le script python. Le dossier src contient également les sous-dossiers suivants :
- data : ce dossier contient tous les scripts Python de nettoyage de la base de données ainsi que le script de trasnformation en binaire, un sous dossier database est également présent et comporte la base de données nettoyée en version csv et pickle.
- features :
- models : ce dossier contient les scripts d'analyse des données et de modèles de prédiction réalisés en Python.
- notebook : ce dossier contient les fichiers de prise de notes à propos du projet.
- visualization : ce dossier contient les scripts Python de création de graphique nécessaires pour les résultats du DPE mais aussi pour la visualisation des données préliminaire.

Pour finir, le dossier test est constitué des quatre sous-dossiers suivants :
- data : ce dossier contient les tests des programmes de nettoyage de la base de données
- features
- models : ce dossier contient les tests des scripts de modèles de prédiction
- visualization : ce dossier contient les tests des scripts de création de graphique

La documentation sur la base de données, le DPE et la question du RGPD s'appliquant à nos données est disponible dans le Wiki du repository.

# Objectif en Cours
- Product owner    : Poursuivre la rédaction de la notice en intégrant les nouvelles variables explicatives et les interfaces de saisie et de résultat sous forme d’images.
- Scrum master     : 
- Data engineer    : Protéger la base de données du projet et accélerer sa réutilisation en la transformant en binaire pour encapsuler l'exécution en utilisant pickle avec Python.
- Data scientist   : Apporter une probabilité de confiance de l’estimation du score du DPE afin d’avoir un résultat plus précis (par exemple : 70% A et 30% B) qui sera transmis en complément à l’utilisateur.
- UI/UX designer   : Apporter des restrictions au formulaire pour éviter l’insertion de valeurs aberrantes (des lettres pour les surfaces par exemple) et ainsi garantir le bon fonctionnement de l’algorithme de prédiction.
- Data Gouvernance : Intégrer le formulaire au classeur Excel du projet capable de lancer le script Python afin d’avoir un outil fonctionnel et proposant une estimation du DPE par le bais d’un message Excel.

# Recommandations générales:
- Faire plus de tests
- Tester le programme pour un neophyte voir si ça marche ou s'il y a des modifications à faire
