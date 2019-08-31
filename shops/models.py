from django.db import models

class Pet(models.Model):
	name = models.CharField(max_length=120)
	age = models.IntegerField()
	available = models.BooleanField(default=True)
	image = models.ImageField()
	price = models.DecimalField(max_digits=4, decimal_places=1)

	def __str__(self):
		return self.name
