from data.preprocessing import CustomProcessing
from models.train_model import Models
from models.selection import select_features
from visualization.importance_feature_graph import plot_feature_importance
from data.clean import clean_df
from data.make_dataset import importation_excel
import pandas as pd
import time
import os
import numpy as np
def app():
    # Calculate the start time
    start = time.time()

    # Import database
    properties = clean_df("src/data/database/df_clean.csv")
    # new_variable = importation_excel("src/formulaire.xlsm", "Source")

    # Instance of the processing framework and data training on properties for encoding
    cpp_p_selection = CustomProcessing(properties)
    properties = cpp_p_selection.fit_transform(properties)

    # Selection of important variables, encoding must have been done beforehand
    nb_features = 8
    columns_important, importance = select_features(properties, nb_features)

    plot_feature_importance(importance, nb_features)

    col = cpp_p_selection.column_selection(columns_important)

    cpp_p_selection.inverse_transform(properties)

    properties.to_csv("src/data/database/try.csv")
    if 'classe_bilan_dpe' in col:
    # Sélectionnez toutes les colonnes, mais avec 'classe_bilan_dpe' en premier
        ordered_columns = ['classe_bilan_dpe'] + [col for col in col if col != 'classe_bilan_dpe']

    # Réorganisez les colonnes du DataFrame
        properties_selected = properties[ordered_columns]
    
    new_variable = properties_selected.sample(1)
    print(new_variable)
    # Instance of the processing framework and data training on properties for encoding after selection
    cpp_kneigh = CustomProcessing(properties_selected)

    properties_selected = cpp_kneigh.fit_transform(properties_selected)
    new_variable = cpp_kneigh.transform(new_variable)
    # Create the graph of importances in the selection model

    # Instance and training of k_neighbors on the encoded data
    knn_model = Models(properties_selected, new_variable)
    print(new_variable)
    # knn_model.standardize_training_data()
    # knn_model.standardize_test_data()
    best_k = knn_model.metric_knn()
    individual,proba = knn_model.k_neighbors(best_k)
    # individual.columns = new_variable.columns

    # Restoration of a human-readable dataframe
    # Predicted value of k_neighbors
    cpp_kneigh.inverse_transform(individual)
    individual = individual.iloc[:, 0].values.flatten()[0]
    file_path = os.path.join('src/data/database/', 'prediction.txt')

    # Open the file in write mode (w), if it does not exist, it will be created
    with open(file_path, 'w') as text_file:
        # Write the string to the file
        text_file.write(str(individual))
        text_file.write(np.array2string(proba))

    print(individual)
    
    # Calculate the total execution time
    end = time.time()
    print("Execution time: ", round(end - start, 2), "seconds") 
    return individual
    
if __name__ == "__main__":
    app()
