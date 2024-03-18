import pandas as pd


def input_from_console():
    """
    A function for reading the entered text from the console.
    :return: str. The text that was entered.
    """
    text = input("Please, enter your text: ")
    return str(text)


def read_from_file(inputFile):
    """
    This function for reading text from file with using standard python's methods.
    Note:
        If there is no specific file you will get an error about it.
    :param inputFile:  It's file to read.
    :return: str. Text from file.
    """

    text = ""
    try:
        with open(inputFile) as file:
            file_content = file.read()
            text += file_content
    except FileNotFoundError as a:
        raise FileNotFoundError("File not found: ", a)
    return text


def read_from_file_pandas(inputFile):
    """
    This function for reading text from file with using the pandas library.
    Note:
        If there is no specific file you will get an error about it.
    :param inputFile:  It's file to read.
    :return: str. Text from file.
    """

    try:
        text = pd.read_csv(inputFile)
    except FileNotFoundError as a:
        raise FileNotFoundError("File not found: ", a)
    return text
