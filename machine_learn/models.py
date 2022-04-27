from django.db import models

# Create your models here.

class Flores(models.Model):
    
    # sl = sepal length (cm)
    # sw = sepal width (cm)	
    # pl = petal length (cm)	
    # pw = petal width (cm)

    sl = models.CharField(max_length=5)
    sw = models.CharField(max_length=5)
    pl = models.CharField(max_length=5)
    pw = models.CharField(max_length=5)
    predict = models.CharField(max_length=20)

    def __str__(self):
        return self.predict
