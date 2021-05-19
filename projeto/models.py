from projeto import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    address = db.Column(db.String(120))
    number = db.Column(db.Integer)
    city = db.Column(db.String(150))
    state = db.Column(db.String(20))
    country_code = db.Column(db.Integer)
    phone = db.Column(db.String(11))
    email =db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    pass_confirm = db.Column(db.String(128))

    def __init__(self, name, address, number, city, state, country_code, phone,
                email, username, password, pass_confirm):

        self.name = name
        self.address = address
        self.number = number
        self.city = city
        self.state = state
        self.country_code = country_code
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password
        self.pass_confirm = pass_confirm
