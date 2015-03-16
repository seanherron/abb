from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'abb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'hours.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^timesheets','hours.views.view_all',name='view_all'),
    url(r'^timesheet/create$', 'hours.views.new_timesheet', name='new_timesheet')
)