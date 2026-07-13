from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str],) -> Callable[[str, int],
                                                        tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int) -> Callable[[str, int], str]:
    def amplified_power(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))
    return amplified_power


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def spell_true(target: str, power: int) -> str:
        if condition(target, power):
            return (spell(target, power))
        else:
            return "Spell fizzled"
    return spell_true


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    def cast(target: str, power: int) -> list[str]:
        all_spells: list[str] = [spell(target, power) for spell in spells]
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
    print('Test conditional caster:\n')
    test = conditional_caster(lambda _, b: b > 10, fireball)
    print(test("Godzilla", 5))
