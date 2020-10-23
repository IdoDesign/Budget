import datetime
from flask import Blueprint, render_template, request
from models.category import Category
from models.transaction import Transaction

transactions = Blueprint('transactions', __name__)

@transactions.route('/add_transactions', methods=["GET", "POST"])
def add_transaction():
    categories = Category.all()
    if request.method == "POST":
        desc = request.form['description']
        amount = float(request.form["amount"])*-1
        cat = request.form["category"]
        date= datetime.datetime.fromisoformat(request.form["date"])
        Transaction(date, amount, desc, cat).save_to_mongo()
    return render_template('add_transactions.html', categories=categories)

@transactions.route('/all')
def all_transactions():
    transactions=Transaction.all()
    for item in transactions:
        item.category = Category.get_by_id(item.category).name
    return render_template('all_transactions.html', transactions=transactions)
