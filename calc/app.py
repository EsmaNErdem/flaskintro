# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route("/add")
def adding():
    a = int(request.args.get('a'))
    b = int(request.args['b'])
    result = add(a,b)
    return f'<h1>Result:{result}</h1>'

@app.route("/sub")
def substracting():
    a = int(request.args.get('a'))
    b = int(request.args['b'])
    result = sub(a,b)
    return f'<h1>Result:{result}</h1>'

@app.route("/mult")
def mlutiplying():
    a = int(request.args.get('a'))
    b = int(request.args['b'])
    result = mult(a,b)
    return f'<h1>Result:{result}</h1>'

@app.route("/div")
def dividing():
    a = int(request.args.get('a'))
    b = int(request.args['b'])
    result = div(a,b)
    return f'<h1>Result:{result}</h1>'

operations = {
    "add" : add,
    "sub" : sub,
    "div" : div,
    "mult" :mult
}

@app.route("/math/<operation>")
def calculation(operation):
    a = int(request.args.get('a'))
    b = int(request.args['b'])
    result = operations[operation](a,b)
    return f'<h1>Result:{result}</h1>'



