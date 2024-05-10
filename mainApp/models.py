from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    price = models.IntegerField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
