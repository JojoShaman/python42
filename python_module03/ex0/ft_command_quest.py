import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])

    if len(sys.argv) > 1:
        i = 1
        print("Arguments received:", len(sys.argv) - 1)
        for index in sys.argv[1:]:
            print(f"Argument {i}:", index)
            i += 1
    else:
        print("No arguments provided!")

    print("Total arguments:", len(sys.argv), "\n")
