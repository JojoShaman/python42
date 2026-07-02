from importlib.metadata import metadata
from importlib import util

RED_BOLD = '\033[31;1m'
RED = '\033[31m'
BOLD = '\033[1m'
END = '\033[0m'

if __name__ == '__main__':
    packages = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical coputation',
        'matplotlib': 'Visualization'
        }
    missing = {}
    installed = {}
    for package, value in packages.items():
        spec = util.find_spec(package)
        if spec:
            installed[package] = value
        else:
            missing[package] = value
    if missing:
        for x in missing:
            print(f"{RED}[ERROR]: {END}" +
                  f"{RED_BOLD}{x}{END} {RED}package is missing!{END}")
        print("pip install:")
        print("$> pip install -r requirements.txt\n$> python3 loading.py\n")
        print("poetry install:")
        print("$> poetry install\n$> python3 loading.py")
    else:
        print("LOADING STATUS: Loading programs...")
        print("\nChecking dependencies:")
        for package, type in installed.items():
            meta = metadata(package)
            print(f"[OK] {meta['name']} ({meta['version']}) - {type} ready")
        try:
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt  # type: ignore
        except Exception as e:
            print(e)
        data = np.random.randint(999, size=(1000))
        print("\nAnalyzing Matrix data...")
        df = pd.DataFrame(data, columns=['matrix'])
        print("Processing 1000 data points...")
        plt.hist(data)
        print("Generating visualization...\n")
        plt.savefig('matrix_analysis.png')
        print('Results saved to: matrix_analysis.png')
        # plt.show()
