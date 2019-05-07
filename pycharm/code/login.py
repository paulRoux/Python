from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not all([username, password]):
        data = {
            "code": 1,
            "message": "invalid params"
        }
        return jsonify(data)

    if username == "roux" and password == "111":
        data = {
            "code": 0,
            "message": "login success"
        }
        return jsonify(data)
    else:
        data = {
            "code": 2,
            "message": "name or password error"
        }
        return jsonify(data)


if __name__ == "__main__":
    app.run()
