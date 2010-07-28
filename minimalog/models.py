from google.appengine.ext import db
from django.db import models

class Entry(db.Model):
    author = db.UserProperty()
    title = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    published = db.DateTimeProperty(auto_now_add=True)
    #updated = db.DateTimeProperty(auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return ('minimalog.views.entry', [], {"slug": self.slug})
        

