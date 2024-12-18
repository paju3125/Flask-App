import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


# Endpoint to get version info
@app.route("/version", methods=["GET"])
def get_version():
    app_version = os.getenv("APP_VERSION", "unknown")
    tools_version = os.getenv("TOOLS_VERSION", "unknown")

    return jsonify({"app_version": app_version, "tools_version": tools_version})


if __name__ == "__main__":
    app.run(debug=True)
