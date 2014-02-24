import datetime
from flask import url_for
from music import db

class Album(db.Document):
    slug = db.StringField(max_length=255, required=False)
    name = db.StringField(max_length=255, required=True)
    publisher = db.StringField(max_length=255, required=True)
    genre = db.StringField(max_length=255, required=True)
    media_type = db.StringField(max_length=255, required=True)
    name = db.StringField(max_length=255, required=True)
    
    def get_absolute_url(self):
        return url_for('album', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name



class Artist(db.Document):

    name = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=False)
    albums = db.ListField(db.ReferenceField('Album'))


    def get_absolute_url(self):
        return url_for('artist', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name


class User(db.Document):

    name = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=False)
    email = db.StringField(max_length=255, required=False)

    def __unicode__(self):
        return "%s, Email:%s" % (self.name, self.email)




