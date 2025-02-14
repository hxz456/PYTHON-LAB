from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    return render_template("index.html",data = list1)

@app.route("/user/id/<id>")
def user(id):
    return render_template("user.html",id=id)

if __name__ == "__main__":
    app.run(debug=True)