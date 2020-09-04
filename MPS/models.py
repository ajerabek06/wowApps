from django.db import models
from .api_look_up import scoreSearch


# Create your models here.
class CharacterInfo(models.Model):
    name = str(scoreSearch.name)
    region = str(scoreSearch.region)
    server = str(scoreSearch.realm)
    mythicscore = str(scoreSearch.mythicscore)

    def __str__(self):
        return f'{self.name} {self.region} {self.server} {self.mythicscore}'
