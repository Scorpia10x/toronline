from django.db import models

class Proxy(models.Model):
    name = models.CharField(max_length=16)
    rate = models.IntegerField()
    replace_original_domain = models.BooleanField(default=False)

    def __str__(self):
        return self.name