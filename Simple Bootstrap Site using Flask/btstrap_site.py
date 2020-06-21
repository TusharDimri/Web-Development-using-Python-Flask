from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def site():
    return render_template('bootstrap site.html')

app.run(debug = True)