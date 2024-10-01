from App.database import db


class Review(db.Model):
    reviewID = db.Column(db.String(10), primary_key = True)
    studentID = db.Column(db.String(10), db.ForeignKey('student.id'), nullable=False)
    review =  db.Column(db.String(10000), nullable=False, unique=True)


    def __init__(self, revID , id ,review):
 
        self.reviewID = revID
        self.review = review
        self.studentID = id

    def __repr__(self):
        return f'\nStudent ID:  {self.studentID} \n Review: {self.review} \n'

    def toJSON(self):
        return{
            'id': self.id,
            'review': self.review
        }