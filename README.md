# Baby journal

A MVC application to create posts for events happening to your babies as they are growing.

The goal of this project was to build an application with the MVC pattern using Django, Postgresql, Bootstrap 4 and deploy it on a self manage linux server.

[Live preview](https://babyjournal.francispelletier.ca)

## Table of Contents

<!-- vim-markdown-toc GFM -->

- [Installation](#installation)
- [Development](#development)
  - [Settings](#settings)
  - [Virtual environment](#virtual-environment)
  - [Requirements](#requirements)
  - [Database](#database)
  - [Test](#test)
  - [Development server](#development-server)
- [Production](#production)
  - [Production Settings](#production-settings)
  - [Deployment](#deployment)
    - [Managed Server](#managed-server)
    - [Self Manage Server](#self-manage-server)
- [Usage](#usage)

<!-- vim-markdown-toc -->

## Installation

## Development

Clone the repository

```
$ git clone https://github.com/fpelletier-gh/baby-journal-MVC
```

Change directory

```
$ cd baby-journal-MVC
```

### Settings

Create .env file with development settings from template .env.dist

```
$ cp .env.dist .env
```

> The default settings for development are already set in the .env.dist  
> **_Do not use these settings in productions_**

### Virtual environment

Make sure python 3 is installed

Unix

```
$ which python3
```

Install virtualenv package

```
$ pip3 install virtualenv
```

Create the virtual environment

```
$ virtualenv venv
```

Activate the environment

```
$ source venv/bin/activate
```

### Requirements

Install the development requirements (**Virtual environment must be activated**)

```
$ pip install -r requirements-dev.txt
```

### Database

For development a SQLite database is used, it is **not recommended for productions usage**. I recommend **[Postgresql](https://www.postgresql.org/)** for production.

Create the migrations files

```
$ python manage.py makemigrations
```

Migrate the database

```
$ python manage.py migrate
```

Create a superuser

```
$ python manage.py createsuperuser
```

### Test

Run the test suite

```
$ pytest
```

### Development server

Start the development server

```
$ python manage.py runserver
```

In your browser go to

```
http://localhost:8000/
```

## Production

### Production Settings

Create `.env` file from template `.env.dist`

```
$ cp .env.dist .env
```

Edit the environment variables

```
$ vim .env
```

> The `.env` file needs to be updated with the production settings

### Deployment

Some Deployment options

#### Managed Server

- [Heroku](https://www.heroku.com/python)

#### Self Manage Server

- [Digital Ocean](https://www.digitalocean.com/products/droplets)

## Usage

1. Create an account
2. Sign in
3. Create or select a baby
4. Click on the baby to access his journal
5. Create, modify or delete posts
