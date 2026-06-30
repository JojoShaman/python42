from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return (['bats', 'frog', 'arsenic', 'eyeball'])


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    is_valid = validate_ingredients(ingredients)
    if 'VALID' in is_valid:
        status = "Spell recorded"
    else:
        status = "Spell rejected"
    return (f"{status}: {spell_name} ({is_valid})")
