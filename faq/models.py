from django.db import models


class Status(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    status = models.CharField(
        max_length=8, choices=Status.choices, default=Status.ACTIVE
    )
