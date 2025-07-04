# 03_template_rendering.py
# Render a dynamic HTML page using Flask and Jinja2

from flask import Flask, render_template

app = Flask(__name__ ,template_folder='01_templates')

@app.route('/')
def home():
    user = {
        'name': 'Prashanshi',
        'role': 'Python Full Stack Developer'
    }
    return render_template('welcome.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
