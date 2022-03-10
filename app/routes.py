from flask import Flask

app = Flask(__name__)

@app.route("/")
def about_me():
    me={
        "first_name":"Kyle",
        "last_name":"Haywood",
        "hobbies":"Board games",
        "active":True
        }
    return me


@app.route("/greet/<name>/")
def greet_user(name):
    return "<h1>Hello, %s</h1>" % name

@app.route("/square/<int:num>")
def square_num(num):
    return "<h1> %s square is: %s</h1>" %(num, num*num)