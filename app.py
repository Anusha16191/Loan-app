from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("mainpage.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/lender")
def lender():
    return render_template("registerlender.html")

@app.route("/vendor")
def vendor():
    return render_template("registervendor.html")

    
    

if __name__=="__main__":
    app.run(debug=True)

