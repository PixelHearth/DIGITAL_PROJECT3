from data.preprocessing import CustomPreprocessor
from models.train_model import Models
from models.selection import select_variables
from visualization.importance_feature_graph import plot_feature_importance
from data.CleanBDD import clean
from data.make_dataset import importation_excel
import pandas as pd
import time
def app():
    # calcul le temps du début
    start = time.time()

    # import bdd
    properties = clean("C:/Users/Guillaume/Documents/DIGITAL_PROJECT3/bdata/raw/Base_clean.csv")
    new_variable = importation_excel("C:/Users/Guillaume/Documents/DIGITAL_PROJECT3/essai.xlsm", "saisie")
    #selection d'une variable pour le test
    # new_variable = properties.sample(1)

    #instance du framework de processing et entrainement des données sur properties pour l'encodage
    cpp_p_selection = CustomPreprocessor(properties)
    cpp_p_selection.fit()

    #encodage des variables dans les deux bases de données
    cpp_p_selection.transform(properties)

    #selection des variables importantes, il faut avoir fait l'encodage aupréalable
    nb_features = 10
    properties,importance = select_variables(properties,nb_features)
    cpp_p_selection.inverse_transform(properties)

    #instance du framework de processing et entrainement des données sur properties pour l'encodage après selection
    cpp_kneigh = CustomPreprocessor(properties)
    cpp_kneigh.fit()

    cpp_kneigh.transform(properties)
    
    cpp_kneigh.transform(new_variable)
    

    #création du graph des importances dans le modèle de selection
    plot_feature_importance(importance,10)

    #instance et entrainement du k_neighbors sur les données encodées 
    individual = Models(properties,new_variable).k_neighbors()
    individual.columns = new_variable.columns

    #restitution d'un dataframe compréhensible pour un humain
    #valeur prédite du k_neighbors
    cpp_kneigh.inverse_transform(individual)
    print(individual.iloc[:,0].values)
    


    #calcul du temps d'exécution total
    end = time.time()
    print("Temps d'exécution : ",round(end-start,2),"secondes") 
    return individual
    
if __name__ == "__main__":
    app()

