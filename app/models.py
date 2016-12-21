from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50, unique=True, db_index=True)
	password = models.CharField(max_length=50)
	shares = models.IntegerField()
	reg_data = models.DateField()

	def __init__(self, username, password, shares, reg_data):
		username = username
		password = password
		shares = shares
		reg_data = reg_data

	def __unicode__(self):
		return "<User %s>"%username

class Complaint(models.Model):
	user = models.ForeignKey()
	type = models.TextField(max_length=500)
	description = models.TextField()

	def __init__(self, type, description):
		type = type
		description = description

	def __unicode__(self):
		return "<Type %s>"%type