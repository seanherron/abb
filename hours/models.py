from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.

class ReportingPeriod (models.Model):
	date_from = models.DateField()
	date_to = models.DateField()

	def __str__(self):
		return self.date_from.strftime("%m/%d/%y") + " -- " + self.date_to.strftime("%m/%d/%y")

class Project (models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)
	billable = models.BooleanField(default=True)
	description = models.TextField(blank=True, null=False)

	def __str__(self):
		return self.name

class Record (models.Model):
	project = models.ForeignKey(Project)
	hours = models.IntegerField()

	def __str__(self):
		return self.project.name + " (" + str(self.hours) + ")"

class Timesheet (models.Model):
	employee = models.ForeignKey(User, blank=True, null=True)
	reporting_period = models.ForeignKey(ReportingPeriod)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	records = models.ManyToManyField(Record)

	def get_absolute_url(self):
		return "timesheet/" + str(self.id)