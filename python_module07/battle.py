from ex0 import CreatureFactory, AquaFactory, FlameFactory


def testing_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    creature = factory.create_evolved()
    print(creature.describe())
    print(creature.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_evolved()
    print(creature1.describe())
    print("  vs.")
    print(creature2.describe())
    print("  fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    testing_factory(FlameFactory())
    print(" ")
    testing_factory(AquaFactory())
    print(" ")
    battle(FlameFactory(), AquaFactory())
