from django.db import models

# Create your models here.

class Quote(models.Model):

    thinker = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.thinker