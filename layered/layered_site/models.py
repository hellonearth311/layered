from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="hackclub_profile")
	verification_status = models.CharField(max_length=64, blank=True, default="")
	slack_id = models.CharField(max_length=64, blank=True, default="")

	def __str__(self):
		return self.user.username

class Project(models.Model):
	owner = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="projects"
	)
	title = models.CharField(max_length=60, default="My Project")
	description = models.CharField(max_length=1000)
	printablesUrl = models.CharField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.id}: {self.title}"

class Item(models.Model):
	name = models.CharField(max_length=60)
	description = models.CharField(max_length=100)
	cost = models.PositiveIntegerField()

class Permissions(models.Model):
	class Meta:
		permissions = [
			("t1_review", "T1 Project Review"),
			("t2_review", "T2 Project Review"),
			("t3_review", "T3/Fraud Project Review"),
			("printer", "Project Printer"),
			("fulfillment", "Fulfill shop orders"),
			("statistics", "View statistics")
		]