import data.csv_to_json as freshdata
from flask import Flask, render_template, request # for my flask app, app.route and to pass request from the flask form in html
from flask_restful import Resource, Api, reqparse # for my data
import pandas as pd #pandas used to open csv file
import json #convert csv to json then read file it later
import os #get current directory for file paths

app = Flask(__name__, template_folder="templates") # initiate that all html files to be rendered is in "templates" folder
api = Api(app)


@app.route("/")
def home():
    return render_template("index.html")

#ALL DRINKS
@app.route("/drinks")
def all_drinks():
    # Read your JSON File
    with open('data/drinks.json') as json_file:
        ALL_DRINKS = json.load(json_file)

    return render_template("drinks.html",allDrinks=ALL_DRINKS)

#TAKE TEST
@app.route("/getmydrinks")
def mydrinks():
    return render_template("getmydrinks.html")

#AFTER TEST
@app.route("/getmyresults" , methods=['GET','POST'])
def myresults():
    type_of_drinker = {
        "A": 'Zero to Minimal Alcohol Consumption',
        "B": 'Moderate Alcohol Consumption',
        "C": 'Low-Risk Drinking and Alcohol Use Disorder',
        "D": 'Binge Drinking',
        "E": 'Extreme Binge Drinking',
        "F": 'Heavy Drinking'
    }
    if request.method == 'GET':
        return render_template("getmydrinks.html")
    else:
        answer1 = request.form['q1']
        answer2 = request.form['q2']

        drinker_type = str(answer1)
        # SPECIAL CASES:
        if answer1 == 'B' and answer2 == 'B':
            drinker_type = "B"
        elif answer1 == 'B' and answer2 == 'C':
            drinker_type = "C"
        elif answer1 == 'E' and answer2 =='C':
            drinker_type = "F"

        drinker_description = str(type_of_drinker.get(drinker_type))

        # CALL SUGGESTION ENGINE
        freshdata.suggest(drinker_type)
        freshdata.suggest_healthy(drinker_type)

        #OPEN THE OUTPUT GENERATED
        json_suggesteddrinks_path = os.getcwd() + '\data\output\suggesteddrinks.json'
        json_healthierdrinks_path = os.getcwd() + '\data\output\healthierdrinks.json'

        with open(json_suggesteddrinks_path) as json_file:
            SUGGESTED_DRINKS = json.load(json_file)

        with open(json_healthierdrinks_path) as json_file:
            HEALTHIER_DRINKS = json.load(json_file)

        return render_template("results.html",
                               answer1=request.form['q1'],
                               answer2=request.form['q2'],
                               drinkerType=drinker_type,
                               drinkerDescription=drinker_description,
                               suggestedDrinks=SUGGESTED_DRINKS,
                               healthierDrinks=HEALTHIER_DRINKS)


#API CALLS
class Results(Resource):
    def post(self):
        return "Hello POST Results from getmydrinks.html DRINKER TYPE: ____, RECOMMENDATIONS: ____ ", 200
api.add_resource(Results, '/getmyresults')

if __name__ == "__main__":
    freshdata.create()
    app.run(debug=False) #default is false, set to true if needed