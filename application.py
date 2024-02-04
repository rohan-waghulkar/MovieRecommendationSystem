from flask import Flask,render_template,request,session,redirect,url_for
import random
from twilio.rest import Client
import os
from User import user


app=Flask(__name__)
app.secret_key=os.urandom(24)
@app.route("/")
def home():    
    return render_template('login.html')
@app.route("/login",methods=["POST"])
def login():
    mobileNumber=session.get("mobno",None)
    username=request.form.get("username")
    passward=request.form.get("password")
    usr=user(mobileNumber,username,passward)
    return f"<h1>username is {usr.userName} and Mobile Number is {usr.mobnumber}</h1>"
@app.route("/send_otp",methods=["GET","POST"])
def signin():
    if request.method=="POST":
        mobileNumber=request.form.get("mobileNumber")
        session['mobno']=mobileNumber
        otp=str(random.randint(1000,9999))
        session['generated_otp']=otp
        client=Client(" "," ")
        message=client.messages.create(
        body=f"Hey Your One Time Password for Recommeder is :{otp}. let's get sign in into your app",
        from_=" ",
        to="+91"+mobileNumber
        )
        # otp="1111"
        # session['generated_otp']=otp
        return render_template("verifyotp.html")
    else:
        return render_template("signin.html")
@app.route('/verify',methods=['GET','POST'])
def verify():
    if request.method=="POST":
        users_otp=str(request.form.get("otp"))
        otp=session.get('generated_otp',None)
        if otp==users_otp:
            return render_template("login.html")
        else:
            return redirect(url_for('verify.html'))
            
    else:
        return render_template('Verification Failed ')  #signin.html

if __name__=="__main__":
    app.run(debug=True)