from django.db import models


class Faq(models.Model):
    A = "ACTIVE"
    U = "UNACTIVE"

    status_choices = [("A", ("active")), ("U", ("unactive"))]

    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    status = models.CharField(max_length=8, choices=status_choices, default=A)
