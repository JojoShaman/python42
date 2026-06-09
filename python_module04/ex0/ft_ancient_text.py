import sys
from typing import IO

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit()
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file: IO = open(sys.argv[1], 'r')
        print("---\n")
        print(file.read())
        print("\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}: {e}'")
