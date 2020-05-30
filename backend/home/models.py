from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    name = models.BinaryField(null=True, blank=True,)
    test = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_test",
    )
    emp = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_emp",
    )
    subpage = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="customtext_subpage",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Testtt(models.Model):
    "Generated Model"
    testt = models.BinaryField()


class Testing(models.Model):
    "Generated Model"
    test = models.BigIntegerField()


class Test(models.Model):
    "Generated Model"
    test = models.BigIntegerField()
