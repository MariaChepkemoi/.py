def read_file(filename):
    """Reads the content of the file."""
    try:
        with open(filename, "r") as file:
            return file.read()  # Return the file's content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def write_file(filename, content):
    """Writes modified content to a new file."""
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"Modified content has been written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to '{filename}': {e}")

def main():
    """Main program logic."""
    input_file = input("Enter the filename to read: ")
    content = read_file(input_file)
    
    if content:
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Ask for the output filename
        output_file = input("Enter the filename to write the modified content: ")
        write_file(output_file, modified_content)

if __name__ == "__main__":
    main()
read_file