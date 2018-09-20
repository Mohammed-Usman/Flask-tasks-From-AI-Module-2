from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<number>")

def index(number):

    number = int(number)
    #blist = []
    #alist = [blist.append(i) for i in range(number)]
    numlist = range(1,number,2)
    return  render_template('loop.html',numlist = numlist)

if __name__ == '__main__':
    app.run(debug=True, port=8080)