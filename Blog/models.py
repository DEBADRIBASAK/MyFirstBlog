from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
	PriKey = models.CharField(max_length=255,primary_key=True)
	Heading = models.CharField(max_length=100)
	DateOfPost = models.DateField(default=datetime.date.today())
	Content = models.TextField()