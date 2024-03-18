from app.io import input as input
from app.io import output as output


def main():

    # read from console output to console
    output.print_text(input.input_from_console())
    # read from file and output in console
    output.print_text(input.read_from_file("data/testFile1"))
    # read from file (using pandas) in console
    output.print_text(input.read_from_file_pandas("data/testFile2.csv"))

    # read from console output to file
    output.write_text_in_file(input.input_from_console(), "data/testFile3")
    # read from file and output in file
    output.write_text_in_file(input.read_from_file("data/testFile1"), "data/testFile4")
    # read from file (using pandas) in file
    output.write_text_in_file(input.read_from_file_pandas("data/testFile2.csv"), "data/testFile5")

    # read from file (using pandas) in file with using pandas library
    output.write_text_in_file_pandas(input.read_from_file_pandas("data/testFile2.csv"), "data/testFile5.csv")
    pass


if __name__ == "__main__":
    main()
