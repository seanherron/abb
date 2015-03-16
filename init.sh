#!/bin/sh
echo "------ Create database tables ------"
python abb/manage.py migrate --noinput
 
echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'changeme')" | python abb/manage.py shell

echo "------- load data ------"
python abb/manage.py loaddata hours/fixtures/initial_data.json

echo "------ starting django &nbsp;------"
cd abb && waitress-serve --port=$VCAP_APP_PORT abb.wsgi:application