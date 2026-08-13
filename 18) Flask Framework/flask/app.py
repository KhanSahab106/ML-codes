from flask import Flask 

## WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to flask lecture.This is an amazing lecture"

@app.route('/index')
def index():
    return 'this is index page'
if __name__=="__main__":
    app.run(debug=True)