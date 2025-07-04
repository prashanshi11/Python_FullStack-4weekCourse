from flask import Flask, render_template, request

app = Flask(__name__, template_folder='02_templates')

@app.route('/', methods=['GET', 'POST'])  # ✅ Allow POST method too
def index():
    if request.method == 'POST':
        name = request.form.get('username')
        return f"<h2>Hello, {name}!</h2>"  # You can also render another template here
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
