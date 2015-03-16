from models import Project
import csv
with open('hours/fixtures/projects.csv','r') as f:
  projects = csv.reader(f)
  for project in projects:
  	p = Project(name=project[0], billable=project[1]).save()