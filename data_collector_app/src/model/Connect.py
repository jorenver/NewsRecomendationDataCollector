import mongoengine as me


def connect_to_db():
    me.connect('newsbase')