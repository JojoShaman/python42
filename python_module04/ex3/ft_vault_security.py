from typing import IO


def secure_archive(file_name: str, mode: str = 'r',
                   content: str = 'content') -> tuple[bool, str]:
    try:
        file: IO = open(file_name, mode)
        if mode == 'r':
            text = file.read()
            print("Using 'secure_archive' "
                  "to read from a regular file:")
        elif mode == 'w':
            file.write(content)
            text = 'Content successfully written to file'
        return (True, text)
    except FileNotFoundError as e:
        print("Using 'secure_archive' to read from a "
              "nonexistent file:")
        return (False, f"{e}")
    except PermissionError as e:
        print("Using 'secure_archive' to read from "
              "an inaccessible file:")
        return (False, f"{e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print(secure_archive('/not/existing/file'), '\n')
    print(secure_archive('/etc/master.passwd'), '\n')
    print(secure_archive('ancient_fragment.txt'), '\n')
    prev_content = secure_archive('ancient_fragment.txt')[1]
    print(secure_archive('new_fragment.txt', 'w', prev_content), '\n')
