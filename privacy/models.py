from django.db import models


class Privacy(models.Model):
    """
    Set up privacy policy model object
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    privacy_policy = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
