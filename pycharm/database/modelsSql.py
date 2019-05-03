from app import db


class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String)

    def __init__(self, userId, userName):
        self.id = userId
        self.name = userName
