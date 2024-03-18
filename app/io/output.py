
def print_text(input):
    """
    Function for enter text from the console
    :return: This function returns text which input user from console.
    examples:
    """
    print(input)


def write_text_in_file(inputText, fileName):
    """

    :param fileName:
    :param inputText:
    :return:
    """
    try:
        with open(fileName, 'w') as file:
            file.write(inputText)
    except FileNotFoundError as a:
        print("File not found: ", a)
    print(f"Input text was succeeded written in file: {fileName}!")