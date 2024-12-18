from flask import Flask, jsonify
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
import os

APP_VERSION = os.getenv("APP_VERSION", "0.0.0")
TOOLS_VERSION = os.getenv("TOOLS_VERSION", "0.0.0")


@app.route("/")
def home():
    return "Hello, Prajval!"


@app.route("/api/versions", methods=["GET"])
def get_versions():
    """
    Endpoint to return the app and tools version.
    """
    version_info = {
        "app_version": APP_VERSION,
        "tools_version": TOOLS_VERSION,
    }
    return jsonify(version_info), 200


if __name__ == "__main__":
    app.run(debug=True)
