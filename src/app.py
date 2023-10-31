from data.make_dataset import generate_property_data
from data.preprocessing import CustomPreprocessor
from models.train_model import Models
from models.selection import select_variables
from data.CleanBDD import clean
import pandas as pd
import time
from IPython.display import display
def app():
    # calcul le temps du début
    start = time.time()

    # import bdd
    properties = clean("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/data/raw/Bdd_newfiltre.xlsx")
    # properties = pd.read_csv("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/data/processed/bdd_model.csv", index_col="Unnamed: 0")
    #selection d'une variable pour le test
    new_variable = properties.sample(n=1)
    df_reel = new_variable
     
    #instance du framework de processing et entrainement des données sur properties pour l'encodage
    cpp_p = CustomPreprocessor(properties)
    cpp_p.fit()
    #encodage des variables dans les deux bases de données
    cpp_p.transform(new_variable)
    cpp_p.transform(properties)

    #selection des variables importantes, il faut avoir fait l'encodage aupréalable
    properties,new_variable,nv_colonne = select_variables(properties,new_variable)
    # print(properties,new_variable)

    #instance et entrainement du k_neighbors sur les données encodées 
    individual = Models(properties,new_variable).k_neighbors()
    individual.columns = nv_colonne
    print(individual)
    #restitution d'un dataframe compréhensible pour un humain
    cpp_p.inverse_transform(individual)
    cpp_p.inverse_transform(new_variable)


    print(individual)
    print(new_variable)
    #comparaison avec la valeur réelle

    #calcul du temps d'exécution total
    end = time.time()
    print("Temps d'exécution : ",round(end-start,2),"secondes") 
    
if __name__ == "__main__":
    app()

