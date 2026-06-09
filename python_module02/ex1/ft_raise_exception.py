def input_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    integer = int(temp_str)
    if integer >= 0 and integer <= 40:
        print(f"Temperature is now {integer}°C\n")
    elif integer > 40:
        raise ValueError(f"{integer}°C is too hot for plants (max 40°C)")
    elif integer < 0:
        raise ValueError(f"{integer}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    print("=== Garden Temperature Checker===\n")
    for temp in ["25", "abc", "100", "-50"]:
        try:
            input_temperature(temp)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
