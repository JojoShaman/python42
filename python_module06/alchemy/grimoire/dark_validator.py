from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    keyword = 'UNVALID'
    for word in dark_spell_allowed_ingredients():
        if word in ingredients:
            keyword = 'VALID'
            break
    return (f"{ingredients} - {keyword}")
