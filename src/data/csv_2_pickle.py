import pandas as pd
import pickle

def stock_pickle_csv(path_in:str, path_out:str):

    """
    Stocke en pickle le fichier csv mis en entrée

    var:
    path_in (str): chemin du fichier csv en entrée
    path_out (str): chemin du fichier pkl en sortie
    """

    # ouverture des données
    df = pd.read_csv(path_in, sep = ",")

    # écriture du pickle avec les données csv
    with open(path_out, "wb") as file_pickle:
        pickle.dump(df, file_pickle)

def open_pkl(path_in:str):
    # test ouverture d'un pickle
    with open(path_in, "rb") as file2:
        return(pickle.load(file2))
    

if __name__ == "__main__":
    stock_pickle_csv("Base_clean.csv", "Base_clean.pkl")
    print(open_pkl("Base_clean.pkl"))