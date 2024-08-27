from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify


class Room(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Message(models.Model):
    room = models.ForeignKey(Room, CASCADE)
    user = models.ForeignKey(User, CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date", ]

    def __str__(self):
        return self.body
