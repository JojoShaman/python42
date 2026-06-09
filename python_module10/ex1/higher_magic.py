from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_power(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))
    return amplified_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def spell_true(target: str, power: int) -> str:
        if condition(target, power):
            return (spell(target, power))
        else:
            return "Spell fizzled"
    return spell_true


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast(target: str, power: int) -> list[str]:
        all_spells = [spell(target, power) for spell in spells]
        return all_spells
    return cast


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {', '.join(combined('King Kong', 25))}\n")
    print("Testing power amplifier...")
    original = 10
    amplified = (power_amplifier(fireball, 3))('King Kong', original)
    print(f"Original: {original}, Amplified: {original * 3}")
    print('result:', amplified)
