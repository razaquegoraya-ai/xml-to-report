import os

def ensure_directories_exist():
    required_dirs = ["../logs", "../data"]
    for directory in required_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created missing directory: {directory}")

# Uncomment for standalone testing
# ensure_directories_exist()
