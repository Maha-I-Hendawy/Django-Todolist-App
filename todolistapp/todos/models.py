from django.db import models

# Create your models here.


class Todo(models.Model):
	todo = models.CharField(max_length=100);
	complated = models.BooleanField(default=False)
	date_posted = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.todo}"