import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from mbta_helper import find_trip

load_dotenv()

app = Flask(__name__)
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def results():
    place_name = request.form["place_name"]

    try:
        result = find_trip(place_name)
        
        return render_template(
            "results.html",
            result=result,
            mapbox_token=MAPBOX_TOKEN
        )

    except Exception as error:
        return render_template("index.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)