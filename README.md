Author: [@reneebetina](https://github.com/reneebetina)

<h2>PROJECT XYZ</h2>

![sample_app_run](https://user-images.githubusercontent.com/24974238/208610255-34210768-495b-4a4a-b363-69b454cc4386.png)
 
 - THIS APP IS FOR DEMO ONLY.
 
 - This is a sample Flask App and it determine your alcohol behavior type
 
 - Logic to determine drinker type and suggested drinks are explained in the table at the end of this document


What is this project for?

- <h4> For New Drinkers:</h4> The app gives you a list of drinks that you can tolerate or might want to try


- <h4> For People with Alcoholism and want to Quit:</h4> The app gives you a list of healthier alternatives (lower alcohol content)

---
DEV NOTES
---
To Run on your local:
1. Install Python
2. Install additional Python Libraries: 
pip install
`flask`
`flask-restful`
`pandas`

3. Go to `main.py` and run on your local
4. Flask app will start adn it will give you an address that you can open in your browser

Default Address: http://127.0.0.1:5000

<h3> Make sure that your local server is up and running to access this page. </h3>

* This app is not connected to any database.
* Data displayed is stored under /data folder. You can add new data there. 


<h1>LOGIC BEHIND THE DISPLAYED DRINKS</h1>

INPUT: list of drinks are stored under /data/drinks.csv


PROCESS: 
/data/drinks.csv is transformed to a json so that it will be displayed in frontend
Once user answers the test, the methods `suggest()` and `suggest_healthy()` will run

![image](https://user-images.githubusercontent.com/24974238/211728144-aaf64ba1-ec4d-4e88-a69f-74232c2d032b.png)


OUTPUT: 
Output will be stored under /data/ouput as csv files
output csv file will be transformed to a json and will be displayed in frontend
