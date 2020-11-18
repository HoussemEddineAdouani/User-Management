# User-Management
## Introduction

Hello everyone ! :bowtie: 


`This applicaton was developped with`[ the micro-framework Flask](https://flask.palletsprojects.com/en/1.1.x/).

In this repository,I will propose a small example of `user management`.

which the functionality group of which will be the following:

- CRUD
  - Add user(s). # many_ways 
  - Update user(s).
  - Delete user(s).
  - Get all user(s).
- Authenticate a user.
- Connect a user.
- Export a user's data in pdf

## Explain the complex functionalities (in terms of processing)

1. Adding users in two ways :
   - Manual Addition.
   - Import of data concerning a set of users from an Excel file.
     - Condition: Emails are validated in terms of syntax etc. (The contribution of [Mailboxlayer API](https://mailboxlayer.com/documentation))
     - To ensure the import, I am in the process of introducing the [Flask-Excel](http://flask.pyexcel.org/en/latest/) dependency.
   
   
2. Connect a user :
   - To connect a user, I introduced the FLask-login dependency.
   - Flask-Login to manage user sessions.
        - To integrate it: 
          > Installation
          >
          ```
          $ pip3 install flask-login
          ```
          > Importations
          >
          ```python
          from flask_login import login_user, login_required, current_user
          ```
         
The other steps are explained in the code.
        
        
3. Export a user's data in pdf:
   - To export a pdf connecting user information, I introtuit [PDFKit](https://pypi.org/project/pdfkit/) (adapted version of ruby PDFKit library).
   - I used the global `response` variable to manipulate the content of the PDF.
   
## Annex
### Preparation of the work environment
> Virtual environment python 
```
$ pip3 install pipenv
```

> Flask , flask_login
```
(user-management)$ pipenv install flask flask_login
```

> Psycopg is a PostgreSQL adapter for the Python programming language (Postgresql already installed).
```
(user-management)$ pipenv psycopg2
```

> The binary package is a practical choice for development and testing but in production it is advised to use the package built from sources.
```
(user-management)$ pipenv psycopg2-binary
```

> SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
||
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.
```
(user-management)$ pipenv install flask-sqlalchemy
```

> Gunicorn, for “Green Unicorn”, is a WSGI HTTP web server written in Python and available for Unix.
||
The Web Server Gateway Interface (WSGI) is a specification that defines an interface between servers and web applications for the Python language.
```
(user-management)$ pipenv install gunicorn
```


