from django.db import models

class Proxy(models.Model):
    name = models.CharField(max_length=16)
    rate = models.IntegerField()

    def __str__(self):
        return self.name