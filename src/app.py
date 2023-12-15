from data.clean import clean_df
from data.preprocessing import CustomProcessing, ScalerProcessor
from models.train_model import Models
from models.selection import select_features
from visualization.importance_feature_graph import plot_feature_importance
from data.make_dataset import *

def app():
    # Import database
    properties = clean_df("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/src/data/database/df_clean.csv")
    
    # Import customer desc
    customer = importation_excel("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/src/formulaire_DPE.xlsm", "Source")
    
    # Instance StandardScaler for the models and run
    ScalerProcessor(properties,customer).run_processing_pipeline()
    
    # Instance of the processing framework and data training on properties for encoding
    cpp_p_selection = CustomProcessing(properties)
    properties = cpp_p_selection.fit_transform(properties)
    
    # Selection of number of features, important variables, encoding must have been done before
    nb_features = 15
    properties_selected, importance = select_features(properties, nb_features)
    
    # Plot of features importances
    # plot_feature_importance(importance, nb_features)
    
    # Instance and training of k_neighbors on the encoded data
    knn_model = Models(properties_selected, customer)
    
    # Make the K Nearest Neighbors
    proba = knn_model.k_neighbors()
    
    # Write data on txt file
    with open("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/src/data/database/prediction.txt", 'w') as fichier:
        fichier.write(str(proba))

if __name__ == "__main__":
    app()
