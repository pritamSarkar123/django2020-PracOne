from django.db import models


class WebUser(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
