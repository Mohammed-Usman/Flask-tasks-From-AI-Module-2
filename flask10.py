from flask import Flask,render_template

app = Flask(__name__)

@app.route("/test/<number>")

def index(number):

    number = int(number)
    #blist = []
    #alist = [blist.append(i) for i in range(number)]
    numlist = range(1,number,2)
    return  render_template('loop.html',numlist = numlist)

@app.route("/my_macro")
def index2():
    return render_template('macro.html',args=[0,2,3,4,5,6,4,33,4,5,66,7,6,65,4432,432234])

if __name__ == '__main__':
    app.run(debug=True, port=8081)