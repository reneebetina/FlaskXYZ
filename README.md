To Run on your local:
1. Install Python
2. Install Python Libraries: pip install
flask
flask-restful
pandas
json

3. Go to main.py and run on your local
4. Flask app will start adn it will give you an address that you can open in your browser
Default: http://127.0.0.1:5000

Make sure that your local server is up and running to access this page.

Important Notes: 
THIS APP IS FOR DEMO PURPOSE ONLY.
This app is not connected to any database.
Data displayed is stored under /data folder. You can add new data there. 

LOGIC BEHIND THE DISPLAYED DRINKS
Input: list of drinks are stored under /data/drinks.csv

Process:
/data/drinks.csv is transformed to a json so that it will be displayed in frontend
Once user answers the test, the methods `suggest()` and `suggest_healthy()` will run

Output: 
Output will be stored under /data/ouput as csv files
output csv file will be transformed to a json and will be displayed in frontend