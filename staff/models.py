from django.db import models

class ChefModel(models.Model):
    image = models.ImageField(upload_to="chefs")
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=221)
    info = models.CharField(max_length=225)

    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Chefs'
        verbose_name = 'Chef'