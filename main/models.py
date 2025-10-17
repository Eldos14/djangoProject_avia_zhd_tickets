from django.db import models


class TransportType(models.TextChoices):
    PLANE = 'plane', 'Самолет'
    TRAIN = 'train', 'Поезд'


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Route(models.Model):
    departure = models.ForeignKey(City, related_name='departures', on_delete=models.CASCADE)
    destination = models.ForeignKey(City, related_name='destinations', on_delete=models.CASCADE)
    transport_type = models.CharField(max_length=10, choices=TransportType.choices)

    def __str__(self):
        return f"{self.departure} → {self.destination} ({self.get_transport_type_display()})"


class Ticket(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.route} | {self.company_name} | {self.price}₽"
