from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

    def _str_(self) -> str:
        return self.name
