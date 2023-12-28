from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=355, null=True, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
