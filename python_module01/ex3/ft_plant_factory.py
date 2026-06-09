class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = round(height, 2)
        self.age = age

    def show(self) -> str:
        return (f"{self.name}: {round(self.height, 2)}cm, {self.age} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 200.0, 265)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)
    my_plants = [rose, oak, cactus, sunflower, fern]
    for plants in my_plants:
        print(f"Created: {plants.show()}")


if __name__ == "__main__":
    ft_plant_factory()
