# By default static is public and templates is private in flask
# Static folder usually contains the front end(client side)  while templates store the backend(server side) of the website

from flask import Flask,  render_template
app = Flask(__name__, template_folder='templates')

@app.route("/")
def tushar():
    name1 = "Tushar Dimri"
    return render_template('index.html', name=name1)

@app.route("/about")
def about():
    return render_template('about.html')


app.run(debug = True)