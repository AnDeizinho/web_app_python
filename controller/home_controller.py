from flask import render_template
from main import app

@app.route("/")
def index():
    return render_template("home/index.html")

@app.route("/sobre")
def sobre():
    return "<h1>Sobre a impresa aqui</h1>"

@app.route("/reclame")
def reclame():
    return "<h1>lá na casa das lamentações</h1>"