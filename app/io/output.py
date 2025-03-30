def output_to_console(text):
    """
    Prints text to the console.

    Args:
        text (str): The text to print to the console.
    """
    print(text)


def output_to_file(file_path, text):
    """
    Writes text to a file using built-in Python functionality.

    Args:
        file_path (str): The path to the file to write.
        text (str): The text to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(text)
