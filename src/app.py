from data.make_dataset import generate_property_data
from data.preprocessing import CustomPreprocessor
from models.train_model import k_neighbors
import random
import pandas as pd
import numpy as np
def app():
    properties = generate_property_data(100)
    
    cpp = CustomPreprocessor()
    cpp.fit(properties)
    cpp.transform(properties)
    
    new_variable = generate_property_data(1)
    print(new_variable)
    cpp.transform(new_variable)
    #! trouver un moyen de convertir les variables string en variables ordinal avec Ordinal encoder
    predict = k_neighbors(properties,new_variable)
    independante_variable =new_variable.iloc[:,1:].values.flatten()
    reel =new_variable.values.flatten()
    result = np.concatenate([predict, independante_variable])
    print(reel)
    print(result)
    cpp.encoder.inverse_transform(result)
    
if __name__ == "__main__":
    app()

