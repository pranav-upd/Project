from flask import Flask, flash, jsonify, redirect, render_template, request, session
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        h = request.form.get("height")
        if not h:
            errmsg = "Height is empty"
            return render_template("home.html",errmsg=errmsg)
        for i in h:
            if (ord(i)<48 or ord(i)>57) and ord(i)!=46:
                errmsg = "Invalid Input"
                return render_template("home.html",errmsg=errmsg)
        i = 0
        w = request.form.get("weight")
        if not w:
            errmsg = "Weight is empty"
            return render_template("home.html", errmsg=errmsg)
        for i in w:
            if (ord(i)<48 or ord(i)>57) and ord(i)!=46:
                errmsg = "Invalid Input"
                return render_template("home.html", errmsg=errmsg)
        i = 0
        age = request.form.get("age")
        if not age:
            errmsg = "Age is empty"
            return render_template("home.html",errmsg=errmsg)
        for i in age:
            if ord(i)<48 or ord(i)>57:
                errmsg = "Invalid Input"
                return render_template("home.html",errmsg=errmsg)
        gender = request.form.get("gender")
        if gender == "male":
            g = 5
        else:
            g = -161
        h = float(h)
        w = float(w)
        age = int(age)
        bmr_val = 10*w + 6.25*h - 5*age + g
        bmr = f"Your Basal Metabolic Rate (BMR) is {bmr_val}"
        return render_template("home.html",bmr=bmr)
    else:
        return render_template("home.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        successmsg = "Your message has been successfully sent"
        name = request.form.get("name")
        if not name:
            errmsg2 = "Enter your name"
            return render_template("contact.html",errmsg2=errmsg2)
        email = request.form.get("email")
        if not email:
            errmsg2 = "Enter your email address"
            return render_template("contact.html",errmsg2=errmsg2)
        comment = request.form.get("comment")
        if not comment:
            errmsg2 = "Enter a comment"
            return render_template("contact.html",errmsg2=errmsg2)
        requests.post(
		"https://api.mailgun.net/v3/sandboxb3989f3658384a21b81d5d8e6cf1735b.mailgun.org/messages",
		auth=("api", "a7f7116426c4abf25eac359507f994f7-ed4dc7c4-c32f967e"),
		data={"from": "Weight Planner <mailgun@sandboxb3989f3658384a21b81d5d8e6cf1735b.mailgun.org>",
			"to": ["pranavupadhyaya51@gmail.com"],
			"subject": "Message from Weight Planner",
			"text": f"Message from {name}, email: {email}. The message is: {comment}"})
        return render_template("contact.html",successmsg=successmsg)
    else:
        return render_template("contact.html")

@app.route("/lose")
def lose():
    return render_template("lose.html")

@app.route("/gain")
def gain():
    return render_template("gain.html")
