if we run manage.py test, Django will run both the functional and the unit
tests: python manage.py test

In order to run just the unit tests, we can specify that we want to only run the tests for the app1 app: python manage.py test app1