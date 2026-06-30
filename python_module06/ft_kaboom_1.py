import traceback

if __name__ == '__main__':
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN EXCEPTION")
    try:
        from alchemy.grimoire import dark_spellbook  # noqa
    except Exception:
        print(traceback.format_exc())
