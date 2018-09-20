from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<number>")

def index(number):
    args={}
   # args['param'] = 'usman'
    args['number'] = int(number)
    return  render_template('numChk.html',args = args)

if __name__ == '__main__':
    app.run(debug=True, port=8081)