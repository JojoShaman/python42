from ex0.factory import CreatureFactory
from .creatures import Sproutling
from .creatures import Bloomelle
from .creatures import Shiftling
from .creatures import Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return (Sproutling('Sproutling', 'Grass'))

    def create_evolved(self) -> Bloomelle:
        return (Bloomelle('Bloomelle', 'Grass/Fairy'))


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return (Shiftling('Shiftling', 'Normal'))

    def create_evolved(self) -> Morphagon:
        return (Morphagon('Morphagon', 'Normal/Dragon'))
