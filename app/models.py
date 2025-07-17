from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    discription = models.TextField()

    def __str__(self):
        return self.name


