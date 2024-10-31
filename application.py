from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application


# import ridge regressor and scaler pickle

model = pickle.load(open("models/forest_fire_prediction_regressor.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))

        new_data_scaled = scaler.transform(
            [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        )
        result = model.predict(new_data_scaled)

        return render_template("home.html", result=result[0])

    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
