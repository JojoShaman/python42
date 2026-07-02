from ex1 import HealingCreatureFactory, TransformCreatureFactory


def healing_creature_factory() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    creature = HealingCreatureFactory()
    base = creature.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = creature.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def transform_creature_factory() -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    creature = TransformCreatureFactory()
    base = creature.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.revert())
    print(" evolved:")
    evolved = creature.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.revert())


if __name__ == "__main__":
    healing_creature_factory()
    transform_creature_factory()
