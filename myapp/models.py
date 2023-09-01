from django.db import models


class myapp(models.Model):
    title = models.CharField(max_length=50)
    contend = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



