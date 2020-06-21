from flask import Flask
app = Flask(__name__)

@app.route("/")
def tushar():
    return "Welcome to my website99"

app.run(debug = True) # Check Outupt without this statement to know its importance
# debug = True makes changes to our code be available in our website