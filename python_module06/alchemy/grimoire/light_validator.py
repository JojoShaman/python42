
def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    keyword = 'UNVALID'
    for word in light_spell_allowed_ingredients():
        if word in ingredients:
            keyword = 'VALID'
            break
    return (f"{ingredients} - {keyword}")
