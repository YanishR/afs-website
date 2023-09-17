# AFS website configuration

This repository holds the source code
for the AFS website.

The website itself is hosted on Heroku.

### Prerequisites

In order to run the server, you will need:
- Pyenv to manage Python versions
- Python 3.11
- Poetry 1.6
- Psycopg Binary

### Creating a shell

Set the local and Poetry version:

`pyenv local 3.10 && poetry env use 3.10`

Enter the shell:
`poetry shell`

Install dependencies:
`poetry install`

`poetry install`


## Running the website locally

First, make sure migrations are properly applied.

To make them run `python manage.py makemigrations`.

Then, apply them: `python manage.py migrate`

Simply run `python manage.py runserver`

## Collecting static files for whitenoise

Run `python manage.py collectstatic`

> This needs to be done before merging if static
> files have been added.
> There is work coming to do that on the CI side.

## Deployment

To crate a review app, simply create a PR on the `main` branch.
This will temporarily deploy the application to a Heroku app.

When there's a merge onto `main`, the branch is 
automatically deployed with the up-to-date code.

## Repository layout


