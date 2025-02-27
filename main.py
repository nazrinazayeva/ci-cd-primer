from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/nazrin")
def nazrin():
    return "Hello, Nazrin!"


@app.route("/ping")
def ping():
    return "Pong!"


if __name__ == "__main__":
    app.run(debug=True)
