from flask import Flask

app = Flask(__name__)

@app.route("/") # @ sign wraps the code for the route
def hello_world():
    return "<p>Hello, World!</p>"

# venv/Scripts/Activate.ps1
