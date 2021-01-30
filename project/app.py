
import uuid
import flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes.transactions import transactions
from routes.users import users

app = flask.Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ido:Aa123456@localhost:5432/budget"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'IdoTarazi'

db.init_app(app)

app.register_blueprint(transactions)
app.register_blueprint(users)

@app.route('/')
def home():
    return flask.render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)