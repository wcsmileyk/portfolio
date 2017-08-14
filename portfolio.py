import os

from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail, Message

from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or '\xfb\x92$\x0f\xef\xb4(\xb5\xaf\x9f-9N\xf1\xc6h\x8f\x87\xc5L\xde\x9a=;'


@app.route('/')
@app.route('/index')
def index():
    form = ContactForm()
    return render_template('index.html', form=form)


@app.route('/contact', methods=['POST'])
def contact():
    pass


if __name__ == '__main__':
    app.run(debug="True", host="0.0.0.0")
