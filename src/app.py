from data.preprocessing import CustomPreprocessor
from models.train_model import Models
from models.selection import select_variables
from visualization.importance_feature_graph import plot_feature_importance
from data.CleanBDD import clean
import pandas as pd
import time
def app():
    # calcul le temps du début
    start = time.time()

    # import bdd
    properties = clean("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/data/processed/Base_clean.csv")
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
    nb_features = 10
    properties,new_variable,nv_colonne,importance = select_variables(properties,new_variable,nb_features)
    
    #création du graph des importances dans le modèle de selection
    plot_feature_importance(importance,10)
    #instance et entrainement du k_neighbors sur les données encodées 
    individual = Models(properties,new_variable).k_neighbors()
    individual.columns = nv_colonne

    #restitution d'un dataframe compréhensible pour un humain
    #valeur prédite du k_neighbors
    cpp_p.inverse_transform(individual)

    #valeur réelle de l'individu testé
    cpp_p.inverse_transform(new_variable)

    #comparaison avec la valeur réelle
    print(individual)
    print(new_variable)

    #calcul du temps d'exécution total
    end = time.time()
    print("Temps d'exécution : ",round(end-start,2),"secondes") 
    
if __name__ == "__main__":
    app()

