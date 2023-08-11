from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name        = models.CharField(
        max_length=64,
        error_messages="name field is required.")
    description = models.TextField(
        default="",
        error_messages="description is optional and default value is empty string.")
    price       = models.FloatField(
        validators=[MinValueValidator(limit_value=0.0)],
        error_messages="price is required and float. Minimum value is 0.00 and default value is 0.00.")

    def __str__(self):
        return self.name
    