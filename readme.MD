# AFS website configuration

This repository holds the source code
for the AFS website.

The website itself is hosted on Heroku.



## Running the website locally

First, make sure migrations are properly applied.

Run `python manage.py migrate`

To make migrations `python manage.py makemigrations`

Simply run `python manage.py runserver`

## Collecting static files for whitenoise

Run `python manage.py collectstatic`