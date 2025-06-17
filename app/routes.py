from flask import render_template
from app import app
from app.forms import LoginForm

# python -m flask run

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)