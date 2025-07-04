from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm, LoginForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions and CSRF
csrf = CSRFProtect(app)  # Enables CSRF protection


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Message submitted successfully!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Logged in successfully!", "success")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
