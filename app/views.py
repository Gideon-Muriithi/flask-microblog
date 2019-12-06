from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/index')
def index():
    name = {'username': 'Tina'}
    title = 'Home'

    return render_template('index.html', name=name, title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(form.username.data,
        form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)