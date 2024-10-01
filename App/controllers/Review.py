from App.models import Review
from App.database import db
import json
import re
import uuid
import base64

#for generating random reviewID
def uuid_url64():
    rv = base64.b64encode(uuid.uuid4().bytes).decode('utf-8')
    return re.sub(r'[\=\+\/]', lambda m: {'+': '-', '/': '_', '=': ''}[m.group(0)], rv)

#add review to database
def add_review():
        id = input('Enter ID: ')
        review = input('\nEnter review: ')

        new_review = Review(str(uuid_url64()) ,id, review)
        try:
            db.session.add(new_review)
            db.session.commit()
            print('Review added!\n')
            return new_review
        except:
            db.session.rollback()
            return None


    
