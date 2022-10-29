from functools import wraps
from datetime import datetime
import random
import flask
from .. models import Category
from .. models import Transaction
from flask_login import current_user,login_required

transactions = flask.Blueprint('transactions', __name__)
COLORS = [
    "#330C2F",
    "#1A317F",
    "#0056CF",
    "#0076E7",
    "#005fe4",
    "#0095ff",
    "#27B1E2",
    "#4ECDC4",
    "#7AD9AC",
    "#A5E593",
    "#E7F76F",
    "#FCFC62",
    "#FEC731",
    "#ff9100",
    "#EE6352",
    "#ff0000",
    "#DA3E52",
    "#FF335A",
    "#FF66B3",
    "#FECEE9"

]


@transactions.route('/add_transactions', methods=["GET", "POST"])
@login_required
def add_transaction():
    categories = Category.all()
    if flask.request.method == "POST":
        desc = flask.request.form['description']
        amount = float(flask.request.form["amount"])
        cat = flask.request.form["category"]
        date= flask.request.form["date"]
        Transaction(date, amount, desc, cat, current_user._id).save()
    return flask.render_template('add_transactions.html', categories=categories)

@transactions.route('/all')
@login_required
def all_transactions():
    transactions= Transaction.get_by_user_sorted(current_user._id)
    return flask.render_template('all_transactions.html', transactions=transactions)

@transactions.route('/home')
def summary():
    doughnut_data = None
    bar_data = None
    if current_user.is_authenticated:
        sum_by_category= Transaction.group_by_category(current_user._id)
        sum_by_month= Transaction.group_by_month(current_user._id)

        doughnut_data = {
            'labels': sum_by_category['labels'],
            'datasets':[{
                'label': 'Sum',
                'data': sum_by_category['values'],
                'backgroundColor': COLORS
            }]
        }
        bar_data= {
            'labels': sum_by_month['labels'],
            'datasets':[{
                'label': 'Sum',
                'data': sum_by_month['values'],
                'backgroundColor': COLORS
            }]
        }

    return flask.render_template('home.html', doughnut_data=doughnut_data, bar_data=bar_data)
