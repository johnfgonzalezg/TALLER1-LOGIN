from models.user import User
from db import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    try:
        print('Request method: ' + request.method)
        if request.method == 'GET':
            print('Login GET')
            return render_template('login.html')
        elif request.method == 'POST':
            print('Login POST')
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                print('Encontró el usuario')
                welcome_message = f'¡Bienvenido a mi proyecto Flask, {user.username}!'
                success_login = True
                login_user(user)
                print('welcome_message: ' + welcome_message)
                if user.is_admin:
                    return redirect(url_for('user.admin_dashboard') + f'?welcome_message={welcome_message}')
                else:
                    return redirect(url_for('user.user_dashboard') + f'?welcome_message={welcome_message}')
            else:
                print('No encontró el usuario')
                flash('Usuario y/o password incorrectos', 'danger')
                return redirect(url_for('user.login'))
    except Exception as e:
        flash(str(e))
        print('Error login: ' + str(e))
        return redirect(url_for('user.login'))

@user_bp.route('/user_dashboad', methods = ['GET'], endpoint = 'user_dashboard')
def user_dashboar():
    welcome_message = request.args.get('welcome_message')
    return render_template('user_dashboard.html', welcome_message = welcome_message)

@user_bp.route('/admin_dashboard', methods = ['GET'], endpoint = 'admin_dashboard')
def admin_dashboard():
    welcome_message = request.args.get('welcome_message')
    return render_template('admin_dashboard.html', welcome_message = welcome_message)

@user_bp.route('/logout', methods=['POST'], endpoint='logout') 
def logout(): 
    logout_user() 
    return redirect(url_for('index'))

def load_user(user_id):
    return User.query.get(int(user_id))


