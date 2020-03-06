from flask import Flask, url_for, render_template, redirect
from forms import ContactForm
import os
SECRET_KEY = os.urandom(32)
app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = SECRET_KEY


@app.route('/')
def home():
    return render_template('index.html',
                           template='home-template')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('success'), code=302)
    return render_template('contact.html',
                           form=form,
                           template='form-template')

@app.route('/success', methods=('GET', 'POST'))
def success():
    return render_template('success.html',
                           template='success-template')

app.run()