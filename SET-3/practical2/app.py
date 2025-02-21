from flask import Flask,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "sdfDFBGFNFGHFGDf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer)
@app.route("/",methods=["GET","POST"])
def home():

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re-password']

        if password == re_password:
            flash("Registered Successfully")
        else:
            flash("password not matched" , category="error")

        print(request.form)
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)