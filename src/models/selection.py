from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
            
def select_variables(dataframe,individual_features):
    #initialisation des variable

    dependent_variable = dataframe.iloc[:,0]
    independent_variable  = dataframe.iloc[:,1:]
    individual_independante_features  = individual_features.iloc[:,1:]
    rf_model = RandomForestClassifier(n_estimators=100,random_state=42)
    rf_model.fit(independent_variable.values,dependent_variable.values)

    feature_importances = rf_model.feature_importances_
    importances_df = pd.DataFrame({'Feature': dataframe.iloc[:,1:].columns, 'Importance': feature_importances})
    importances_df = importances_df.sort_values(by='Importance', ascending=False)
    selection_dataframe = importances_df[:10]

    
    # restitution des index et des noms des colonnes transformées

    selected_features = selection_dataframe['Feature'].tolist()
    selected_dataframe = pd.concat([dependent_variable, independent_variable[selected_features]],axis = 1)
    selected_new_variable = pd.concat([individual_features.iloc[:,0],individual_independante_features[selected_features]],axis = 1)
    selected_new_variable_col = selected_new_variable.columns
    return selected_dataframe,selected_new_variable,selected_new_variable_col


    
    
    # # Créer le graphique à barres
    # plt.figure(figsize=(10, 6))
    # plt.bar(importances_df['Feature'], importances_df['Importance'], color='b')
    # plt.xlabel('Caractéristique')
    # plt.ylabel('Importance')
    # plt.title('Importance des Caractéristiques dans le Modèle Random Forest')
    # plt.xticks(rotation=45)  # Rotation des étiquettes pour une meilleure lisibilité
    # plt.tight_layout()

    # # Afficher le pourcentage total d'importance représenté par les caractéristiques les plus importantes
    # total_importance = importances_df['Importance'].sum()
    # top_features_importance = importances_df.iloc[:nb_feature]['Importance'].sum()  # Par exemple, en prenant les 3 premières caractéristiques
    # percentage = (top_features_importance / total_importance) * 100
    # plt.annotate(f"Top {nb_feature} Features: {percentage:.2f}%", xy=(0.5, 0.9), xycoords='axes fraction')
    # plt.show()