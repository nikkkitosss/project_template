from app.io.input import input_from_console, input_from_file, input_from_file_pandas
from app.io.output import output_to_console, output_to_file


def main():
    console_text = input_from_console()
    output_to_console(f"Console Input: {console_text}")
    output_to_file("console_output.txt", f"Console Input: {console_text}")

    file_text = input_from_file("input.txt")
    output_to_console(f"File Input: {file_text}")
    output_to_file("file_output.txt", f"File Input: {file_text}")

    try:
        file_df = input_from_file_pandas("data.csv")
        output_to_console(f"Pandas File Input:\n{file_df}")
        output_to_file("pandas_output.txt", f"Pandas File Input:\n{file_df}")
    except Exception as e:
        output_to_console(f"Error reading file with pandas: {e}")
        output_to_file("pandas_error_output.txt", f"Error reading file with pandas: {e}")


if __name__ == "__main__":
    main()
