# AFS website configuration

This repository holds the source code
for the AFS website.

The website itself is hosted on Heroku.

### Prerequisites

In order to run the server, you will need:

- Pyenv to manage Python versions
- Python 3.11
- Poetry 2
- Psycopg Binary

### Creating a shell

`eval $(poetry env activate)`

Set the local and Poetry version:

`pyenv local 3.11.3 && poetry env use 3.11.3`

Install dependencies:
`poetry install`

## Running the website locally

Simply run `python manage.py runserver`

## Collecting static files for whitenoise

Run `python manage.py collectstatic`

> This needs to be done before merging if static
> files have been added.
> There is work coming to do that on the CI side.
