from flask import Flask, render_template, request
from password_utils import check_password_strength, hash_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        password = request.form["password"]
        level, suggestions = check_password_strength(password)
        hashed = hash_password(password)

        # Prepare result message
        result = f"<b>Strength:</b> {level}<br><br>"
        if suggestions:
            result += "<b>Suggestions:</b><br>"
            for s in suggestions:
                result += f"- {s}<br>"
        result += f"<br><b>SHA-256 Hash:</b><br>{hashed}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
