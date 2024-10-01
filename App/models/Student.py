from App.database import db

class Student(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    studentName =  db.Column(db.String(120), nullable=False, unique=True)
    review = db.relationship('Review', backref = 'reviews')


    def __init__(self, studentName, id):
        self.studentName = studentName
        self.id = id

    def __repr__(self):
        return f'<Student ID: {self.id}. Student name: {self.studentName}\nReviews: \n{self.review}>'


    def toJSON(self):
        return{
            'id': self.id,
            'studentName': self.studentName
        }