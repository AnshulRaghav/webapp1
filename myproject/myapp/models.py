from django.db import models
from django.urls import reverse


# Create your models here.
#Parent class
class employee(models.Model):
	name=models.CharField(max_length=250)
	designation=models.CharField(max_length=12)
	gender=models.CharField(max_length=3)
	dp=models.FileField()
	video=models.FileField(default=None,blank=True)

	def get_absolute_url(self):
		return reverse('myapp:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.name + "->" + self.designation

#Child class
class auth_data(models.Model):
	employee_auth=models.ForeignKey(employee, on_delete=models.CASCADE)
	employee_id=models.CharField(max_length=250)
	employee_password=models.CharField(max_length=250)
	selected=models.BooleanField(default=False)

	def __str__(self):
		return self.employee_id

	