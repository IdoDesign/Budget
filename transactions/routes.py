import datetime
import flask
from models.category import Category
from models.transaction import Transaction

transactions = flask.Blueprint('transactions', __name__)

@transactions.route('/add_transactions', methods=["GET", "POST"])
def add_transaction():
    categories = Category.all()
    if flask.request.method == "POST":
        desc = flask.request.form['description']
        amount = float(flask.request.form["amount"])*-1
        cat = flask.request.form["category"]
        date= datetime.datetime.fromisoformat(flask.request.form["date"])
        Transaction(date, amount, desc, cat, flask.session['user']).save_to_mongo()
    return flask.render_template('add_transactions.html', categories=categories)

@transactions.route('/all')
def all_transactions():
    transactions=Transaction.get_by_user(flask.session['user'])
    for item in transactions:
        item.category = Category.get_by_id(item.category).name
    return flask.render_template('all_transactions.html', transactions=transactions)
