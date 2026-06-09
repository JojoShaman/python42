from ex1 import HealingCreatureFactory, TransformCreatureFactory


def healing_creature_factory() -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    creature = HealingCreatureFactory().create_base()
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())
    print(" evolved:")
    creature = HealingCreatureFactory().create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def transform_creature_factory() -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    creature = TransformCreatureFactory().create_base()
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.revert())
    print(" evolved:")
    creature = TransformCreatureFactory().create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.revert())


if __name__ == "__main__":
    healing_creature_factory()
    transform_creature_factory()
