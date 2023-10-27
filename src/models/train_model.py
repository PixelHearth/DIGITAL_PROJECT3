from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class KNN_MODEL:
    def __init__(self,dataframe,individual_features):
        self.dataframe =dataframe
        self.individual_feature = individual_features
        self.dependent_variable = self.dataframe.iloc[:,0].values
        self.independent_variable = self.dataframe.iloc[:, 1:].values
        self.individual_features  = individual_features.iloc[:,1:].values

    def Select_Variables(self,nb_feature):
        rf_model = RandomForestClassifier(n_estimators=100)
        rf_model.fit(self.independent_variable,self.dependent_variable)
        feature_importances = rf_model.feature_importances_
        importances_df = pd.DataFrame({'Feature': self.dataframe.iloc[:, 1:].columns, 'Importance': feature_importances})

        # Trier les caractéristiques par importance (du plus important au moins important)
        importances_df = importances_df.sort_values(by='Importance', ascending=False)

        # Créer le graphique à barres
        plt.figure(figsize=(10, 6))
        plt.bar(importances_df['Feature'], importances_df['Importance'], color='b')
        plt.xlabel('Caractéristique')
        plt.ylabel('Importance')
        plt.title('Importance des Caractéristiques avec un modèle Random Forest')
        plt.xticks(rotation=45)  # Rotation des étiquettes pour une meilleure lisibilité
        plt.tight_layout()

        # Afficher le pourcentage total d'importance représenté par les caractéristiques les plus importantes
        total_importance = importances_df['Importance'].sum()
        top_features_importance = importances_df.iloc[:nb_feature]['Importance'].sum()  # Par exemple, en prenant les 3 premières caractéristiques
        percentage = (top_features_importance / total_importance) * 100
        plt.annotate(f"Top {nb_feature} Features: {percentage:.2f}%", xy=(0.5, 0.9), xycoords='axes fraction')
        plt.show() 
    def k_neighbors(self):
        """ création d'un algorithme de k_neighbors sur les données properties
        parameter "dataframe", est le dataframe de l'ademe nettoyé
        """
        #entrainement
        neigh = KNeighborsClassifier(n_neighbors=5)
        #entrainement des données
        neigh.fit(self.independent_variable,self.dependent_variable)
        #prédiction
        prediction = neigh.predict(self.individual_features)
        score = neigh.score(self.independent_variable, self.dependent_variable)
        print(f"Précision du modèle : {score}")
    
        #restitution d'un dataframe
        self.independante_variable = self.individual_features.flatten()
        result = np.concatenate([prediction, self.independante_variable])
        dataframe_decoded = pd.DataFrame(result).transpose()
        return dataframe_decoded

