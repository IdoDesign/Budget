import uuid
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import db, User


app = flask.Flask (__name__)

app.config.from_object("project.config.Config")
db.init_app(app)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"
login_manager.init_app(app)
@login_manager.user_loader

def load_user(user_id):
# since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(user_id)
    
from .routes.transactions import transactions
from .routes.users import users

app.register_blueprint(transactions)
app.register_blueprint(users)


if __name__ == '__main__':
    app.run()
