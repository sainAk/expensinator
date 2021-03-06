from django.conf import settings
from django.db import models
from django.db.models.functions import Lower

from expensinator.utils.fields import LCharField


class Category(models.Model):
    name = LCharField(max_length=50)
    color = models.CharField(max_length=7, default="#000000")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(
                Lower("name"), "owner", name="unique_category_name_owner"
            )
        ]
