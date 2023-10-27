# Pour tester le K_neighbors algorithmes on doit s'assurer que la variable entrée est bien un dataframe, qu'il est ne contient pas de none, date, ou autre
from ...src.app import Models
import pandas as pd

data = {
            'Target': [0, 1, 0, 1, 0],
            'Feature1': [1, 2, 3, 4, 5],
            'Feature2': [5, 4, 3, 2, 1]
        }

individual_feature = {
            'Target': [0],
            'Feature1': [1],
            'Feature2': [5]
        }
test_dataframe = pd.DataFrame(data)
test_individual_feature = pd.DataFrame(individual_feature)

model = Models(test_dataframe,test_individual_feature)

dataframe_decoded = model.k_neighbors()