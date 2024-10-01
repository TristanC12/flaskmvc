from App.models import Student
from App.database import db
import json

def add_student():
    studentName = input('Enter student name: ')
    id = input('Enter student ID: ')
    new_student = Student(studentName, id)
    try:
        db.session.add(new_student)
        db.session.commit()
        print(f'{studentName} added!')
        return new_student
    except:
        db.session.rollback()
        return None

def get_student():
    id = input("Enter student ID for query: ")
    return_student = Student.query.get(id)
    if not return_student:
        print('Student not found')
        return 
    else:
        return return_student
    
