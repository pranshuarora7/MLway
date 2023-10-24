import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
data = pd.read_csv("E:\Projects\MLway\HousePricePredictor\Final_data.csv")


@app.route("/")
def index():
    locations = sorted(data["location"].unique())
    return render_template("index.html", locations=locations)


@app.route("/predict", methods=["Post"])
def predict():
    return ""


if __name__ == "__main__":
    app.run(debug=True, port=5500)
