import pandas as pd


def print_text(output_data):
    """
    Function for entering text from the console. It printed the text, that was come as argument.

    :argument: output_data(Any types). It's data to be printed in console.

    :return: None: This function return nothing.
    """
    print(str(output_data))
    return None


def write_text_in_file(output_data, file_name):
    """
    Function to writing text in file. After the execution of this function, there will be a message on the console about
    the successful completion of the action.

    :argument:
            output_data (Any types). It's data to be written in input file.
            file_name (file). It's file in which will be written input data. If there isn't particular file, it will be
                                created.

    :return: None. This function returns nothing.
    """
    with open(file_name, 'w') as file:
        file.write(str(output_data))

    print(f"Input text was succeeded written in file: {file_name}!")
    return None


def write_text_in_file_pandas(output_data, file_name):
    """
    Function to writing text in file with extension 'csv' with using library pandas. After the execution of this
    function, there will be a message on the console about the successful completion of the action.

    :argument:
            output_data (Any types). It's data to be written in input file.
            file_name (file). It's file in which will be written input data. If there isn't particular file, it will be
                                created. File must be with extension 'csv'!

    :return: None. This function returns nothing.
    """
    df = pd.DataFrame(output_data)

    # Write the DataFrame to a CSV file without including the date
    df.to_csv(file_name, index=False, date_format='')
    print(f"Input text was succeeded written in file: {file_name}!")
    return None
