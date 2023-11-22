from data.preprocessing import CustomPreprocessor
from models.train_model import Models
from models.selection import select_features
from visualization.importance_feature_graph import plot_feature_importance
from data.clean import clean
from data.make_dataset import importation_excel
import pandas as pd
import time
import os
from sklearn.preprocessing import MinMaxScaler
def app():
    # Calculate the start time
    start = time.time()

    # Import database
    properties = clean("src/data/database/Base_clean.csv")
    
    new_variable = importation_excel("src/formulaire.xlsm", "Source")

    # Instance of the processing framework and data training on properties for encoding
    cpp_p_selection = CustomPreprocessor(properties)
    cpp_p_selection.fit()

    # Encode variables in both databases
    cpp_p_selection.transform(properties)

    # Selection of important variables, encoding must have been done beforehand
    nb_features = 10
    properties, importance = select_features(properties, nb_features)
    cpp_p_selection.inverse_transform(properties)

    # Instance of the processing framework and data training on properties for encoding after selection
    cpp_kneigh = CustomPreprocessor(properties)
    cpp_kneigh.fit()

    cpp_kneigh.transform(properties)
    cpp_kneigh.transform(new_variable)

    # Create the graph of importances in the selection model
    plot_feature_importance(importance, nb_features)

    # Instance and training of k_neighbors on the encoded data
    individual = Models(properties, new_variable).k_neighbors()
    individual.columns = new_variable.columns

    # Restoration of a human-readable dataframe
    # Predicted value of k_neighbors
    cpp_kneigh.inverse_transform(individual)
    individual = individual.iloc[:, 0].values.flatten()[0]
    file_path = os.path.join('src/data/database', 'prediction.txt')

    # Open the file in write mode (w), if it does not exist, it will be created
    with open(file_path, 'w') as text_file:
        # Write the string to the file
        text_file.write(str(individual))

    print(individual)
    
    # Calculate the total execution time
    end = time.time()
    print("Execution time: ", round(end - start, 2), "seconds") 
    return individual
    
if __name__ == "__main__":
    app()
