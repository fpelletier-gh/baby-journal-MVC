# Baby journal

A simple app to create posts for events happening to your babies as they are growing.

[Live preview](https://babyjournal.francispelletier.ca)

## Installation

#### Setup for local development:

Clone the repository:

```
$ git clone https://github.com/fpelletier-gh/baby-journal-MVC
```

Change directory:

```
$ cd baby-journal-MVC
```

Create .env file with development settings from template .env.dist:

```
$ cp .env.dist .env
```

Install virtualenv package:

```
$ pip3 install virtualenv
```

Create the virtual environment:

```
$ virtualenv venv
```

Activate the environment:

```
$ source venv/bin/activate
```

Install the development requirements:

```
$ pip install -r requirements-dev.txt
```

Create the migrations files:

```
$ python manage.py makemigrations
```

Migrate the database:

```
$ python manage.py migrate
```

Create a superuser:

```
$ python manage.py createsuperuser
```

Run the test suite:

```
$ pytest
```

Start the development server:

```
$ python manage.py runserver
```

In your browser go to:

```
http://localhost:8000/
```

## Usage

1. Create an account
2. Sign in
3. Create or select a baby
4. Click on the baby to access his journal
5. Create, modify or delete posts
