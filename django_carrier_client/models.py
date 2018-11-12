from django.db import models

class AuthToken(models.Model):
    token = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.token

    def __unicode__(self):
        return self.token