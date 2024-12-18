# from flask import Flask, jsonify
# from dotenv import load_dotenv

# app = Flask(__name__)
# load_dotenv()
# import os

# APP_VERSION = os.getenv("APP_VERSION", "0.0.0")
# TOOLS_VERSION = os.getenv("TOOLS_VERSION", "0.0.0")


# @app.route("/")
# def home():
#     return "Hello, Prajval!"


# @app.route("/api/versions", methods=["GET"])
# def get_versions():
#     """
#     Endpoint to return the app and tools version.
#     """
#     version_info = {
#         "app_version": APP_VERSION,
#         "tools_version": TOOLS_VERSION,
#     }
#     return jsonify(version_info), 200


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, jsonify
import subprocess
import datetime

app = Flask(__name__)


@app.route("/api/version", methods=["GET"])
def get_version():
    try:
        # Get the latest Git tag (version)
        version = (
            subprocess.check_output(
                ["git", "describe", "--tags"], stderr=subprocess.STDOUT
            )
            .decode("utf-8")
            .strip()
        )
        # Get the latest commit hash
        commit_hash = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], stderr=subprocess.STDOUT
            )
            .decode("utf-8")
            .strip()
        )
        # Get the current build timestamp
        build_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except subprocess.CalledProcessError:
        version = "unknown"
        commit_hash = "unknown"
        build_time = "unknown"

    return jsonify(
        {"version": version, "commit_hash": commit_hash, "build_time": build_time}
    )


if __name__ == "__main__":
    app.run(debug=True)
