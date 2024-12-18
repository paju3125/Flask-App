from flask import Flask, jsonify
import subprocess

app = Flask(__name__)


@app.route("/api/version")
def get_version():
    try:
        # Fetch the latest Git tag (version)
        version = (
            subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
            .decode()
            .strip()
        )
    except subprocess.CalledProcessError:
        version = "unknown"

    try:
        commit_hash = (
            subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
        )
    except subprocess.CalledProcessError:
        commit_hash = "unknown"

    return jsonify(
        {
            "version": version,
            "build_time": "unknown",  # You can also store build time dynamically
            "commit_hash": commit_hash,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
