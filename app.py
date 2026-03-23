from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def current_time():
    """Return the current UTC time in ISO 8601 format."""
    return jsonify({"current_time": datetime.now(timezone.utc).isoformat()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
