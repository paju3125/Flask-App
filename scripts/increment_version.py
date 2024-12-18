import sys


def increment_version(version: str, part: str) -> str:
    """
    Increment the specified part of the version: major, minor, or patch.
    """
    try:
        major, minor, patch = map(int, version.split("."))
    except ValueError:
        raise ValueError(f"Invalid version format: {version}. Use 'x.y.z' format.")

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError("Invalid part specified. Use 'major', 'minor', or 'patch'.")

    return f"{major}.{minor}.{patch}"


def update_env_file(file_path: str, key: str, new_version: str):
    """
    Update the .env file with the new version.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if line.startswith(key):
                file.write(f"{key}={new_version}\n")
            else:
                file.write(line)


if __name__ == "__main__":
    # Read arguments from CLI
    env_file = sys.argv[1]  # Path to the .env file
    key = sys.argv[2]  # Key to update (e.g., APP_VERSION or TOOLS_VERSION)
    part = sys.argv[3]  # Which part to increment (major, minor, or patch)

    # Read current version from the .env file
    with open(env_file, "r") as file:
        for line in file:
            if line.startswith(key):
                current_version = line.split("=")[1].strip()
                break
        else:
            raise KeyError(f"{key} not found in {env_file}.")

    # Increment the version
    new_version = increment_version(current_version, part)
    print(f"Updating {key} from {current_version} to {new_version}")

    # Update the .env file
    update_env_file(env_file, key, new_version)
