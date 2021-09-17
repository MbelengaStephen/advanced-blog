from flask import Flask, render_template
import datetime
import requests


posts = requests.get("https://api.npoint.io/03f78aa31e6fc8a058cf").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/about")
def about():
    current_year = datetime.datetime.now().year
    return render_template("about.html", year=current_year)


@app.route("/contact")
def contact():
    current_year = datetime.datetime.now().year
    return render_template("contact.html", year=current_year)


@app.route("/blog")
def blog():
    current_year = datetime.datetime.now().year
    return render_template("steve.html", all_posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
