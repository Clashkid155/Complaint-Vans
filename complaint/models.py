from . import db
import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Document):
    """Model for user accounts."""
    name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password =  db.StringField(required=True)
    created_on = db.DateTimeField(default=datetime.datetime.utcnow)


    # __tablename__ = 'complaint-users'

    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String, nullable=False, unique=False)
    #email = db.Column(db.String(40), unique=True, nullable=False)

    #password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    #website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    #created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    #last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__ (self):
        return '<User {}>'.format(self.username)

#def init_db():
#if __name__ == '__main__':
 #   db.create_all()

    ## Create a test user
    #new_user = User('a@a.com', 'aaaaaaaa')
    #new_user.display_name = 'Nathan'
    #db.session.add(new_user)
    #db.session.commit()

    # new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
    #db.session.commit()


    #init_db()
