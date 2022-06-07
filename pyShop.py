from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap


app=Flask("__name__")

Bootstrap(app)

@app.route("/")
def index():
    return render_template("base.html")

if __name__=="__name__":
    app.run(debug=True)