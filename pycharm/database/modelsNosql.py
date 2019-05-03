# import pymongo
#
#
# def getColl():
#     client = pymongo.MongoClient('127.0.0.1', 27017)
#     db = client.demo
#     user = db.user_collection
#
#     return user
#
#
# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def save(self):
#         user = {
#             "name": self.name,
#             "email": self.email
#         }
#         coll = getColl()
#         id = coll.insert(user)
#         print(id)
#
#     @staticmethod
#     def quertUser():
#         users = getColl().find()
#         return users

from app import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()

    def __str__(self):
        return "name:{}-email:{}".format(self.name, self.email)
