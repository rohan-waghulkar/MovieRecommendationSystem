from flask import Flask,render_template,request,session,redirect,url_for
import random
from twilio.rest import Client
import os
from src.User import user
import mysql.connector
from src.user_db_connection import make_db_connection,user_in_db,conn
from keys import sid,tocan,server_mob_number
app=Flask(__name__)
app.secret_key=os.urandom(24)
in_signin=False
@app.route("/")
def home():    
    return render_template('login.html')
@app.route("/login",methods=["POST"])
def login():
    global in_signin
    mobileNumber=session.get("mobno",None)
    username=request.form.get("username")
    password=request.form.get("password")
    # make_db_connection()
    # if flag:
    #     if user_in_db(username,password):
    #         return f"<h1>username is {usr.userName} and Mobile Number is {usr.mobnumber}</h1>"
    #     else:
    #         return render_template("verifyotp.html")
    # else:
    # usr=user(mobileNumber,username,password)

    if in_signin:
        usr = user(mobileNumber,username,password)
        in_signin = False
        return f"<h1> Sign Up Completed</h1>"
    else :
        if user_in_db(username=username,password=password):
            return f"<h1>username is {username} and Mobile Number is {mobileNumber}</h1>"
        else:
            return render_template("login.html")
    
@app.route("/send_otp",methods=["GET","POST"])
def signin():
    global in_signin
    in_signin=True
    if request.method=="POST":
        mobileNumber=request.form.get("mobileNumber")
        session['mobno']=mobileNumber
        # otp=str(random.randint(1000,9999))
        # session['generated_otp']=otp
        # client=Client(sid,tocan)
        # message=client.messages.create(
        # body=f"Hey Your One Time Password for Recommeder is :{otp}. let's get sign in into your app",
        # from_=server_mob_number,
        # to="+91"+mobileNumber
        # )
        otp="1111"
        session['generated_otp']=otp
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
            return render_template('verifyotp.html')
            
    else:
        return render_template('Verification Failed ')  #signin.html
if __name__=="__main__":
    app.run(debug=True)