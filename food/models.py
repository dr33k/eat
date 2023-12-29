from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=500, default="https://www.wallpaperup.com/uploads/wallpapers/2014/09/26/457781/b3cb545383e59aef8287ba9422002866.jpg")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("food:details", kwargs={"pk": self.pk})