from django.db import models
from django.utils import timezone


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    country = models.CharField(max_length=50, default="Unknown")
    established_year = models.IntegerField(default=2000)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100,
        choices=[
            ('SUV', 'Sport Utility Vehicle'),
            ('Sedan', 'Sedan'),
            ('Coupe', 'Coupe'),
            ('Wagon', 'Wagon'),
            ('Hatchback', 'Hatchback'),
        ]
    )
    year = models.IntegerField()
    dealer_id = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.car_make.name}"


class DealerReview(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    dealership = models.IntegerField()
    review = models.CharField(max_length=5000)
    rating = models.IntegerField()
    another_field = models.CharField(max_length=500, default="default value")
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(auto_now=False, default=timezone.now)
    car_make = models.CharField(max_length=500)
    car_model = models.CharField(max_length=500)
    car_year = models.IntegerField()
    sentiment = models.CharField(max_length=10)

    def __str__(self):
        return self.name
