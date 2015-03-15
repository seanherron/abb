from django.shortcuts import render, render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
# Create your views here.

from hours.models import Record, Project, Timesheet, ReportingPeriod

def home (request):
	return render(request, "home.html")

def view_all (request):
	timesheets = Timesheet.objects.all().filter(employee=request.user)
	return render(request, "view_all.html", {"timesheets":timesheets})

@csrf_protect
def new_timesheet (request):
	projects = Project.objects.all()
	weeks = ReportingPeriod.objects.last()
	if request.method == "POST":
		form = request.POST
		period = ReportingPeriod.objects.get(pk=form["week"])
		t = Timesheet(employee=request.user, reporting_period=period)
		t.save()
		t.records = []
		f = dict(form.lists())
		for pr in f["project"]:
			r = Record(project=Project.objects.get(pk=pr), hours=f["percentage"].pop(0))
			print(r)
			r.save()
			t.records.add(r)
		t.save()
		return redirect ("/")
	return render (request, 'edit.html', {"projects":projects, "weeks":weeks})