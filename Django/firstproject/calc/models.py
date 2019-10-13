from django.db import models

# Create your models here.
class Topic(models.Model):

	top_name=models.CharField(max_length=200,unique=True)


	def __str__(self):
		return self.top_name

class Webpage(models.Model):
	"""docstring for ClassName"""
	topic=models.ForeignKey(Topic,on_delete=models.PROTECT)
	name=models.CharField(max_length=50,unique=True)
	url=models.URLField(unique=True,default='Something')


	def __str__(self):
		return self.name

class  AccessRecord(models.Model):
	"""docstring for ClassName"""
	name=models.ForeignKey(Webpage,on_delete=models.PROTECT)
	date=models.DateField()

	def __str__(self):
		return str(self.date)
		
