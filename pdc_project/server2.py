from flask import Flask, render_template

app = Flask(__name__)

headings = ("Name", "Role", "Salary")
data = (
    ("Rolf", "Software Engineer", "$10000.0"),
)


@app.route("/")
def table():
    return render_template("table.html", headings=headings, data =data)


app.run()