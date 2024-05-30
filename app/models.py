from django.db import models


# Create your models here.
class Klass(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=60)
    stars = models.IntegerField(default=0)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    lifetime = models.IntegerField()
    price = models.FloatField()
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
