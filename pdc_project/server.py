from flask import Flask, jsonify, render_template, request
from queries import *

username = '' 
password = ''
loggedin = False
isAdmin = False
SERVER = Server("muneeb", "admin")
USERS_DB = SERVER.get_database("users")

headings = ("Name", "Role", "Salary")
data = (
    ("Rolf", "Software Engineer", "$10000.0"),
)

# Creating a new "app" by using the Flask constructor. Passes _name_ as a parameter.
app = Flask(__name__)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python function that returns "Hello world!";
def index():
    file = open("index.html", "r")
    return file.read()

@app.route("/login")
# Generic Python function that returns "Hello world!";
def login():
    file = open("login.html", "r")
    return file.read()

@app.route("/authn",methods=['POST','GET'])
# Generic Python function that returns "Hello world!";
def authn():
    username=request.form['user']
    pwd=request.form['pass']
    if username=="" or pwd == "":
        file = open("error.html")
        return file.read()
    query = {'username': username}
    usr  = USERS_DB.search(query)
    if(len(usr)==0):
        print('User Not Found')
        file = open("error.html")
    elif usr[0]['password']!=pwd:
        print('Password Incorrect')
        file = open("error.html")
    else:
        print('Loged In Successfully')
        file = open("create/mainpage.html")
    return file.read()
    # return render_template("table.html", headings=headings, data = data)
 
@app.route("/employees/<int:salary>/<int:othr>",methods=['GET'])
def get_employeesWithSalary(salary):
    salary = int(salary)
    othr = int(othr)
    return str(salary)+str(othr)


@app.route("/logout")
# Generic Python function that returns "Hello world!";
def logout():
    file = open("D:/pdc/logout.html", "r")
    # file.read()
    return file.read()

# @app.route("/employees")
# # Annotation that allows the function to be hit at the specific URL. Indicates a GET HTTP method.
# def get_employees():
# # Returns a JSON of the employees defined above. jsonify is a Flask function that serializes the object for us.
#     return jsonify({"employees": employees})

# @app.route("/employees/<int:salary>",methods=['GET'])
# def get_employeesWithSalary(salary):
#     salary = int(salary)
#     for x in employees:
#         if(x["Salary"]==salary):
#             return jsonify({"employee": x})
#     return "Unable To Find Employee With The Spacified Salary"

# Checks to see if the name of the package is the run as the main package.
if __name__ == '__main__':
# Runs the Flask application only if the main.py file is being run.
    app.run()
    # file = open("D:/pdc/index.html", "r")