from django.db import models

# Create your models here.
class category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 50)
		
    def __str__(self):
        return self.name
	
class product(models.Model):
	price = models.IntegerField(default=0)
	name = models.CharField(max_length = 50)
	categoryId = models.ForeignKey(category, on_delete = models.CASCADE, default=1)
	image = models.ImageField(upload_to='upload/products/')
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length=250, default='', blank = True, null = True)
	
	def __str__(self):
		return self.name