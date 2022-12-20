import csv
import json
import os

dirPath = os.getcwd() + '\data'

def getCurrentLimit(drinkerType):
    drinker_current_limit = {
        "A": 5,
        "B": 10,
        "C": 15,
        "D": 40,
        "E": 65,
        "F": 100
    }
    return float(drinker_current_limit.get(drinkerType))

def getHealthyLimit(drinkerType):
    #anything below
    drinker_healthy_limit = {
        "A": 4,
        "B": 9,
        "C": 12,
        "D": 15,
        "E": 20,
        "F": 30
    }
    return float(drinker_healthy_limit.get(drinkerType))

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

def create():
    csvFilePath = dirPath + '\drinks.csv'
    jsonFilePath = dirPath + '\drinks.json'
    csv_to_json(csvFilePath, jsonFilePath)

def suggest(drinkerType):
    #get Limit
    current_limit = getCurrentLimit(drinkerType)
    print("CURRENT LIMIT: ", current_limit)

    #construct CSV
    name = ""
    abv = 0
    res_string = ""
    res_line = {}
    list_of_dictionaries_res_line = []
    list_of_dictionaries_res_line_healty = []

    source_csvFilePath = dirPath + '\drinks.csv'
    with open(source_csvFilePath, mode='r', encoding='UTF-8') as file:
        for line in file.readlines():
            list_num = line.split(',')
            #print(list_num)
            name = list_num[0]
            abv = list_num[1].replace("\n","")
            # pass type to function

            res_line["name"] = str(name)
            res_line["abv"] = str(abv)

            # Conditional Insertion:
            if abv.isalpha():
                list_of_dictionaries_res_line.append(res_line)

            if abv.isalpha()==False and float(res_line["abv"]) <= current_limit:
                    list_of_dictionaries_res_line.append(res_line)

            # always reset res_line so new entry will not overwrite the existing
            res_line={}
        print(list_of_dictionaries_res_line)
    try:
        if len(list_of_dictionaries_res_line)==0:
            raise Exception("Custom ERROR - nothing to write ", sys.stderr)

        #declare keys aligned to exact keys you used in your dictionary
        keys = ["name","abv"]
        # Python 3 syntax in writing files, mode=w and newline='' are REQUIRED

        destination1_csvFilePath = dirPath + '\output\suggesteddrinks.csv'
        destination1_jsonFilePath = dirPath + '\output\suggesteddrinks.json'

        with open(destination1_csvFilePath, mode='w', newline='') as wfile:
            writer = csv.DictWriter(wfile,fieldnames=keys)
            print("INFO: Now writing to csv ... ")
            #writer.writeheader()
            # for debugging purposes you can check print all rows to be written using WRITEROWS
            for pos in list_of_dictionaries_res_line:
                print(pos)
            #dictwriter only accepts dictionary so make sure your list_of_dictionaries is correct and complete
            writer.writerows(list_of_dictionaries_res_line)
            print("INFO: Writing Complete!")

        # OUTPUT 1
        csv_to_json(destination1_csvFilePath,destination1_jsonFilePath)

    except Exception as e :
        print("***Error encountered: ", e)


def suggest_healthy(drinkerType):
    # get Limit
    healthy_limit = getHealthyLimit(drinkerType)
    print("HEALTHY LIMIT: ", healthy_limit)

    # construct CSV
    name = ""
    abv = 0
    res_string = ""
    res_line = {}
    list_of_dictionaries_res_line = []
    list_of_dictionaries_res_line_healty = []

    source_csvFilePath = dirPath + '\drinks.csv'
    with open(source_csvFilePath, mode='r', encoding='UTF-8') as file:
        for line in file.readlines():
            list_num = line.split(',')
            # print(list_num)
            name = list_num[0]
            abv = list_num[1].replace("\n", "")
            # pass type to function

            res_line["name"] = str(name)
            res_line["abv"] = str(abv)

            # Conditional Insertion:
            if abv.isalpha():
                list_of_dictionaries_res_line.append(res_line)

            if abv.isalpha() == False and float(res_line["abv"]) <= healthy_limit:
                list_of_dictionaries_res_line.append(res_line)

            # always reset res_line so new entry will not overwrite the existing
            res_line = {}
        print(list_of_dictionaries_res_line)
    try:
        if len(list_of_dictionaries_res_line) == 0:
            raise Exception("Custom ERROR - nothing to write ", sys.stderr)

        # declare keys aligned to exact keys you used in your dictionary
        keys = ["name", "abv"]
        # Python 3 syntax in writing files, mode=w and newline='' are REQUIRED

        destination1_csvFilePath = dirPath + '\output\healthierdrinks.csv'
        destination1_jsonFilePath = dirPath + '\output\healthierdrinks.json'

        with open(destination1_csvFilePath, mode='w', newline='') as wfile:
            writer = csv.DictWriter(wfile, fieldnames=keys)
            print("INFO: Now writing to csv ... ")
            # writer.writeheader()
            # for debugging purposes you can check print all rows to be written using WRITEROWS

            for pos in list_of_dictionaries_res_line:
                print(pos)
            # dictwriter only accepts dictionary so make sure your list_of_dictionaries is correct and complete
            writer.writerows(list_of_dictionaries_res_line)
            print("INFO: Writing Complete!")

        # OUTPUT 1
        csv_to_json(destination1_csvFilePath, destination1_jsonFilePath)

    except Exception as e:
        print("***Error encountered: ", e)




if __name__ == "__main__":
    create()
    suggest()