import datetime
from flask import url_for
from music import db


class Artist(db.Document):

    slug = db.StringField(max_length=255, required=False)
    name = db.StringField(max_length=255, required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)


    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title