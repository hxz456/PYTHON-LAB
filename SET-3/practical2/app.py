from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re-password']

        if password == re_password:
            print("success")
        else:
            print("password not matched")
        print(request.form)
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)