from flask import Flask, render_template, request, redirect
from cs50 import SQL
import secrets

# Create the application
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///enxoval.db")

# Home page
@app.route("/")
def index():
    total_donations = db.execute("SELECT COUNT(*) as count FROM donations WHERE status = 'donated'")[0]["count"]
    total_available = db.execute("SELECT COUNT(*) as count FROM donations WHERE status = 'available'")[0]["count"]
    return render_template("index.html", total_donations=total_donations, total_available=total_available)

# Donate page
@app.route("/donate", methods=["GET", "POST"])
def donate():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        city = request.form.get("city")
        state = request.form.get("state")
        item = request.form.get("item")
        gender = request.form.get("gender")
        condition = request.form.get("condition")
        description = request.form.get("description")
        photo = request.form.get("photo")

        manage_code = secrets.token_urlsafe(8)

        db.execute("INSERT INTO donations (name, phone, city, state, item, gender, condition, description, photo, status, manage_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'available', ?)",
                   name, phone, city, state, item, gender, condition, description, photo, manage_code)

        return redirect(f"/thankyou/{manage_code}")

    return render_template("donate.html")

# Thank you page with manage link
@app.route("/thankyou/<code>")
def thankyou(code):
    donation = db.execute("SELECT * FROM donations WHERE manage_code = ?", code)
    if donation:
        return render_template("thankyou.html", manage_code=code, donation=donation[0])
    return redirect("/")

# Edit donation page
@app.route("/edit/<code>", methods=["GET", "POST"])
def edit_donation(code):
    donation = db.execute("SELECT * FROM donations WHERE manage_code = ?", code)
    if not donation:
        return redirect("/")

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        city = request.form.get("city")
        state = request.form.get("state")
        item = request.form.get("item")
        gender = request.form.get("gender")
        condition = request.form.get("condition")
        description = request.form.get("description")
        photo = request.form.get("photo")

        db.execute("UPDATE donations SET name=?, phone=?, city=?, state=?, item=?, gender=?, condition=?, description=?, photo=? WHERE manage_code=?",
                   name, phone, city, state, item, gender, condition, description, photo, code)

        return redirect(f"/thankyou/{code}")

    return render_template("edit.html", donation=donation[0], manage_code=code)

# Delete donation
@app.route("/delete/<code>")
def delete_donation(code):
    db.execute("DELETE FROM donations WHERE manage_code = ?", code)
    return render_template("deleted.html")

# Mark as donated
@app.route("/donated/<code>")
def mark_donated(code):
    db.execute("UPDATE donations SET status = 'donated' WHERE manage_code = ?", code)
    return render_template("donated.html")

# Available items page with filters
@app.route("/items")
def items():
    category = request.args.get("category", "")
    city = request.args.get("city", "")
    state = request.args.get("state", "")
    gender = request.args.get("gender", "")

    query = "SELECT * FROM donations WHERE status = 'available'"
    params = []

    if category:
        query += " AND item = ?"
        params.append(category)
    if city:
        query += " AND city LIKE ?"
        params.append("%" + city + "%")
    if state:
        query += " AND state = ?"
        params.append(state)
    if gender:
        query += " AND gender = ?"
        params.append(gender)

    donations = db.execute(query, *params)

    return render_template("items.html", donations=donations)

# Request page
@app.route("/request", methods=["GET", "POST"])
def request_help():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        needs = request.form.get("needs")

        db.execute("INSERT INTO requests (name, phone, needs) VALUES (?, ?, ?)",
                   name, phone, needs)
        return redirect("/")

    return render_template("request.html")

# Checklist page
@app.route("/checklist")
def checklist():
    return render_template("checklist.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")
