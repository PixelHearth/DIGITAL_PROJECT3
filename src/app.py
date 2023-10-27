from data.make_dataset import generate_property_data
from data.preprocessing import CustomPreprocessor
from models.train_model import Models
from models.selection import select_variables
import pandas as pd
import time
def app():
    # calcul le temps du début
    start = time.time()

    # import bdd
    properties = pd.read_csv("C:/Users/Guillaume/Documents/DIGITAL_PROJECT3/bdata/processed/bdd_model.csv", index_col="Unnamed: 0")

    #selection d'une variable pour le test
    new_variable = properties.sample(n=1)
    
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
    print(individual)
    #comparaison avec la valeur réelle
    # print(df_reel)

    #calcul du temps d'exécution total
    end = time.time()
    print("Temps d'exécution : ",round(end-start,2),"secondes")
    
if __name__ == "__main__":
    app()

