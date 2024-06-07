from django.db import models
from PIL import Image


class Quiz(models.Model):
    RUSSIA_HISTORY = 'russia history'
    MUSIC = 'music'
    NORWAY = 'norway'
    HISTORY = 'history'

    CHOICE_GROUP = {
        (RUSSIA_HISTORY, 'ruh'),
        (MUSIC, 'music'),
        (NORWAY, 'nor'),
        (HISTORY, 'history')
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    date = models.DateTimeField()
    countries = models.CharField(max_length=20, choices=CHOICE_GROUP, default='')
    img = models.ImageField(default='noimage.jpg', upload_to='quiz_image')

    def __str__(self):
        return f'{self.name}'