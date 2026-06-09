import os
import sys
import site


if sys.base_prefix != sys.prefix:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!\n" +
          "Safe to install packages without affecting\n" +
          "the global system.\n")
    print(f"Package installation path: {site.getsitepackages()[0]}")

else:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!\n" +
          "The machines can see everything you install.\n")
    print("To enter the construct, run:\n" +
          "python -m venv matrix_env\n" +
          "source matrix_env/bin/activate # On Unix\n" +
          "matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")
