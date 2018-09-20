from flask import redirect
from flask import request
from flask import Flask ,render_template
from  flask import make_response

app = Flask(__name__)


@app.route('/d')
def index1():
    return redirect('http://www.yahoo.com')


@app.route('/d1')
def index2():

    response  = make_response('<h1>this document carries Text<h1>')
    response.set_cookie('size','100')
    return response


@app.route('/d2')
def index3():
    size = request.cookies['size']
    response = make_response('<font size='+size+'>this is basend on my cookie value</font>')
    return response

if __name__ =='__main__':
    app.run(debug=True,port=8080)