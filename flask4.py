from flask import redirect
from flask import request
from flask import Flask ,render_template
from  flask import make_response

app = Flask(__name__)


@app.route('/c')
def index1():
    return redirect('http://www.yahoo.com')


@app.route('/c1')
def index2():

    response  = make_response('<h1>this document carr<h1>')
    response.set_cookie('color','red')
    return response


@app.route('/c2')
def index3():
    color = request.cookies['color']
    response = make_response('<font color='+color+'>this is basend on my cookie value</font>')
    return response

if __name__ =='__main__':
    app.run(debug=True)