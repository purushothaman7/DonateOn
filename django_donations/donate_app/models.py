from django.db import models

class Signup(models.Model):
    # CITY_CHOICES = (
    #     (Chennai , "Chennai"),
    #     (Kanchipuram, "Kanchipuram"),
    #     (Thiruvallur, "Thiruvallur"),
    # )
    username = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    # city = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    # choices = CITY_CHOICES, default = Chennai


