#!/bin/sh
echo "------ Create database tables ------"
python manage.py migrate --noinput
 
echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'changeme')" | python manage.py shell

echo "------- load data ------"
python manage.py loaddata hours/fixtures/initial_data.json

echo "------ starting django &nbsp;------"
waitress-serve --port=$VCAP_APP_PORT abb.wsgi:application