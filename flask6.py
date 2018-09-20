from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<action>")

def index(action):
    args={}
    args['param'] = 'usman'
    args['action'] = action
    return  render_template('index.html',args = args)

if __name__ == '__main__':
    app.run(debug=True, port=8080)