def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for test in [0, 1, 2, 3, 4]:
        print(f"Testing operation {test}...")
        try:
            garden_operations(test)
        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested successfully!")


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        100/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 42
    elif operation_number == 4:
        1
    else:
        print("Operation completed successfully")


if __name__ == "__main__":
    test_error_types()
