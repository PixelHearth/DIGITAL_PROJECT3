from data.preprocessing import CustomProcessing
from models.train_model import Models
from models.selection import select_features
from visualization.importance_feature_graph import plot_feature_importance

from data.clean import clean_df
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
import os
import numpy as np
import xlwings as xw

def app():
    # Calculate the start time
    start = time.time()

    # Import database
    properties = clean_df("src/data/database/df_clean.csv")
    
    # Import customer desc
    # new_variable = importation_excel("src/formulaire.xlsm", "Source")

    # Instance of the processing framework and data training on properties for encoding
    cpp_p_selection = CustomProcessing(properties)
    numeric_columns = properties.select_dtypes(include=['number']).columns

    # Instance StandardScaler for the models
    scaler = StandardScaler()

    # Apply scaler to numeric columns
    properties[numeric_columns] = scaler.fit_transform(properties[numeric_columns])
    properties = cpp_p_selection.fit_transform(properties)

    # Selection of number of features, important variables, encoding must have been done before
    nb_features = 15
    columns_important, importance = select_features(properties, nb_features)

    # Plot of features importances
    plot_feature_importance(importance, nb_features)

    # Get columns keeped by select features
    col = cpp_p_selection.column_selection(columns_important)
    # Inverse transform the properties 
    cpp_p_selection.inverse_transform(properties)

    # Select col in initial properties with col selected by the RandomForest
    if 'classe_bilan_dpe' in col:
        # Keep classe_bilan_dpe and col in randomforest
        ordered_columns = ['classe_bilan_dpe'] + [col for col in col if col != 'classe_bilan_dpe']

        # copy property with new cols
        properties_selected = properties[ordered_columns]
    
    customer = properties_selected.sample(1)
    
    # Instance processing framework and data training on properties for encoding after selection
    cpp_kneigh = CustomProcessing(properties_selected)

    #fit and transform training dataset and customer dataset
    properties_selected = cpp_kneigh.fit_transform(properties_selected)
    customer = cpp_kneigh.transform(customer)
    # Create the graph of importances in the selection model

    # Instance and training of k_neighbors on the encoded data
    knn_model = Models(properties_selected, customer)
    
    # get k optimal
    best_k = knn_model.metric_knn()
    individual,proba = knn_model.k_neighbors(best_k)

    # Restoration of a human-readable dataframe
    # Predicted value of k_neighbors
    cpp_kneigh.inverse_transform(individual)
    
    file_path = os.path.join('src/data/database/', 'prediction.txt')

    # Open the file in write mode (w), if it does not exist, it will be created
    with open(file_path, 'w') as text_file:
        # Write the string to the file
        text_file.write(str(proba))

    try:

        app = xw.App(visible=True)
        workbook = app.books.open("src/formulaire.xlsm")

        # Sélectionner la feuille source
        feuille_source = workbook.sheets['Source']

        # Ajouter les classes à partir de la cellule A5
        for index, donnee in enumerate(proba):
            classe = donnee['classe']
            feuille_source.range((5, index + 1)).value = classe

        # Ajouter les probabilités à partir de la cellule A6
        for index, donnee in enumerate(proba):
            probabilite = donnee['probabilite']
            feuille_source.range((6, index + 1)).value = probabilite
        # Save the workbook
        workbook.save('src/formulaire.xlsm')
        print("Workbook saved successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Calculate the total execution time
    end = time.time()
    print("Execution time: ", round(end - start, 2), "seconds") 
    return individual
    
if __name__ == "__main__":
    app()
