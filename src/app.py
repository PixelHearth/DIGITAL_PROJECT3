import time

from sklearn.preprocessing import StandardScaler

from data.clean import clean_df
from data.preprocessing import CustomProcessing
from models.train_model import Models
from models.selection import select_features
from visualization.importance_feature_graph import plot_feature_importance
from data.make_dataset import *

def app():
    # Calculate the start time
    start = time.time()

    # Import database
    properties = clean_df("src/data/database/df_clean.csv")
    
    # Import customer desc
    customer = importation_excel("src/formulaire.xlsm", "Source")
    
    # Instance StandardScaler for the models
    scaler = StandardScaler()
    numerous = properties.select_dtypes(include=['number']).columns
    # Apply scaler to numeric columns
    properties[numerous] = scaler.fit_transform(properties[numerous])
    # customer[customer.select_dtypes(include=['number']).columns] = scaler.fit_transform(customer.select_dtypes(include=['number']).columns)
    
    # Instance of the processing framework and data training on properties for encoding
    cpp_p_selection = CustomProcessing(properties)
    properties = cpp_p_selection.fit_transform(properties)

    # Selection of number of features, important variables, encoding must have been done before
    nb_features = 15
    columns_important, importance = select_features(properties, nb_features)
    print(columns_important)
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
    # Instance and training of k_neighbors on the encoded data
    knn_model = Models(properties_selected, customer)
    
    # get k optimal
    best_k = knn_model.metric_knn()
    
    # Make the K Nearest Neighbors
    individual,proba = knn_model.k_neighbors(best_k)
    
    # Restoration of a human-readable dataframe
    # Predicted value of k_neighbors
    cpp_kneigh.inverse_transform(individual)

    export_excel(proba,"src/formulaire.xlsm", "Source")
    
    # Calculate the total execution time
    end = time.time()
    print("Execution time: ", round(end - start, 2), "seconds") 
    return individual
    
if __name__ == "__main__":
    app()
