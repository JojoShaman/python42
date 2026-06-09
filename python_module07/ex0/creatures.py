from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self._name = name
        self._type = type

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        return (f"{self._name} is a {self._type} type creature")


class Flameling(Creature):
    def attack(self):
        return (f"{self._name} uses Ember!")


class Pyrodon(Creature):
    def attack(self):
        return (f"{self._name} uses Flamethrower!")


class Aquabub(Creature):
    def attack(self):
        return (f"{self._name} uses Water Gun!")


class Torragon(Creature):
    def attack(self):
        return (f"{self._name} uses Hydro Pump!")
