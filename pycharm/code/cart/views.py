from flask import render_template
from . import app_cart


@app_cart.route("/get")
def get():
    return render_template("cart.html")
