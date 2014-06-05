from google.appengine.ext import db
from google.appengine.api import users
import logging

# Make this very flat to start with, then add references later...
class Ride(db.Model):
    passengers_max = db.IntegerProperty()
    passengers_total = db.IntegerProperty()
    driver = db.BooleanProperty()
    driver_key = db.Key
    origin_add = db.StringProperty()
    origin_lat = db.FloatProperty()
    origin_lng = db.FloatProperty()
    dest_add = db.StringProperty()
    dest_lat = db.FloatProperty()
    dest_lng = db.FloatProperty()
    date = db.DateProperty()
    time = db.StringProperty()
    passengers = db.ListProperty(db.Key)
    contact = db.StringProperty()
    details = db.StringProperty()
    circle = db.StringProperty()
    event = db.StringProperty()

    def to_dict(self):
        resp = {}
        for p in Ride._properties:
            resp[p] = str(getattr(self, p))
        resp['id'] = self.key().id()
        return resp

class Comment(db.Model):
    user = db.Key
    date = db.DateProperty()
    text = db.TextProperty()
    event = db.Key
    ride = db.Key
    circle = db.Key

class Community(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    lat = db.FloatProperty()
    lng = db.FloatProperty()
    # appId = db.StringProperty()
    # appSecret = db.StringProperty()

class Circle(db.Model):
    name = db.StringProperty()
    description = db.StringProperty()
    def to_dict(self):
        d = {}
        d['id'] = Circle.key().id()
        d['name'] = Circle.name
        d['description'] = Circle.description
        return d

class Event(db.Model):
    name = db.StringProperty()
    circle = db.Key
    lat = db.FloatProperty()
    lng = db.FloatProperty()
    date = db.DateProperty()
    address = db.StringProperty()
    time = db.StringProperty()
    user = db.Key

    def to_dict(self):
        resp = {}
        for p in Ride._properties:
            resp[p] = str(getattr(self, p))
        resp['id'] = self.key().id()
        return resp
        
class ApplicationParameters(db.Model):
    apikey = db.StringProperty()
    notifyEmailAddr = db.StringProperty()
    fromEmailAddr = db.StringProperty()


class User(db.Model):
    id = db.StringProperty()
    auth_id = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    name = db.StringProperty()
    email = db.EmailProperty()
    circles = db.ListProperty(db.Key)

    def to_dict(self):
        resp = {}
        for u in User._properties:
            resp[u] = str(getattr(self, u))
        resp['key'] = self.key()
        return resp