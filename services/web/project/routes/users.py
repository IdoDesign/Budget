import flask
from flask_login import login_user, logout_user, login_required
from .. models import User
from .. common.utils import Utils

users = flask.Blueprint('users', __name__)

@users.route('/register', methods=["GET", "POST"])
def register():
    if flask.request.method=='POST':
        name = flask.request.form['name']
        email = flask.request.form['email']
        password = flask.request.form['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(name, email, Utils.hash_password(password))
            user.save()
            login_user(user)
            
            return flask.redirect('/home')
    return flask.render_template('register.html')
    

@users.route('/login', methods=["GET", "POST"])
def login():
    if flask.request.method=='POST':
        email = flask.request.form['email']
        password = flask.request.form['password']
        user = User.query.filter_by(email=email).first()
        if not user:
            flask.current_app.logger.info(f"{email} does not exsist")
            return flask.render_template('login.html')
        if not Utils.check_hashed_password(password, user.password_hash):
            flask.current_app.logger.info(f"{email} failed to login")
            return flask.render_template('login.html')  
        
        login_user(user)
        flask.current_app.logger.info(f"{email} logged in successfully")
        return flask.redirect('/home')
    
    return flask.render_template('login.html')

@users.route('/logout')
@login_required
def logout():
    logout_user()
    flask.current_app.logger.info(f"logged out successfully")
    return flask.redirect('/home')
