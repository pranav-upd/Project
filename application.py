import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    row = db.execute("SELECT * FROM users WHERE id = :user_id", user_id=user_id)
    username  = row[0]["username"]
    cash = row[0]["cash"]
    row = db.execute("SELECT * FROM index2 WHERE username = :username", username=username)
    return render_template("index.html",cash=usd(cash),row=row)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        quotes = lookup(symbol)
        if quotes == None:
            return apology("Invalid symbol")
        quantity = request.form.get("quantity")
        if quantity == "":
            return apology("The quantity cannot be left blank")
        quantity = int(quantity)
        price = quotes["price"]
        row = db.execute("SELECT username,cash FROM users WHERE id = :user_id ", user_id=session["user_id"])
        username = row[0]["username"]
        cash = row[0]["cash"]
        if quantity*price > cash:
            return apology("Not enough Money")
        name = quotes["name"]
        date = datetime.datetime.now()
        cash = cash - (quantity*price)
        db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash=cash, user_id=session["user_id"])
        db.execute("INSERT INTO history (username, symbol, quantity, price, datetime) VALUES (:username, :symbol, :quantity, :price, :date)", username=username, symbol=symbol, quantity=quantity, price=price, date=date)
        row = db.execute("SELECT quantity FROM index2 WHERE username = :username AND symbol = :symbol", username=username, symbol=symbol)
        if len(row) != 0:
            quantity2 = row[0]["quantity"]
            quantity2 = quantity2 + quantity
            db.execute("UPDATE index2 SET quantity = :quantity2 WHERE username = :username AND symbol = :symbol", quantity2=quantity2, symbol=symbol, username=username)
        else:
            db.execute("INSERT INTO index2 (username, symbol, stockname, quantity, price) VALUES (:username, :symbol, :name, :quantity, :price)", username=username, symbol=symbol, name=name, quantity=quantity, price=price)
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    row = db.execute("SELECT username FROM users WHERE id = :userid", userid=session["user_id"])
    username = row[0]["username"]
    row = db.execute("SELECT * FROM history WHERE username = :username", username=username)
    return render_template("history.html",row=row)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        quotes = lookup(symbol)
        if quotes == None:
            return apology("Invalid Symbol", 403)
        else:
            return render_template("quote2.html", quotes=quotes)
    #..
    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        username = request.form.get("username")
        password = request.form.get("password")
        repassword = request.form.get("repassword")
        #...
        if password != repassword:
            return apology("Passwords do not match", 403)
        #..
        upper = 0
        special = 0
        ascii_value = 0
        if len(password) < 8:
            return apology("The Password needs to contain atleast 8 characters, 2 special characters and 2 uppercase letters", 403)
        #..
        for i in password:
            ascii_value = ord(i)
            if ascii_value>=65 and ascii_value<=90:
                upper = upper + 1
            if ascii_value<48 or ascii_value>122:
                special = special + 1
            if ascii_value>57 and ascii_value<65:
                special = special + 1
            if ascii_value>90 and ascii_value<97:
                special = special + 1
        if upper<2 or special<2:
            return apology("The Password needs to contain atleast 8 characters, 2 special characters and 2 uppercase letters", 403)

        #..
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)
        if len(rows) != 0:
            return apology("Username already exists", 403)
        # Now we insert the values in the database
        phash = ""
        phash = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :phash)", username=username, phash=phash)
        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    row = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=session["user_id"])
    username = row[0]["username"]
    row = db.execute("SELECT symbol FROM index2 WHERE username = :username", username=username)
    row2 = row
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quantity = request.form.get("quantity")
        quantity = int(quantity)
        quotes = lookup(symbol)
        price = quotes["price"]
        total = quantity * price
        row = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
        cash = row[0]["cash"]
        row = db.execute("SELECT quantity FROM index2 WHERE username = :username AND symbol = :symbol", symbol=symbol, username=username)
        quantity2 = row[0]["quantity"]
        if quantity > quantity2:
            return apology("Not enough stocks")
        else:
            quantity2 = quantity2 - quantity
            cash = cash + total
            date = datetime.datetime.now()
            db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash=cash, user_id=session["user_id"])
            if quantity2 == 0:
                db.execute("DELETE FROM index2 where username = :username AND symbol = :symbol", username=username, symbol=symbol)
            else:
                db.execute("UPDATE index2 SET quantity = :quantity WHERE username = :username AND symbol = :symbol", quantity=quantity2, symbol=symbol, username=username)
            quantity3 = quantity * (-1)
            db.execute("INSERT INTO history (username, symbol, quantity, price, datetime) VALUES (:username, :symbol, :quantity, :price, :date)", username=username, symbol=symbol, quantity=quantity3, price=price, date=date)
        return redirect("/")
    else:
        return render_template("sell.html", row2=row2)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
