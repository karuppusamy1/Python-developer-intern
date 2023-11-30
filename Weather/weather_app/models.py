from django.db import models

class WeatherAlert(models.Model):
    city = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.city}-{self.email}"
