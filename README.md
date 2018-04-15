# election-system
Online election system - Course project for Software Engineering CO251

## Installation
Enter the following commands in your terminal

### Install components 
```bash
sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
```
### Create a Database and Database User
```bash
sudo su - postgres
psql
CREATE DATABASE electionsystem;
CREATE USER user WITH PASSWORD 'password';
ALTER ROLE user SET client_encoding TO 'utf8';
ALTER ROLE user SET default_transaction_isolation TO 'read committed';
ALTER ROLE user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE electionsystem TO user;
\q
exit
```
### Clone the repository
```git clone https://github.com/mehnazyunus/election-system```

### Set up Virtual Environment and Install Requirements
```bash
python3 -m venv electionsystem
source electionsystem/bin/activate
cd election-system
pip install -r requirements.txt
```
### Migrate Database and Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
### Credits
[Install Django with PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
