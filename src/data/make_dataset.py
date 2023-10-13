# -*- coding: utf-8 -*-




def generate_property_data(num_rows):
    """génération d'un dataset crée aléatoirement pour commencer les modèles 
    """
    import pandas as pd
    import random
    dpe = ["A","B","C","D","E","F","G"]
    property_types = ['Maison', 'Appartement']
    surface = [random.randint(20, 250) for _ in range(num_rows)]
    num_rooms = [random.randint(1, 8) for _ in range(num_rows)]
    energy_consumption = [random.randint(70, 250) for _ in range(num_rows)]
    emissions = [random.randint(15, 60) for _ in range(num_rows)]
    roof_types = ['Plat', '2 Pans', 'Mansardé', 'Monopente', '4 pans', 'toit pavillon']
    roof_material = ["Tuiles en terre cuite","Tuiles en terre cuite","Ardoises artificielles","Ardoises naturelles","Toiture en chaume","Toiture en zinc"]
    siding_types = ['Brique', 'Enduit', 'Bois', 'Béton', 'Pierre']
    insulation_types = ['Laine de verre', 'Polystyrène expansé', 'Laine de roche', 'Laine de bois', 'Polyuréthane']

    data = {
        "Dpe" : [random.choice(dpe) for _ in range(num_rows)],
        'Type': [random.choice(property_types) for _ in range(num_rows)],
        'Surface (m²)': surface,
        'Nombre de pièces': num_rooms,
        'Consommation énergétique (kWh/m²/an)': energy_consumption,
        'Émissions de gaz à effet de serre (kgCO2/m²/an)': emissions,
        'Type de toiture': [random.choice(roof_types) for _ in range(num_rows)],
        'type de revêtement toiture' : [random.choice(roof_material) for _ in range(num_rows)],
        'Type de revêtement': [random.choice(siding_types) for _ in range(num_rows)],
        'Type d\'isolation': [random.choice(insulation_types) for _ in range(num_rows)]
    }

    dataframe_property = pd.DataFrame(data)
    return dataframe_property