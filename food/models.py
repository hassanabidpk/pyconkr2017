from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
       
    name = models.CharField(max_length=200)
    address = models.TextField()
    photo = models.ImageField(upload_to="food/photos/", null=True, blank=True)
    menu = models.TextField()
    tags = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User)

    def __str__(self):
        return self.name

