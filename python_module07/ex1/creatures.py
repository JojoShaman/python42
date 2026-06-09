from .capabilities import HealCapability
from .capabilities import TransformCapability
from ex0.creatures import Creature


class Sproutling(HealCapability, Creature):
    def heal(self):
        return (f"{self._name} heals itself for a small amount")

    def attack(self):
        return (f"{self._name} uses Vine Whip!")


class Bloomelle(HealCapability, Creature):
    def heal(self):
        return (f"{self._name} heals itself and others for a large amount")

    def attack(self):
        return (f"{self._name} uses Petal Dance!")


class Shiftling(TransformCapability, Creature):
    def transform(self):
        return (f"{self._name} shifts into a sharper form!")

    def attack(self):
        return (f"{self._name} performs a boosted strike!")

    def revert(self):
        return (f"{self._name} returns to normal.")


class Morphagon(TransformCapability, Creature):
    def transform(self):
        return (f"{self._name} morphs into a dragonic battle form!")

    def attack(self):
        return (f"{self._name} unleashes a devastating morph strike!")

    def revert(self):
        return (f"{self._name} stabilizes its form.")
