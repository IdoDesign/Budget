import flask
from models.user import User


users = flask.Blueprint('users', __name__)
@users.route('/register', methods=["GET", "POST"])
def register():
    if flask.request.method=='POST':
        email = flask.request.form['email']
        password = flask.request.form['password']
        register = User.register(email, password)
        if register:
            flask.session['user'] = User.get_by_email(email)
            return flask.redirect('/')
    return flask.render_template('register.html')
    

@users.route('/login', methods=["GET", "POST"])
def login():
    if flask.request.method=='POST':
        email = flask.request.form['email']
        password = flask.request.form['password']
        login = User.is_login_valid(email, password)
        if login:
            flask.session['user'] = email
            return flask.redirect('/')
    return flask.render_template('login.html')

@users.route('/logout')
def logout_user():
    flask.session['user']=None
    return flask.redirect('/')