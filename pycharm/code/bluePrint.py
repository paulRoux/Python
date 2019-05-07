from flask import Blueprint

app_orders = Blueprint("app_orders", __name__)


@app_orders.route("/get")
def get():
    return "get orders"


@app_orders.route("put")
def put():
    return "put orders"
