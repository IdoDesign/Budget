from functools import wraps
import datetime
import flask
from models.category import Category
from models.transaction import Transaction

transactions = flask.Blueprint('transactions', __name__)

def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'user' not in flask.session:
        return flask.redirect('/login')
    if flask.session['user'] is None:
        return flask.redirect('/login')
    return f(*args, **kwargs)
  return decorated_function

@transactions.route('/add_transactions', methods=["GET", "POST"])
@login_required
def add_transaction():
    categories = Category.all()
    if flask.request.method == "POST":
        desc = flask.request.form['description']
        amount = float(flask.request.form["amount"])*-1
        cat = flask.request.form["category"]
        date= datetime.datetime.fromisoformat(flask.request.form["date"])
        Transaction(date, amount, desc, cat, flask.session['user']['_id']).save_to_mongo()
    return flask.render_template('add_transactions.html', categories=categories)

@transactions.route('/all')
@login_required
def all_transactions():
    transactions=Transaction.get_by_user(flask.session['user']['_id'])
    for item in transactions:
        item.category = Category.get_by_id(item.category).name
    return flask.render_template('all_transactions.html', transactions=transactions)
