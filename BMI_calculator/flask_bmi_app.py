from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    if height <= 0:
        return None
    height_m = height / 100
    return (weight)/(height_m**2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


@app.route("/", methods=["GET", "POST"])
def index():
    bmi_value = None
    category = None
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi_value = calculate_bmi(weight, height)
            category = bmi_category(bmi_value)
            if bmi_value is None:
                bmi_value = "invalid height"
                category = None
        except ValueError:
            bmi_value = "Invalid input"
            category = None

    return render_template("index.html", bmi=bmi_value, category=category)


if __name__ == "__main__":
    app.run(debug=True)
          
