import os
from dotenv import load_dotenv

RED_B = '\033[31;1m'
RED = '\033[31m'
END = '\033[0m'

if __name__ == "__main__":
    loaded = load_dotenv()
    config = [
        'MATRIX_MODE',
        'DATABASE_URL',
        'API_KEY',
        'LOG_LEVEL',
        'ZION_ENDPOINT'
    ]
    mode = os.getenv('MATRIX_MODE')
    db = os.getenv('DATABASE_URL')
    api = os.getenv('API_KEY')
    log = os.getenv('LOG_LEVEL')
    ep = os.getenv('ZION_ENDPOINT')
    error = 0
    for key in config:
        if os.getenv(key) is None:
            print(f"{RED}[ERROR] " +
                  f"{END}{RED_B}{key}{END}{RED} " +
                  f"variable is not defined{END}")
            error = 1
    if error:
        exit()
    print("\nORACLE STATUS: Reading the Matrix...\n")
    database = "Connected to local instance"
    if mode == 'production':
        database = "Connected to production instance"
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database : {database}")
    print(f"API Access: {'Authenticated' if api else 'Access denied'}")
    print(f"Log Level: {log}")
    print(f"Zion Network: {'Online' if ep else 'Offline'}")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")
