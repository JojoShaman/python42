import operator
from functools import reduce
from functools import partial
from functools import lru_cache
from functools import singledispatch
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation not in ["add", "multiply", "max", "min"]:
        raise ValueError(f"Unknown operation: '{operation}'")
    if not spells:
        return 0
    if operation == "add":
        total = reduce(operator.add, spells)
    elif operation == "multiply":
        total = reduce(operator.mul, spells)
    elif operation == "max":
        total = reduce(max, spells)
    elif operation == "min":
        total = reduce(min, spells)
    return total


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:
    fire = partial(base_enchantment, 50, 'Fire')
    ice = partial(base_enchantment, 50, 'Ice')
    water = partial(base_enchantment, 50, 'Water')
    return {'fire': fire,
            'ice': ice,
            'water': water}


def enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment of {power} power on {target}"


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(arg: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _0(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @cast.register(str)
    def _1(arg: str) -> str:
        return f"Enchantment: {arg}"

    @cast.register(list)
    def _2(arg: list[Any]) -> str:
        return f"Multicast: {len(arg)} spells"
    return cast


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    spells: list[int] = [10, 20, 30, 40]
    try:
        print('Sum:', spell_reducer(spells, 'add'))
        print('Product:', spell_reducer(spells, 'multiply'))
        print('Max:', spell_reducer(spells, 'max'))
    except ValueError as e:
        print(e)
    print("\nTesting partial enchanter...")
    enchanted = partial_enchanter(enchantment)
    print(enchanted['fire']('sword'))
    print(enchanted['ice']('shield'))
    print("\nTesting memoized fibonacci...")
    fib = memoized_fibonacci
    print('Fib(0):', fib(0))
    print('Fib(1):', fib(1))
    print('Fib(10):', fib(10))
    print('Fib(15):', fib(15))
    print('\nTesting spell dispatcher...')
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher('fireball'))
    print(dispatcher(['fireball', 'ice orb', 'tsunami wave']))
    print(dispatcher(0.42))
