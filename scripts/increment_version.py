import os
import re
import sys
from dotenv import load_dotenv

# Load the environment variables from .env
load_dotenv()


# Function to increment the version
def increment_version(version_str, part):
    version_parts = list(map(int, version_str.split(".")))

    if part == "major":
        version_parts[0] += 1
        version_parts[1] = 0
        version_parts[2] = 0
    elif part == "minor":
        version_parts[1] += 1
        version_parts[2] = 0
    elif part == "patch":
        version_parts[2] += 1

    return ".".join(map(str, version_parts))


# Function to update the .env file with the new version
def update_version_file(app_version, tools_version):
    with open(".env", "w") as f:
        f.write(f"APP_VERSION={app_version}\n")
        f.write(f"TOOLS_VERSION={tools_version}\n")


if __name__ == "__main__":
    target_key = sys.argv[1]  # APP_VERSION or TOOLS_VERSION
    version_part = sys.argv[2]  # major, minor, or patch

    # Get current version values
    current_app_version = os.getenv("APP_VERSION", "0.0.0")
    current_tools_version = os.getenv("TOOLS_VERSION", "0.0.0")

    if target_key == "APP_VERSION":
        new_app_version = increment_version(current_app_version, version_part)
        update_version_file(new_app_version, current_tools_version)
        print(f"Updated APP_VERSION to {new_app_version}")
    elif target_key == "TOOLS_VERSION":
        new_tools_version = increment_version(current_tools_version, version_part)
        update_version_file(current_app_version, new_tools_version)
        print(f"Updated TOOLS_VERSION to {new_tools_version}")
    else:
        print("Invalid target key. Use 'APP_VERSION' or 'TOOLS_VERSION'.")
