from django.db import models

# Create your models here.

class Laptop(models.Model): # translate a table Laptop (in the db testapp_laptop)
    lap_type = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    issues = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    # convert object to string
    def __str__(self):
        return self.lap_type