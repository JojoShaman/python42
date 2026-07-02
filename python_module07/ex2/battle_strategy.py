from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability
from ex1.capabilities import HealCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())


class AgressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, TransformCapability))

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            creature_type = cast(TransformCapability, creature)
            print(creature_type.transform())
            print(creature.attack())
            print(creature_type.revert())
        else:
            raise Exception("Battle error, aborting tournament: "
                            f"Invalid Creature '{creature._name}' "
                            "for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (isinstance(creature, HealCapability))

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            creature_type = cast(HealCapability, creature)
            print(creature.attack())
            print(creature_type.heal())
        else:
            raise Exception("Battle error, aborting tournament: "
                            f"Invalid Creature '{creature._name}' "
                            "for this defensive strategy")
