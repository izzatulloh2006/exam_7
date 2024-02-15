from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.username


