import pandas as pd


def input_from_console():
    """
    A function for reading the entered text from the console.

    :argument: This function hasn't any argument.

    :return: str. The text that was entered.
    """
    text = input("Please, enter your text: ")
    return str(text)


def read_from_file(input_file):
    """
    This function for reading text from file with using standard python's methods.
    Note:
        If there is no specific file you will get an error about it.

    :argument: input_file:  It's file to read.

    :return: str. Text from file.

    :raise: Function raise a "FileNotFoundError" error if there isn't particular file.
    """

    text = ""
    try:
        with open(input_file) as file:
            file_content = file.read()
            text += file_content
    except FileNotFoundError as a:
        raise FileNotFoundError("File not found: ", a)
    return text


def read_from_file_pandas(input_file):
    """
    This function for reading text from file with using the pandas library.
    Note:
        If there is no specific file you will get an error about it.

    :argument: input_file:  It's file to read.

    :return: str. Text from file.

    :raise: Function raise a "FileNotFoundError" error if there isn't particular file.
    """

    try:
        text = pd.read_csv(input_file)
    except FileNotFoundError as a:
        raise FileNotFoundError("File not found: ", a)
    return text
