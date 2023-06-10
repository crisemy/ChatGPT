from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        bmi = round(weight / (height**2), 2)
        return render_template("index.html", bmi=bmi)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
