from django.db import models


class People(models.Model):
    p_id = models.AutoField(primary_key=True,unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
