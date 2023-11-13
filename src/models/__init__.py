def __init__(self,dataframe,individual_features):
        self.dataframe =dataframe
        self.individual_feature = individual_features
        self.dependent_variable = self.dataframe.iloc[:,0]
        self.independent_variable = self.dataframe.iloc[:,1:]
        self.individual_independante_features  = individual_features.iloc[:,1:]