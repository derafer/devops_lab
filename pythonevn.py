# Create a script that outputs information about the current versions of python in the system:
# 1. version
# 2. virtual environment (name)
# 3. python executable location
# 4. pip location (each python version has its own version of pip)
# 5. PYTHONPATH
# 6. installed packages: name, version
# 7. site-packages location
#Script should output result to *.json and *.yaml files.
#Additional task (optional): Output info about all python versions and environments.

import sys
import os
import subprocess


if __name__ == "__main__":
    version = sys.prefix
    python = subprocess.check_output("python -V", shell=True).decode()

