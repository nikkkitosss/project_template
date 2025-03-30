import pandas as pd

def input_from_console():
    """
    Reads text from the console.
    Asks the user to input some text and returns it as a string.
    """
    user_input = input("Enter some text: ")
    return user_input


def input_from_file(file_path):
    """
    Reads text from a file using built-in Python functionality.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The content of the file as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()


def input_from_file_pandas(file_path):
    """
    Reads text from a file using the pandas' library.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        pandas.DataFrame: The content of the file as a dataframe.
    """
    return pd.read_csv(file_path)
