
from flask.templating import render_template
from flask import Flask, request

#initiate flask
app = Flask(__name__)

# define routes first of all default route as /
@app.route('/')
def home():
    return "Web development in python updated 123"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/sub/<int:a>/<int:b>")
def sub(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/templates")
def templates():
    return render_template("index.html", name="NAgesh")

@app.route("/newtemplates")
def newtemplates():
    return render_template("page.html")

@app.route("/forms", methods=["GET", "POST"])
def forms():
    if request.method=="POST":
        name=request.form["name"]
        return f"Hello, {name}!"
    
    
    
    return render_template("Form.html")

# run the app
if __name__ == "__main__":
    app.run(debug=True)