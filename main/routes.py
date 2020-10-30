import flask
from flask import session

main = flask.Blueprint('main', __name__)

@main.route('/')
def home():
    return flask.render_template('home.html')