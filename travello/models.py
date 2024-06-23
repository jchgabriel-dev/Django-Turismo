from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Destination(models.Model):
	name = models.CharField(max_length=20)
	img = models.ImageField(upload_to='pics')
	desc = models.TextField()
	price = models.IntegerField (validators=[MinValueValidator(0),MaxValueValidator(1000000)])
	offer = models.BooleanField(default=False)

	def getUpdate(self):
		return "updatePlace/"+str(self.id)+"/"

	def getDelete(self):
		return "deletePlace/"+str(self.id)+"/"