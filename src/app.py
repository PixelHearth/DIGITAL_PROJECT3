from data.make_dataset import generate_property_data
from data.preprocessing import CustomPreprocessor
from models.train_model import KNN_MODEL
import random
import pandas as pd
import numpy as np
import time
def app():
    # start = time.time()
    # properties = pd.read_csv("data/processed/bdd_model.csv",index_col="Unnamed: 0")
    # new_variable = properties.sample(n=1)
    # # print(new_variable)
    # cpp_p = CustomPreprocessor(properties)
    # cpp_p.fit()
    # cpp_p.transform(new_variable)
    # cpp_p.transform(properties)
    # # ! trouver un moyen de convertir les variables string en variables ordinal avec Ordinal encoder
    # individual = KNN_MODEL(properties,new_variable).k_neighbors()
    # cpp_p.inverse_transform(individual)
    # print(individual)
    # reel =new_variable.values.flatten()
    # df_reel = pd.DataFrame(reel).transpose()
    # cpp_p.inverse_transform(df_reel)
    # print(df_reel)
    # end = time.time()
    # print("Temps d'exécution : ",round(end-start,2),"secondes")
    #!! Ne pas supprimer c'est pour la démo 
    
    start = time.time()
    properties = generate_property_data(100)
    print(properties)
    new_variable = generate_property_data(1)
    # print(new_variable)
    cpp_p = CustomPreprocessor(properties)
    cpp_p.fit()
    cpp_p.transform(new_variable)
    cpp_p.transform(properties)
    # ! trouver un moyen de convertir les variables string en variables ordinal avec Ordinal encoder
    individual = KNN_MODEL(properties,new_variable).k_neighbors()
    cpp_p.inverse_transform(individual)
    print(individual)
    reel =new_variable.values.flatten()
    df_reel = pd.DataFrame(reel).transpose()
    cpp_p.inverse_transform(df_reel)
    print(df_reel)
    end = time.time()
    print("temps d'exécution",end-start,"secondes")
    
if __name__ == "__main__":
    app()

