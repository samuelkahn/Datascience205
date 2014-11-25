import logging

from google.appengine.ext import ndb


class Data(ndb.Model):
    year = ndb.IntegerProperty()
    income = ndb.FloatProperty()

    def to_json(self):
        return {
            'key': self.key.urlsafe(),
            'year': self.year,
            'income': self.income
        }
