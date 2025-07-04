from flask import Flask, render_template, redirect, url_for
from forms import FeedbackForm

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for CSRF protection

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        return render_template('success.html', name=name, email=email, message=message)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
