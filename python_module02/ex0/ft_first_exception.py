def input_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    integer = int(temp_str)
    print(f"Temperature is now {integer}°C\n")


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    for temp in ["25", "abc"]:
        try:
            input_temperature(temp)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
