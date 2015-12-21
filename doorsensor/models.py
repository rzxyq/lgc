from django.db import models


class Walkin(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    text = models.TextField(default='')

    def __str__(self):
        return self.timestamp

class Walkout(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    text = models.TextField(default='')
    
    def __str__(self):
        return self.timestamp
