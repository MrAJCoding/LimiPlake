from flask import Flask, render_template

app = Flask(__name__)

# Route to the homepage
@app.route("/")
def home():
    # Make sure to render join.html here
    return render_template("join.html")

if __name__ == "__main__":
    app.run(debug=True)
