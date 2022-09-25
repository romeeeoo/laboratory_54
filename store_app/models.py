from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True, max_length=2000)

    def __str__(self):
        return "{}. {} {}".format(self.pk, self.name, self.description)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True, max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    picture_link = models.TextField(null=True, blank=True, max_length=500)

    def __str__(self):
        return "{}. {} {}".format(self.pk, self.name, self.description)
