from flask import redirect
from flask import request
from flask import Flask ,render_template


app = Flask(__name__)

@app.route('/user')
def index():
    return redirect('http://www.yahoo.com')

if __name__ == '__main__':
    app.run(debug=True)
