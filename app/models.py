from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50, unique=True, db_index=True)
	password = models.CharField(max_length=50)
	shares = models.IntegerField()
	reg_data = models.DateField()

	def __unicode__(self):
		return self.username

class Complaint(models.Model):
	user = models.ForeignKey(
		'User'
	)
	type = models.TextField(max_length=500)
	description = models.TextField()

	def __unicode__(self):
		return self.type
