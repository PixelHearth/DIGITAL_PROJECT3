import pandas as pd
import pickle

def stock_pickle_csv(path_in:str, path_out:str):

    """
    Create a pickle with the given csv file 

    var:
    path_in (str): path of the given csv file
    path_out (str): path of the returned csv file
    """

    # opening data
    df = pd.read_csv(path_in, sep = ",")

    # writing the pickle with the csv
    with open(path_out, "wb") as file_pickle:
        pickle.dump(df, file_pickle)

def open_pkl(path_in:str):
    # test opening pickle
    with open(path_in, "rb") as file2:
        return(pickle.load(file2))
