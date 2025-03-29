from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Fake database to store users
users = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")

    if not username or not email or not password or not confirm_password:
        return "All fields are required!", 400
    if password != confirm_password:
        return "Passwords do not match!", 400

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    users.append({"username": username, "email": email, "password": hashed_password})
    
    return "Account created successfully!"

if __name__ == "__main__":
    app.run(debug=True)
