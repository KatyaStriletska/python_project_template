from app.io import input as input
from app.io import output as output

def main():
    print(input.read_from_file_pandas("data/testFile1.csv"))

    #output.print_text(input.read_from_file_pandas("data/testFile3.csv"))
    output.print_text(input.input_from_console())
    output.write_text_in_file(input.input_from_console(), "data/testFile2")

    print("file ", input.read_from_file("data/testFile1"))

    pass


if __name__ == "__main__":
    main()