import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import Student
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

from App.controllers import ( 
    add_student,
    get_student,
    add_review,
)

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''
@app.cli.command("addstudent")
def addstudent():
    add_student()

@app.cli.command("addreview")
def addreview():
    add_review()

@app.cli.command("searchstudent")
def searchstudent():
    reviews = get_student()
    print(reviews)