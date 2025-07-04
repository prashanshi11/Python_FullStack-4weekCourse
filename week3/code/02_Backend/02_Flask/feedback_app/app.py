from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    feedback = request.form.get('feedback')
    return render_template('submitted.html', name=name, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
