import traceback

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN EXCEPTION")
try:
    from alchemy.grimoire import dark_spellbook
except Exception:
    print(traceback.format_exc())
