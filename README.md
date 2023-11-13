# Proposition d'organisation du git basée sur les recommanndations du prof
- /docs
	- Rapport.docx
	- Notice.docx

- /src
	- /data
		- BDD.csv
		- Base_clean.pickle
	- /interfaces
		- projet_digital.xlsm
		- essai2.xlsm
	- /tools
		- /data_preparation
			- cleanBDD.py
			- fonctions_filtrage.py
			- make_dataset.py
			- preprocessing.py
			- csv_2_pickle.py
		- /models
			- selection.py
			- train_model.py
		- /visualisation
			- importance_feature_graph.py

- /tests
	- /tests_data_preparation
		- test_fonctions_filtrage.py
		- test_make_dataset.py
		- test_preprocessing.py
	- /tests_models
		- test_k_neighbors.py
	- /tests_visualisation

- README.md
- requirements.txt

# Lire le document structure de données 
- fichier structure.txt
# Faire un dictionnaire de données 


# Objectif en Cours
- Product owner    : Poursuivre la rédaction de la notice en intégrant les nouvelles variables explicatives et les interfaces de saisie et de résultat sous forme d’images.
- Scrum master     : 
- Data engineer    : Protéger la base de données du projet et accélerer sa réutilisation en la transformant en binaire pour encapsuler l'exécution en utilisant pickle avec Python.
- Data scientist   : Apporter une probabilité de confiance de l’estimation du score du DPE afin d’avoir un résultat plus précis (par exemple : 70% A et 30% B) qui sera transmis en complément à l’utilisateur.
- UI/UX designer   : Apporter des restrictions au formulaire pour éviter l’insertion de valeurs aberrantes (des lettres pour les surfaces par exemple) et ainsi garantir le bon fonctionnement de l’algorithme de prédiction.
- Data Gouvernance : Intégrer le formulaire au classeur Excel du projet capable de lancer le script Python afin d’avoir un outil fonctionnel et proposant une estimation du DPE par le bais d’un message Excel.


# Objectifs  à faire: 
- Product owner    :
- Scrum master     :    
- Data engineer    :
- Data scientist   :
- UI/UX designer   :
- Data Gouvernance :


# Recommendations générales:
- Faire plus de tests
- Tester le programme pour un neophyte voir si ça marche ou s'il y a des modifications à faire
- 
