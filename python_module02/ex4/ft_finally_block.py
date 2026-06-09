class GardenError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"""Invalid plant name to water: {plant_name}
.. ending tests and returning to main""")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    my_plants = [
        ["Tomato", "Lettuce", "Carrots"],
        ["Tomato", "lettuce", "carrots"]]
    watering_system = ["valid", "invalid"]
    index = 0
    for i in watering_system:
        print(f"Testing {i} plants...")
        print("Opening watering system")
        try:
            water_plant(my_plants[index][0])
            water_plant(my_plants[index][1])
            water_plant(my_plants[index][2])
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            return
        finally:
            print("Closing watering system\n")
        index += 1


if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")
