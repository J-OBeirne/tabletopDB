"""
Serves TabletopDB with Flask.
"""

import os
import json

from flask import Flask, request, render_template, send_file

app = Flask(__name__)


@app.route("/")
def index_page():
    """
    Serve the index page.
    """
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    """
    Serve the favicon.
    """
    icon_filename = "favicon.ico"
    icon_path = os.path.join(app.static_folder, icon_filename)
    return send_file(icon_path, mimetype="image/vnd.microsoft.icon")


@app.route("/characters", methods=["GET", "POST"])
def download_characters():
    """
    Serve the characters.json file.
    """
    filename = "characters.json"
    filepath = os.path.join("data", filename)

    if request.method == "GET":
        return (
            open(filepath, "rb"),
            200,
            {
                "Content-Type": "application/json",
                "Content-Disposition": f"attachment;filename={filename}",
            },
        )

    if request.method == "POST":
        data = request.get_json()
        with open(filepath, "r", encoding="utf-8") as file:
            characters = json.load(file)

        characters["characters"].append(data)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(characters, file, indent=4)

        return "", 201


@app.route("/<path:path>")
def html_page(path):
    """
    Serve the HTML pages that are not explicit.
    """
    template = path + ".html"
    return render_template(template)


if __name__ == "__main__":
    app.run(debug=True)
