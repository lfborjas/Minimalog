from django.db import models
from django.contrib.auth.models import User 

class Entry(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique = True)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    #updated = db.DateTimeProperty(auto_now=True)
    def __unicode__(self):
        return u"%s by %s" % (self.title,self.author)

    @models.permalink
    def get_absolute_url(self):
        return ('minimalog.views.entry', [], {"slug": self.slug})
    
    class Meta:
        verbose_name_plural = "Entries"

