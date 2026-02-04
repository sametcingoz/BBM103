import sys
import os

def reading_file(input_file):
    try:
        with open(input_file, "r") as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found error!")
        sys.exit(1)
    except Exception as error_one:
        print(f"The input file '{input_file}' could not be read error:", error_one)
        sys.exit(1)

def matrix_multiplication(matrix1, matrix2):
    try:
        result = []
        for i in range(len(matrix1)):
            row_result = []
            for j in range(len(matrix2[0])):
                cell_result = 0
                for k in range(len(matrix2)):
                    cell_result += matrix1[i][k] * matrix2[k][j]
                row_result.append(cell_result)
            result.append(row_result)
        return result
    except Exception as error_two:
        print("Matrix multiplication error:", error_two)
        sys.exit(1)

def map_letters_to_numbers():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_to_number = {}
    for index, letter in enumerate(alphabet, start=1):
        letter_to_number[letter] = index
    return letter_to_number

def generate_binary_list(file_content):
    try:
        binary_list = []
        letter_to_number_dict = map_letters_to_numbers()

        return binary_list
    except Exception as error_three:
        print("Binary list generation error:", error_three)
        sys.exit(1)

def read_key_file(key_file):
    try:
        with open(key_file, "r") as file:
            key_content = file.read()
        return key_content.strip()
    except FileNotFoundError:
        print(f"Key file '{key_file}' not found error!")
        sys.exit(1)
    except Exception as error_four:
        print(f"Key file '{key_file}' could not be read error:", error_four)
        sys.exit(1)

def process_key_file(key_content):
    try:
        if not key_content:
            print("Key file is empty error!")
            sys.exit(1)

        key_matrix = [list(map(int, row.split(','))) for row in key_content.split('\n')]
        return key_matrix
    except Exception as error_five:
        print("Key file processing error:", error_five)
        sys.exit(1)

def write_to_file(output_file, content):
    try:
        with open(output_file, "w") as file:
            file.write(content)
    except FileNotFoundError:
        print(f"Output file '{output_file}' could not be written error: Output file path does not exist or is write-protected!")
        sys.exit(1)
    except Exception as error_six:
        print(f"Output file '{output_file}' could not be written error:", error_six)
        sys.exit(1)

def main():
    try:
        if len(sys.argv) != 5:
            print("Parameter number error: Usage: python3 assignment4.py enc keyfile.txt inputfile.txt outputfile.txt")
            sys.exit(1)
        if sys.argv[1] != 'enc':
            print("Operation type error: First parameter should be 'enc'.")
            sys.exit(1)

        key_file = sys.argv[2]
        input_file = sys.argv[3]
        output_file = sys.argv[4]

        if not os.path.exists(key_file):
            print(f"Key file '{key_file}' not found error!")
            sys.exit(1)

        if not os.path.exists(input_file):
            print(f"Input file '{input_file}' not found error!")
            sys.exit(1)

        key_content = read_key_file(key_file)
        key_matrix = process_key_file(key_content)

        file_content = reading_file(input_file)
        if not file_content:
            print("Input file is empty error!")
            sys.exit(1)

        binary_list = generate_binary_list(file_content)

        results = []
        for binary_combination in binary_list:
            result = matrix_multiplication(key_matrix, [binary_combination])
            results.append(result)

        output_content = ', '.join(map(str, results))
        write_to_file(output_file, output_content)
        print(f"Result written to {output_file}.")
    except Exception as main_error:
        print("An unexpected error occurred:", main_error)
        sys.exit(1)

if __name__ == "__main__":
    main()
