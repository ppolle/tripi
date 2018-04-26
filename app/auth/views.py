from flask import render_template, request, flash, url_for, redirect
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required,current_user


@auth.route('/route',methods=['GET','POST'])
def index():
    form = RegistrationForm()
    login_form = LoginForm()
    return render_template('auth/login.html', registration_form=form, login_form=login_form)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for ("main.index"))

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    form = RegistrationForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.index'))

        flash('Invalid username or Password')

    title = "Blog login"
    return render_template('auth/login.html',login_form = login_form,registration_form = form,title=title)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    login_form = LoginForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, name = form.name.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
