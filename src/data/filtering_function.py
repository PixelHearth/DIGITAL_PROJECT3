import pandas as pd

def delete_na(df, column_name):
    """
    This function takes as input a DataFrame and the name of a column.
    It returns a new DataFrame that is the result of removing
    rows containing NaN values in the specified column.

    Parameters:
    - df (pandas DataFrame): The DataFrame to process.
    - column_name (str): The name of the column to base the removal of NaN rows on.

    Returns:
    - pandas DataFrame: The resulting DataFrame after removing rows containing NaN in the specified column.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})
    >>> column_name = 'A'
    >>> df_result = delete_na(df, column_name)
    >>> print(df_result)
       A    B
    0  1.0  5.0
    1  2.0  NaN
    3  4.0  8.0
    """
    # Check if the specified column is present in the DataFrame
    if column_name in df.columns:
        # Use the dropna method to remove rows containing NaN in the specified column
        df_no_na = df.dropna(subset=[column_name])
        return df_no_na
    else:
        print(f"'{column_name}' not in df")
        # If the column is not present, return the original DataFrame
        return df



def replace_value(df, column_name, value_a, value_b):
    """
    This function takes as input a DataFrame, the name of a column, a value to replace (value_a),
    and a replacement value (value_b). It returns a new DataFrame resulting
    from replacing all occurrences of value_a with value_b in the specified column.

    Parameters:
    - df (pandas DataFrame): The DataFrame to process.
    - column_name (str): The name of the column in which to perform the value replacement.
    - value_a (str, float, or int): The value to be replaced.
    - value_b (str, float, or int): The replacement value.

    Returns:
    - pandas DataFrame: The resulting DataFrame after replacing the specified values.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'a', 'c']})
    >>> column_name = 'B'
    >>> value_a = 'a'
    >>> value_b = 'x'
    >>> df_result = replace_value(df, column_name, value_a, value_b)
    >>> print(df_result)
       A  B
    0  1  x
    1  2  b
    2  3  x
    3  4  c
    """
    # Check if the specified column is present in the DataFrame
    if column_name in df.columns:
        # Use the 'replace' method to replace values in the specified column
        df[column_name] = df[column_name].replace({value_a: value_b})
    else:
        print(f"'{column_name}' not in df")

    return df

    
def conditional_fill_na(df):
    """
    Conditional fill missing values in a DataFrame based on the data type of each column.

    For columns of type 'object', fill NaN values with the string 'unknown' ('inconnu' in French).
    For numeric columns, fill NaN values with the mean of the column.

    Args:
        df (pd.DataFrame): The DataFrame to be processed.

    Returns:
        pd.DataFrame: A new DataFrame with missing values filled based on the specified conditions.
    
    Example:
        >>> import pandas as pd
        >>> data = {'col1': [1, 2, None], 'col2': ['a', 'b', None], 'col3': [4.0, 5.0, None]}
        >>> df = pd.DataFrame(data)
        >>> df
           col1 col2  col3
        0   1.0    a   4.0
        1   2.0    b   5.0
        2   NaN  NaN   NaN
        
        >>> df = conditional_fill_na(df)
        >>> df
           col1 col2  col3
        0   1.0    a   4.0
        1   2.0    b   5.0
        2   1.5    inconnu   4.5
    """
    assert isinstance(df, pd.DataFrame), "Input must be a DataFrame"

    for column in df.columns:
        if df[column].dtype == "object":
            # For 'object' columns, fill NaN with the string 'unknown'
            df[column].fillna("unknown", inplace=True)
        else:
            # For numeric columns, fill NaN with the mean of the column
            df[column].fillna(df[column].mean(), inplace=True)

    return df

def convert_object_columns_to_integers(df):
    """
    Converts columns of type 'object' to integers if there is at least one element convertible to an integer inside,
    otherwise returns the unchanged DataFrame.
    
    Objective: Allows removing non-NaN values from a column while retaining maximum information.

    Args:
        df (pd.DataFrame): The DataFrame to be processed.

    Returns:
        pd.DataFrame: A new DataFrame with columns converted to integers, if possible.
    
    Raises:
        AssertionError: If the argument is not of type DataFrame.
        AssertionError: If the DataFrame contains non-NaN values. Use the drop_na_rows function before calling this function.
    
    Example:
        >>> import pandas as pd
        >>> data = {'col1': ['1', 'A', '2'], 'col2': ['a', 'b', 'c']}
        >>> df = pd.DataFrame(data)
        >>> df
          col1 col2
        0    1    a
        1    2    b
        2    3    c
        
        >>> df = convert_object_columns_to_integers(df)
        >>> df
          col1   col2
        0    1    a
        1  NaN    b
        2    3    c
    """
    assert isinstance(df, pd.DataFrame), "Input must be a DataFrame"
    assert df.notnull().all().all(), "No NoneType Allowed, use the drop_na_rows function"

    # Select object columns (ambiguous)
    object_columns = df.select_dtypes(include=['object']).columns

    # Iterate through each column and check elements
    for col in object_columns:
        # Initialize a counter to calculate the number of int or float elements
        count = 0
        list_numeric = []
        list_string = []

        # Iterate through the column
        for element in df[col]:
            try:
                int_value = float(element)
                count += 1
                list_numeric.append(int_value)
                list_string.append(None)
            except ValueError:
                list_numeric.append(None)
                list_string.append(element)
        
        # If there are no numeric elements, keep string values; otherwise, convert to numeric
        if count == 0:
            df[col] = list_string
        else:
            df[col] = list_numeric
            df[col] = df[col].astype(float)

    return df

def separate_columns(df, column_name, new_column_names):
    """
    This function takes as input a DataFrame, the name of a column, and a list of custom column names.
    It creates new columns in the DataFrame based on the names specified in the list.
    Each new column contains binary values indicating the presence of the corresponding substring in the original column.

    Parameters:
    - df (pandas DataFrame): The DataFrame to process.
    - column_name (str): The name of the column to split.
    - new_column_names (list): The list of custom column names to create.

    Returns:
    - pandas DataFrame: The resulting DataFrame after creating the new columns.

    Example:
    >>> df = pd.DataFrame({'Tags': ['python, data', 'data science', 'java', 'python', np.nan]})
    >>> column_name = 'Tags'
    >>> new_column_names = ['python', 'java', 'data']
    >>> df_result = separate_columns(df, column_name, new_column_names)
    >>> print(df_result)
       Tags python  Tags java  Tags data
    0    'python, data'         0         1
    1    'data science'         0         0
    2              'java'         1         0
    3            'python'         0         1
    4                NaN      None      None
    """
    # Check if the specified column is present in the DataFrame
    if column_name in df.columns:
        # Create new empty columns with names specified in the list
        for name in new_column_names:
            df[column_name + ' ' + name] = df[column_name].apply(lambda x: 1 if isinstance(x, str) and name in x else (0 if not pd.isna(x) else None))
        # Remove the original column
        df = df.drop(columns=[column_name])
    else:
        print(f"Column '{column_name}' is not present in the DataFrame.")

    return df

def comma_count(string):
    """
    This function takes as input a string representing a list of modalities.
    It returns the number of modalities in the list (the number of commas + 1) or None if the string is NaN.

    Parameters:
    - string (str): A string representing a list of modalities.

    Returns:
    - int or None: The number of modalities in the list (the number of commas + 1) or None if the string is NaN.

    Example:
    >>> string = "['modality1', 'modality2', 'got it']"
    >>> result = comma_count(string)
    >>> print(result)
    3
    """
    if pd.notna(string):
        return string.count(',') + 1 if isinstance(string, str) else 0
    else:
        return None


def list_to_int(df, column_name):
    """
    This function takes as input a DataFrame and the name of a column containing lists of modalities.
    It replaces the lists with the number of modalities they contain using the comma_count function.

    Parameters:
    - df (pandas DataFrame): The DataFrame to process.
    - column_name (str): The name of the column to convert.

    Returns:
    - pandas DataFrame: The resulting DataFrame after converting lists to the number of modalities.

    Example:
    >>> df = pd.DataFrame({'Modalities': ["['modality1', 'modality2', 'got it']", "['option1', 'option2']", np.nan]})
    >>> column_name = 'Modalities'
    >>> df_result = list_to_int(df, column_name)
    >>> print(df_result)
       Modalities
    0            3
    1            2
    2         None
    """
    if column_name in df.columns:
        # Apply the comma_count function to the specified column
        df[column_name] = df[column_name].apply(comma_count)
    else:
        print(f"Column '{column_name}' is not present in the DataFrame.")

    return df


def select_columns(df, columns_to_keep):
    """
    This function takes as input a DataFrame and a list of column names.
    It returns a new DataFrame containing only the specified columns.

    Parameters:
    - df (pandas DataFrame): The DataFrame to process.
    - columns_to_keep (list): The list of column names to retain in the resulting DataFrame.

    Returns:
    - pandas DataFrame: The resulting DataFrame with only the desired columns.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [True, False, True]})
    >>> columns_to_keep = ['A', 'C']
    >>> df_result = select_columns(df, columns_to_keep)
    >>> print(df_result)
       A     C
    0  1  True
    1  2 False
    2  3  True
    """
    # Check if all specified columns are present in the DataFrame
    columns_in_df = [col for col in columns_to_keep if col in df.columns]
    # Select only the present columns
    df_selected = df[columns_in_df]
    return df_selected


def switch_first_column(df, column_name):
    """
    This function takes as input a DataFrame and the name of a column.
    It returns a new DataFrame with the specified column moved to the first position.

    Parameters:
    - df (pandas DataFrame): The DataFrame to process.
    - column_name (str): The name of the column to move to the first position.

    Returns:
    - pandas DataFrame: The resulting DataFrame with the column moved to the first position.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [True, False, True]})
    >>> column_name = 'B'
    >>> df_result = switch_first_column(df, column_name)
    >>> print(df_result)
         B  A     C
    0    'a'  1  True
    1    'b'  2 False
    2    'c'  3  True
    """
    if column_name in df.columns:
        # List of column names
        columns = list(df.columns)
        
        # Remove the column from the list
        columns.remove(column_name)
        
        # Insert the column at the beginning of the list
        columns.insert(0, column_name)
        
        # Reorganize the DataFrame according to the new column sequence
        df = df[columns]
        
        return df
    else:
        print(f"Column '{column_name}' is not present in the DataFrame.")
        return df