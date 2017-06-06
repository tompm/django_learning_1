from django.db import models

# Create your models here.
class Hello(models.Model):
	name=models.CharField(max_length=100, blank=True,default=' ')
	event=models.TextField()
	title=models.CharField(max_length=100, blank=True,default=' ')
	created= models.DateTimeField(auto_now_add=True)
	start_time=models.DateTimeField(null=True, blank=False)
	end_time=models.DateTimeField(null=True, blank=False)
	#class Meta:
	#	ordering = ('created',)