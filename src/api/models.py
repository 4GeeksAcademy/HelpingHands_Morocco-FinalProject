from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=True)
    last_name = db.Column(db.String(80), unique=False, nullable=True)
    login_method = db.Column(db.String(80), unique=False, nullable=True)
    

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "login_method": self.login_method
        }
    
class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, unique=False, nullable=False)
    currency = db.Column(db.String(80), unique=False, nullable=False)
    payment_method = db.Column(db.String(80), unique=False, nullable=False)
    payment_amount = db.Column(db.Integer, unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=False)
    country = db.Column(db.String(80), unique=False, nullable=False)
    postal_code = db.Column(db.Integer, unique=False, nullable=False)
    phone_number = db.Column(db.Integer, unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship(User)


    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "currency": self.currency,
            "payment_method": self.payment_method,
            "payment_amount": self.payment_amount,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "postal_code": self.postal_code,
            "phone_number": self.phone_number,
            "user_id": self.user_id,
        }
    
class ResetTokens(db.Model):
    __tablename__ = 'reset_tokens'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
    token = db.Column(db.String(250), unique=True, nullable=False)
    user = db.relationship(User)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "token": self.token
        }