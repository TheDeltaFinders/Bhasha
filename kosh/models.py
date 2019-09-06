#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 ft=python

# author : Prakash [प्रकाश]
# date   : buried
# update : 2019-09-06 16:41

import datetime

from django.db import models 

from django.utils import timezone


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField() 

    class Meta:
        abstract = True

class Pos(BaseModel):
    abbr = models.CharField(max_length=50,unique=True)
    partname = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.partname


class Meaning(BaseModel):
    meaning = models.TextField()
    pos = models.ForeignKey('Pos',on_delete=models.CASCADE)

    def __str__(self):
        return self.meaning

class BaseWord(BaseModel):
    word = models.CharField(max_length=100,unique=True)
    meaning = models.ManyToManyField('Meaning',blank=False)
    def __str__(self):
        return self.word + " : " 

class SubWord(BaseModel):
    parentword = models.ForeignKey('BaseWord',on_delete=models.CASCADE)
    subword = models.CharField(max_length=100,unique=False)
    meaning = models.ManyToManyField('Meaning',blank=False)

    def __str__ (self):
        return self.subword

class Comment(BaseModel):
    commenter = models.CharField(max_length=40)
    comment = models.TextField()
    postdate = models.DateTimeField(auto_now_add=True)
    word = models.ForeignKey('BaseWord',on_delete=models.CASCADE)

    def __str__(self):
        return self.commenter+ ' on '+ self.blogpost.title
