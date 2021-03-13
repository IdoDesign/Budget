
import uuid
import flask
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask (__name__)

app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
db.init_app(app)

from .routes.transactions import transactions
from .routes.users import users

app.register_blueprint(transactions)
app.register_blueprint(users)


@app.route('/')
def home():
    return flask.render_template('home.html')
'''
if __name__ == '__main__':
    app.run(debug=True)'''