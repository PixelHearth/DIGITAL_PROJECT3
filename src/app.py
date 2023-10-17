from data.make_dataset import generate_property_data
from data.preprocessing import CustomPreprocessor
from models.train_model import KNN_MODEL
import random
import pandas as pd
import numpy as np
def app():
    properties = generate_property_data(100)
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
    
if __name__ == "__main__":
    app()

