from flask import Flask ,render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1> Hello World<h1>'

@app.route('/user/<city>')
def user(city):
    if city == 'Karachi':
        return render_template('karachi.html',city)
    elif city == 'Lahore':
        return render_template('lahore.html',city)

if __name__ == '__main__':
    app.run(debug=True)
