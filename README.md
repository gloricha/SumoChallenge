# SumoChallenge
Django survey app


Requirements:
Python 2.7, django 1.8 instulled and mysql

Instructions:
1) Go in SumoSurvey/settings.py to DATABASES, create the mysql table with the name "sumodb" (or change this setting),
and put the right credentials: USER and PASSWORD (or create a user with this password).

2) From the directory of the project run python manage.py syncdb and in the end answer "no"

3) From the directory of the project run python manage.py runserver

4) Go to your browser and load:    "localhost:8000"

5) Urls:
localhost:8000/survey/ - The page where survey's question is presented
localhost:8000/survey/thanks - 'Thank you' page
localhost:8000/survey/results - The results that are dynamically presented in graphs
localhost:8000/admin/ - The admin page where you can edit the questions and the answers (choices). You are automatically directed there in your first approach to the results page (if you haven't logged in there yet). To log in use the following credentials:
username - root
password - root
