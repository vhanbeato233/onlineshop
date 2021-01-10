from package import app, bcrypt,db
from package.forms import RegisterForm, LoginForm, UpdateAccountForm, ItemsForm, UpdateItemsForm
from flask import render_template, url_for, redirect, flash, request
from package.models import User, Item
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm(request.form)
    if request.method == 'POST':
            email=request.form['email']
            password=request.form['password']
    if form.validate_on_submit():
        user = User.query.filter_by(email=request.form['email']).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('profile'))
        else:
            flash(f'error')
    return render_template('login.html', form=form)
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = RegisterForm(request.form)
    if request.method == 'POST':
            email=request.form['email']
            username=request.form['username']
            fname=request.form['fname']
            lname=request.form['lname']
            password=request.form['password']
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, username=username, fname=fname, lname=fname, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for', 'sucess')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/profile")
def profile():
    return render_template('profile.html')
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')
