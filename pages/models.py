from django.db import models

class EventModel(models.Model):
    image = models.ImageField(upload_to='events')
    date = models.DateTimeField()
    location_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    start_time = models.TimeField()
    end_time = models.TimeField()



    def __str__(self):
        return self.location_name


    class Meta:
        verbose_name_plural = "Events"
        verbose_name = 'Event'



class CustomerModel(models.Model):
    image = models.ImageField(upload_to='events')
    description = models.CharField(max_length=221)
    name = models.CharField(max_length=221)
    job = models.CharField(max_length=221)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Customers"
        verbose_name = 'Customers'



class EmailModel(models.Model):
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


    class Meta:
        verbose_name_plural = "Emails"
        verbose_name = 'Email'


class BookTableModels(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    no_of_people = models.IntegerField()
    date = models.DateTimeField()
    time = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.email


    class Meta:
        verbose_name_plural = "BookTables"
        verbose_name = 'BookTable'
