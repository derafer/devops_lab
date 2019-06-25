# Create a script that outputs information about the current versions of python
# in the system:
# 1. + version
# 2. + virtual environment (name)
# 3. + python executable location
# 4. + pip location (each python version has its own version of pip)
# 5. + PYTHONPATH
# 6. + installed packages: name, version
# 7. + site-packages location
# Script should output result to *.json and *.yaml files.
# Additional task (optional): Output info about all python versions and
# environments.

import sys
import os
import platform
import pkg_resources
import distutils.sysconfig
import json
import yaml


if __name__ == "__main__":
    env_dump = {}
    env_dump["version"] = platform.python_version()
    env_dump["virtual environment"] = sys.path
    env_dump["executable location"] = sys.executable
    env_dump["pip location"] = os.path.join(
        distutils.sysconfig.get_python_lib(), "pip")
    pyth_paths = os.environ["PYTHONPATH"]
    a = pyth_paths.split()
    env_dump["PTYHONPATH"] = a
    installed_packages = {}
    for package in pkg_resources.working_set:
        installed_packages[package.project_name] = package.version
    env_dump["installed packages"] = installed_packages
    env_dump["site-packages location"] = distutils.sysconfig.get_python_lib()
    jsonf = open("env.json", "w")
    json.dump(env_dump, jsonf, indent=4)
    jsonf.close()
    yamlf = open("env.yaml", "w")
    yaml.dump(env_dump, yamlf, default_flow_style=False)
    yamlf.close()
