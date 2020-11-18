#importations
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager

# init ORM :SQLAlchemy
db = SQLAlchemy()

# UserMixin
# Flask-login requires a User model with the following properties:
# has an is_authenticated() method that returns True if the user has provided valid credentials
# has an is_active() method that returns True if the user’s account is active
# has an is_anonymous() method that returns True if the current user is an anonymous user
# has a get_id() method which, given a User instance, returns the unique ID for that object
# UserMixin class provides the implementation of this properties. Its the reason you can call
# for example is_authenticated to check if login credentials provide is correct or not instead
# of having to write a method to do that yourself.
# (https://stackoverflow.com/questions/63231163/what-is-usermixin-in-flask)

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    direction = db.Column(db.String(200))

    def __init__(self, first_name,last_name, email, password,direction):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.direction = direction


#Flask Application Factory
def create_app():
    # Application initialization
    app = Flask(__name__)

    #Define the variables of Configuration
    ## the secret key ensures the security of the sessions
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    # To ensure the mapping with the Postgresql Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/orange_database'

    # The option SQLALCHEMY_TRACK_MODIFICATIONS allows you to disable the modification tracking system(Stack Overflow )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.render_to_login'
    login_manager.init_app(app)

    # user_loader is used to reload the user object from the user ID stored in the session.
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Making application components ==>  The concept of blueprints
    # Blueprint for authentification
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Blueprint for main
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
    # to run it : $ export FLASK_APP=project
                # $ export FLASK_APP=project
                # $ flask run
    # Running on http://127.0.0.1:5000/

