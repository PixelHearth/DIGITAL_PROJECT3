from data.make_dataset import generate_property_data
from data.preprocessing import CustomPreprocessor
from models.train_model import KNN_MODEL
import random
import pandas as pd
import numpy as np
import time
def app():
    start = time.time()
    properties = pd.read_csv("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/data/processed/bdd_model.csv",index_col="Unnamed: 0")
    new_variable = properties.sample(n=1)
    cpp_p = CustomPreprocessor(properties)
    cpp_p.fit()
    cpp_p.transform(new_variable)
    cpp_p.transform(properties)
    individual = KNN_MODEL(properties,new_variable).k_neighbors()
    variable = KNN_MODEL(properties,new_variable).Select_Variables(10)
    cpp_p.inverse_transform(individual)
    print(individual)
    reel =new_variable.values.flatten()
    df_reel = pd.DataFrame(reel).transpose()
    cpp_p.inverse_transform(df_reel)
    print(df_reel)
    end = time.time()
    print("Temps d'exécution : ",round(end-start,2),"secondes") 
    
if __name__ == "__main__":
    app()

