# User-Management
## Introduction

Hello everyone ! 

:bowtie: 

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
          >python
          ```
          from flask_login import login_user, login_required, current_user
          ```
         
The other steps are explained in the code.
        
        
3. Export a user's data in pdf:
   - To export a pdf connecting user information, I introtuit [PDFKit](https://pypi.org/project/pdfkit/) (adapted version of ruby PDFKit library).
   
