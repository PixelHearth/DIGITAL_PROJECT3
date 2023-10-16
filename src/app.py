from data.make_dataset import generate_property_data
from data.preprocessing import CustomPreprocessor
from models.train_model import k_neighbors
import random
import pandas as pd
import numpy as np
def app():
    properties = generate_property_data(100)
    new_variable = generate_property_data(1)
    cpp_p = CustomPreprocessor(properties)
    cpp_p.fit_transform()
    cpp_p.transform(new_variable)
    cpp_p.transform(properties)
    # ! trouver un moyen de convertir les variables string en variables ordinal avec Ordinal encoder
    predict = k_neighbors(properties,new_variable)
    independante_variable =new_variable.iloc[:,1:].values.flatten()
    reel =new_variable.values.flatten()
    result = np.concatenate([predict, independante_variable])
    df_reel = pd.DataFrame(reel).transpose()
    cpp_p.inverse_transform(df_reel)
    print(df_reel)
    df_result = pd.DataFrame(result).transpose()
    cpp_p.inverse_transform(df_result)
    print(df_result)
    
if __name__ == "__main__":
    app()

