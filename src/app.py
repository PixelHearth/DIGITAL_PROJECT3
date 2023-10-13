from data.make_dataset import generate_property_data
from models.train_model import k_neighbors
import random

def app():
    properties = generate_property_data(100)
    new_variable = { 
        'Type': "Maison",
        'Surface (m²)': 50,
        'Nombre de pièces': 2,
        'Consommation énergétique (kWh/m²/an)': 80,
        'Émissions de gaz à effet de serre (kgCO2/m²/an)': 30,
        'Type de toiture': "2 Pans",
        'type de revêtement toiture' : "Tuiles en terre cuite",
        'Type de revêtement': 'Béton',
        'Type d\'isolation': 'Laine de verre'
    }
    #! trouver un moyen de convertir les variables string en variables ordinal avec Ordinal encoder
    predict = k_neighbors(properties,new_variable)
    print(predict)
if __name__ == "__main__":
    app()