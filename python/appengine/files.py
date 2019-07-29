from google.appengine.ext import ndb

class MemeInfo(ndb.Model):
    memeUrl = ndb.StringProperty(required=True)
    memeTop = ndb.StringProperty(required=True)
    memeBottom = ndb.StringProperty(required=True)
