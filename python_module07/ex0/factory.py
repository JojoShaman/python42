from abc import ABC, abstractmethod
from .creatures import Creature
from .creatures import Flameling
from .creatures import Pyrodon
from .creatures import Aquabub
from .creatures import Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Flameling('Flameling', 'Fire'))

    def create_evolved(self) -> Creature:
        return (Pyrodon('Pyrodon', 'Fire/Flying'))


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Aquabub('Aquabub', 'Water'))

    def create_evolved(self) -> Creature:
        return (Torragon('Torragon', 'Water'))
