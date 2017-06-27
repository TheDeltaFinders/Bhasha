import datetime

from django.db.models import Model
from django.db.models import DateTimeField
from django.db.models import CharField 
from django.db.models import TextField 
from django.db.models import SlugField 
from django.db.models import DateTimeField
from django.db.models import BooleanField 
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db import models

from django.utils import timezone


class Pos(Model):
    abbr = CharField(max_length=50,unique=True)
    partname = CharField(max_length=50,unique=True)
    create_date = DateTimeField(auto_now=True)
    is_active = BooleanField() 

    def __str__(self):
        return self.partname


class Meaning(Model):
    meaning = TextField()
    pos = ForeignKey('Pos')

    def __str__(self):
        return self.meaning

class BaseWord(Model):
    word = CharField(max_length=100,unique=True)
    meaning = ManyToManyField('Meaning',blank=False)
    def __str__(self):
        return self.word + " : " 

class SubWord(Model):
    parentword = ForeignKey('BaseWord')
    subword = CharField(max_length=100,unique=False)
    meaning = ManyToManyField('Meaning',blank=False)

    def __str__ (self):
        return self.subword
