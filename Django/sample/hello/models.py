from django.db import models

# Create your models here.
class Student(models.Model):
	"""docstring for ClassName"""
	Student_name=models.CharField(max_length=30)
	Student_ID=models.CharField(max_length=3,unique=True)

	def __str__(self):
		return self.Student_ID
		return self.Student_name

class Details(models.Model):
	"""docstring for ClassName"""
	Student_ID=models.ForeignKey(Student,on_delete=models.PROTECT)
	Address=models.CharField(max_length=200)
	SL=models.CharField(max_length=20)

	def __str__(self):
		return str(self.Student_ID)
		return self.SL

class Mark(models.Model):
	Student_ID=models.ForeignKey(Student,on_delete=models.PROTECT)
	SL=models.ForeignKey(Details,on_delete=models.PROTECT)
	Mark=models.CharField(max_length=3)	
		
	def __str__(self):
		return str(self.Student_ID)
		return str(self.SL)
		return self.Mark