"""Serves TabletopDB with Flask."""

import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/characters", methods=["GET"])
def download_characters():
    filename = "characters.json"
    filepath = os.path.join("data", filename)

    return (
        open(filepath, "rb"),
        200,
        {
            "Content-Type": "application/json",
            "Content-Disposition": f"attachment;filename={filename}",
        },
    )


@app.route("/<path:path>")
def html_page(path):
    template = path + ".html"
    return render_template(template)


if __name__ == "__main__":
    app.run(debug=True)
