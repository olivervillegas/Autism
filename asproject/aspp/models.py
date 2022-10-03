from django.db import models

# Create your models here.
class User(models.Model):
	f_name = models.CharField('First Name', max_length=120)
	l_name = models.CharField('Last Name', max_length=120)
	address = models.CharField('Address', max_length=300)
	city = models.CharField('City', max_length=120)
	country = models.CharField('Country', max_length=120)
	zip_code = models.IntegerField('Zip Code')
	phone = models.IntegerField('Phone Number')
	email = models.EmailField('Email')

	def __str__(self):
		return self.f_name + " " + self.l_name



class Article(models.Model):
	title = models.CharField('Article Title', max_length=120)
	author = models.CharField('Author(s)', max_length=120)
	content = models.FileField('Content', storage=None, null=True)
	date_added = models.DateTimeField('Date Published')
	category = models.CharField('Category', max_length=60)
	tags = models.TextField(blank=True)
	# photos = models.ImageField()

	def __str__(self):
		return self.title