from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

class Models:
    def __init__(self,dataframe,individual_features):
        self.dataframe =dataframe
        self.individual_feature = individual_features
        self.dependent_variable = self.dataframe.iloc[:,0].values
        self.independent_variable = self.dataframe.iloc[:, 1:].values
        self.individual_features  = individual_features.iloc[:,1:].values

    def k_neighbors(self):
        """ création d'un algorithme de k_neighbors sur les données properties
        parameter "dataframe", est le dataframe de l'ademe nettoyé
        """
        #entrainements
        neigh = KNeighborsClassifier(n_neighbors=5)

        #entrainement des données
        neigh.fit(self.independent_variable,self.dependent_variable)

        #prédiction
        prediction = neigh.predict(self.individual_features)
        score = neigh.score(self.independent_variable, self.dependent_variable)
        print(f"Précision du modèle : {score}")
    
        #restitution d'un dataframe
        self.independant_variable = self.individual_features.flatten()
        result = np.concatenate([prediction, self.independant_variable])
        dataframe_decoded = pd.DataFrame(result).transpose()
        return dataframe_decoded