from django.db import models
from datetime import datetime


# Create your models here.

class PostCharacterInfo(models.Model):
    # Stored characterInfo#
    name = models.CharField(max_length=50)
    realm = models.CharField(max_length=50)
    server = models.CharField(max_length=50)

    def __str__(self):
        template='{0.name} {0.realm} {0.server}'
        return template.format(self)
