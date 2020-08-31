from django.db import models
import json
import requests
import numpy as np
import pandas as pd


# Create your models here.


class Input(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    realm = models.CharField(max_length=50)
