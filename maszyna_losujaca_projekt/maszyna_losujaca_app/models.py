from django.db import models


class Draw(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')


class DrawCandidate(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    recipient = models.ForeignKey("DrawCandidate", on_delete=models.DO_NOTHING, null=True)
