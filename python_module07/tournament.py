from ex2 import BattleStrategy, NormalStrategy
from ex2 import AgressiveStrategy, DefensiveStrategy
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(opponents)):
        creature, strategy = opponents[i]
        for j in range(i + 1, len(opponents)):
            creature_2, strategy_2 = opponents[j]
            print("\n* Battle *")
            print(f"{creature.create_base().describe()}\n" +
                  "  vs.\n" +
                  f"{(creature_2.create_base()).describe()}")
            print(" now fight!")
            try:
                strategy.act(creature.create_base())
                strategy_2.act(creature_2.create_base())
            except Exception as e:
                print(e)


if __name__ == "__main__":
    basic: list = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ]
    error: list = [
        (FlameFactory(), AgressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
        ]
    multiple: list = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AgressiveStrategy())
        ]
    print("Tournament 0 (basic)\n",
          "[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***\n" +
          f"{len(basic)} opponents involved")
    battle(basic)
    print("\nTournament 1 (error)\n",
          "[ (Flameling+Agressive), (Healing+Defensive) ]")
    print("*** Tournament ***\n" +
          f"{len(error)} opponents involved")
    battle(error)
    print("\nTournament 2 (multiple)\n",
          "[ (Aquabub+Normal), (Healing+Defensive), (Transform+Agressive) ]")
    print("*** Tournament ***\n" +
          f"{len(multiple)} opponents involved")
    battle(multiple)
