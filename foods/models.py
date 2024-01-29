from django.db import models


from django.db import models

class FoodsModel(models.Model):
    image1 = models.ImageField(upload_to='foods')
    image2 = models.ImageField(upload_to='foods')
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    discount = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(default=0)
    discount_price = models.FloatField(null=True, blank=True)
    is_special = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Foods'
        verbose_name = 'Food'


class SpacialModel(models.Model):
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    name = models.CharField(max_length=221)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    description = models.TextField(max_length=225)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class EatModel(models.Model):
    name = models.CharField(max_length=221)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name





