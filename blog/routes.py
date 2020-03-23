from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post

posts = [
    {
        'author': 'Rishabh Bhardwaj',
        'title': 'Test Blog 1',
        'content': 'First Post Content',
        'posted': 'Jan 11 \'20'
    },
    {
        'author': 'Vipul Dixit',
        'title': 'Test Blog 2',
        'content': 'Second Post Content',
        'posted': 'Jan 22 \'20'
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'rishabh' and form.password.data == '1234567890':
            flash(f'Login successful! Hi {form.username.data}', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful! Please check username/password.', 'danger')
    return render_template('login.html', form=form, title='Login')
