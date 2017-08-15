import os

from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mail import Mail, Message

from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or '\xfb\x92$\x0f\xef\xb4(\xb5\xaf\x9f-9N\xf1\xc6h\x8f\x87\xc5L\xde\x9a=;'

app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
app.config['MAIL_DEFAULT_SENDER'] = 'admin@wsmiley.com'

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message('New Freelance Contact')
            msg.recipients = ['wesley.c.smiley@gmail.com']
            contact_name = form.name.data
            contact_email = form.email.data
            contact_message = form.message.data

            msg.body = f'Name: {contact_name} \n Email: {contact_email} \n Message: \n {contact_message}'
            mail.send(msg)
            flash('Thank you for your message')

        else:
            flash('All fields are required')

        return redirect(url_for('index', _anchor='contact'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
