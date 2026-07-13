from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def add(add_power: int) -> int:
        nonlocal power
        power += add_power
        return power
    return add


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanted(item_name: str) -> str:
        return enchantment_type + ' ' + item_name
    return enchanted


def memory_vault() -> dict[str, Callable[..., Any | None]]:
    key_value = {}

    def store(key: str, value: str) -> None:
        key_value[key] = value

    def recall(key: str) -> Any:
        if key in key_value:
            return key_value[key]
        else:
            return "Memory not found"
    return {'store': store,
            'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    total_power = spell_accumulator(100)
    print(f"Base {100}, add {20}: {total_power(20)}")
    print(f"Base {100}, add {30}: {total_power(30)}")
    print("\nTesting enchantment factory...")
    enchanted_item = enchantment_factory('Flaming')
    print(enchanted_item('Sword'))
    enchanted_item = enchantment_factory('Frozen')
    print(enchanted_item('Shield'))
    print("\nTesting memory vault...")
    key = 'secret'
    value = 42
    print(f"Store '{key}' = {value}")
    vault = memory_vault()
    vault['store'](key, value)
    print(f"Recall '{key}': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
