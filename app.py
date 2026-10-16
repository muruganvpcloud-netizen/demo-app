import os
import socket
 
from flask import Flask, render_template_string
 
app = Flask(__name__)
 
VERSION = os.environ.get("APP_VERSION", "local")
MESSAGE = "Hello from GKE! Deployed by GitHub Actions and Argo CD."
 
PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Demo App</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f6fb; margin: 0; }
    .card { max-width: 560px; margin: 80px auto; background: #ffffff; padding: 32px;
            border-radius: 12px; box-shadow: 0 2px 12px rgba(0, 0, 0, 0.12); }
    h1 { color: #1a3a6b; font-size: 26px; }
    .info { color: #555555; }
  </style>
</head>
<body>
  <div class="card">
    <h1>{{ message }}</h1>
    <p class="info"><b>Version:</b> {{ version }}</p>
    <p class="info"><b>Served by pod:</b> {{ pod }}</p>
  </div>
</body>
</html>
"""
 
 
@app.route("/")
def home():
    return render_template_string(
        PAGE, message=MESSAGE, version=VERSION, pod=socket.gethostname()
    )
 
 
@app.route("/healthz")
def healthz():
    return "ok"
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
