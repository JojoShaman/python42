import alchemy
import traceback

print("=== Alembic 4 ===\n" +
      "Accessing the alchemy module using'import alchemy'")
print("Testing creat_air:", alchemy.create_air())
print("Now show that not all functions can be reached\n" +
      "This will raise an exception!")
try:
    print(alchemy.create_earth())
except Exception:
    print(f"Testing the hidden create_earth: {traceback.format_exc()}\n")
