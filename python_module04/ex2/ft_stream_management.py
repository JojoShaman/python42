import sys
from typing import IO


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit()
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file: IO = open(sys.argv[1], 'r')
        content = file.read()
        file.close()
        print("---\n\n" + content + "\n\n---")
        print(f"File '{sys.argv[1]}' closed.\n")
        new_content = '\n'.join(line + '#' for line in content.split('\n'))
        print("Transform data:\n---\n")
        # for line in new_content:
        print(new_content)
        print("\n---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        file_name = sys.stdin.readline().rstrip('\n')
        if not file_name:
            print("Not saving data.")
            sys.exit()
        try:
            new_file: IO = open(file_name, 'w')
        except PermissionError as e:
            sys.stderr.write(
                f"[STDERR] Error opening file '{file_name}: {e}'\n")
            sys.stdout.write("Data not saved.\n")
            sys.exit()
        print(f"Saving data to '{file_name}'")
        new_file.write(new_content)
        new_file.close()
        print(f"Data saved in file '{file_name}'.")
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{sys.argv[1]}: {e}'\n")
