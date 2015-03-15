from django.forms import ModelForm
from hours.models import Record, Timesheet

class TimesheetForm(ModelForm):
	class Meta:
		model = Timesheet
		fields = ['reporting_period','records']