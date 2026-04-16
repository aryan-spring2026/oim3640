from flask import Flask

app = Flask(__name__)


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    if name is None:
        name = "World"
    name = name.capitalize()
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)