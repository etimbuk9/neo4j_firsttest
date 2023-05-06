from django.db import models
from django_neomodel import DjangoNode
from neomodel import StringProperty, StructuredNode, Relationship, UniqueIdProperty, IntegerProperty
from neomodel import db

# Create your models here.
class Movie(DjangoNode):
    title = StringProperty()
    tagline = StringProperty()
    released = IntegerProperty()
    node_id = UniqueIdProperty(primary_key=True)

    class Meta:
        app_label = 'fetch'

    @property
    def serialize(self):
        return{
            'node_properties':{
                'title': self.title,
                'tagline': self.tagline,
                'released': self.released,
            }
        }