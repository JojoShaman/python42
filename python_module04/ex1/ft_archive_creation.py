import sys
from typing import IO

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit()
    try:
        file_name = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{file_name}'")
        file: IO = open(file_name, 'r')
        content = file.read()
        file.close()
        print("---\n\n" + content + "\n\n---")
        print(f"File '{file_name}' closed.\n")
        print("Transform data:\n---\n")
        new_content = '\n'.join(line + '#' for line in content.split('\n'))
        print(new_content)
        print("\n---")
        file_name = input("Enter new file name (or empty): ")
        if not file_name:
            print("Not saving data.")
            sys.exit()
        new_file: IO = open(file_name, 'w')
        print(f"Saving data to '{file_name}'")
        new_file.write(new_content)
        new_file.close()
        print(f"Data saved in file '{file_name}'.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}: {e}'")
