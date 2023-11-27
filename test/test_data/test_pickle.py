import pickle
import csv

# Passage du fichier CSV au format Pickle

with open("src/Base_clean.csv", "r") as file:
    lecteur_csv = csv.reader(file)
    donnees = list(lecteur_csv)
    
    with open("src/Base_clean.pickle", "wb") as file_pickle:
        pickle.dump(donnees, file_pickle)

# Lecture du fichier pickle (passage du format pickle au format normal)

# with open("Base_clean.pickle", "rb") as file2:
#     donnees2 = pickle.load(file2)
#     print(donnees2)