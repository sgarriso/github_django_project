# github_django_project
# configure django to run in local mode
# first install django
pip install django
pip install djangorestframework
# second confirm migrations are set
python manage.py  makemigrations
python manage.py migrate
# run the github_load.py in the background this will pull 200 records from github wait an hour and try to update any records that have changed in the past hour
python github_load.py
# run the django web server
python manage.py runserver
# go to web site
http://127.0.0.1:8000/list/record/83222441/
