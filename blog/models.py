from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images/')
