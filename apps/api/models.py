from django.db import models
from datetime import datetime
import pytz

# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
defaultDate = datetime(2000, 1, 1, 0, minute=0, second=0, microsecond=0, tzinfo=pytz.UTC, fold=0)

#Create your models here.
class Entertainer(models.Model):
	#v1
	name = models.CharField(max_length=200)
	about = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# v2
	# 'PA' = Performing Arts, 'SE' = Sporting Event
	type = models.CharField(max_length=2, null=True)

	def __str__(self):
		return '%s %s' % (self.name, self.about)

class Venue(models.Model):
	#v1
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# v2
	about = models.CharField(max_length=250, null=True)

	def __str__(self):
		return '%s %s' % (self.name, self.address)

class Event(models.Model):
	#v1
	name = models.CharField(max_length=200)
	entertainer = models.ForeignKey(Entertainer, on_delete=models.CASCADE, related_name='events')
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
	date = models.DateTimeField(default=defaultDate)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    
	#v2
	# 'PA' = Performing Arts, 'SE' = Sporting Event
	type = models.CharField(max_length=2, null=True)

	def __str__(self):
		return '%s' % (self.name)


