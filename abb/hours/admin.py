from django.contrib import admin

# Register your models here.
from hours.models import Project, Record, ReportingPeriod, Timesheet

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    pass

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass

@admin.register(ReportingPeriod)
class ReportingPeriodAdmin(admin.ModelAdmin):
    pass