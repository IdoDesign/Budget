from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User
import main.routes as main
users = Blueprint('users', __name__)
@users.route('/register', methods=["GET", "POST"])
def register():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        if User.register(email, password):
            return redirect('/')
    return render_template('register.html')
    

@users.route('/login', methods=["GET", "POST"])
def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        if User.is_login_valid(email, password):
            return redirect('/')
    return render_template('login.html')