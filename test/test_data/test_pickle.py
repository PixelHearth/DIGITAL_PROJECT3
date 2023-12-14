import pickle
import csv

# Passing the CSV file to Pickle format

with open("src/Base_clean.csv", "r") as file:
    lecteur_csv = csv.reader(file)
    donnees = list(lecteur_csv)
    
    with open("src/Base_clean.pickle", "wb") as file_pickle:
        pickle.dump(donnees, file_pickle)

# Reading the pickle file (change from pickle format to normal format) 

# with open("Base_clean.pickle", "rb") as file2:
#     donnees2 = pickle.load(file2)
#     print(donnees2)
