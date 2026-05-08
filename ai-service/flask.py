# app.py

from flask import Flask
from routes.report import report_bp

app = Flask(__name__)

app.register_blueprint(report_bp)

@app.route("/health")
def health():
    return {
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
