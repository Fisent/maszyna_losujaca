from django.db import models


class Draw(models.Model):
    name = models.CharField(max_length=200)


class DrawCandidate(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    recipient = models.ForeignKey("DrawCandidate", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.name) + ", daje prezent " + (self.recipient.name if self.recipient else "nikomu")
