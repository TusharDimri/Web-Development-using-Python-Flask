from flask import Flask, render_template, request
from flask_sqlalchemy import  SQLAlchemy
from flask_mail import Mail
from datetime import  datetime
import json

with open("config.json", 'r') as c:
    params = json.load(c)['params']

local_server = True

app= Flask(__name__, template_folder="templates")
app.config.update(
    MAIL_SERVER ='smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password'],
)
mail = Mail(app)

if (local_server):  # If the server is Local Server
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]  # imported from config.json

else: # If the server is production server
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_server"] # imported from cnfig.json


db = SQLAlchemy(app)


class Contact(db.Model):
    S_no = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Email = db.Column(db.String(20), nullable=False)
    Ph_no = db.Column(db.String(12), nullable=False)
    Message = db.Column(db.String(120), nullable=False)
    Date = db.Column(db.String(12))



    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def home():
    return render_template("index.html", params=params)

@app.route("/about")
def about():
    return render_template("about.html", params=params)

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=='POST':
        '''Add entry to the Database'''
        name = request.form.get('name')
        email = request.form.get('email')
        ph_no = request.form.get('ph_no')
        message = request.form.get('message')

        entry = Contact(Name=name, Email=email, Ph_no=ph_no, Message=message, Date=datetime.now())

        db.session.add(entry)
        db.session.commit()
        mail.send_message('New Message from Website',
                          sender=email,
                          recipients=[params['gmail-user']],
                          body = "Message:"+message + "\n" + "Username:"+name + "\n" + "Phone Number:"+ph_no
                          )

    return render_template("contact.html",  params=params)

@app.route("/post")
def post():
    return render_template("post.html", params=params)

app.run(debug=True)