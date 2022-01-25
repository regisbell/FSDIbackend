
from flask import Flask, request, abort
from mock_data import catalog
import json 
import random
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # *DANGER* anyone can connect to this server

me = {
        "name": "Regis",
        "last": "Bell",
        "age": 32,
        "hobbies": ["reading", "listing to music"],
        "address": {
            "street": "Evergreen",
            "number": 42,
            "city": "Springfield",
        }
}


@app.route("/", methods = ['GET'])
def home():
    return "Hello from Python"

@app.route("/test")
def any_name():
    return "I'm a test function."


# return the full name getting the values from the dictionary
@app.route("/about")
def practice():
    return me["name"] + " " + me["last"]


#***************************************
#*******API ENDPOINTS*******************
#***************************************




@app.route("/api/catalog")
def get_catalog():
    test = db.products.find({})
    print(test)

    return json.dumps(catalog)


@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    print (product)

    # assign unique _id
    

    # save the product n the catalog
    catalog.append(product)

    
    db.products.insert_one(product)

    print("-----SAVED-----")
    print(product)

    return  json.dumps(product)

@app.route("/api/cheapest")
def get_cheapest():
    # find the cheapest product on the catalog list 
    cheapest = catalog[0]
    for product in catalog:
        if product["price"] < cheapest["price"]:
            cheapest = product
    

    # return it as json
    return json.dumps(cheapest)


@app.route("/api/product/<id>")
def get_product(id):
    # find the product whose _id is equal to id
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)

    #return it as json
    return "NOT FOUND"

# endpoint to retrieve all the products by category
# you should receive the cat. name,
# return all the products that belong to that category
@app.route("/api/catalog/<category>")
def get_by_category(category):
    result = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower() == category:
            result.append(product)

    return json.dumps(result)

# /api/categories
# return the list of unique category names
@app.route("/api/categories")    
def get_categories():
    result = []
    for product in catalog:
        cat = product["category"]

        if cat not in result:
            result.append(cat)

    return json.dumps(result)

# /api/reports/prodCount
@app.route("/api/reports/prodCount")
def get_prod_count():
    count = len(catalog)
    return json.dumps(count)

@app.route("/api/reports/total")
def get_total():
    total = 0

    # print the title of each product
    for prod in catalog:
        totalProd = prod["price"] * prod["stock"]
        total += totalProd

    return json.dumps(total)

@app.route("/api/reprts/highestInvestment")
def get_highestInvestment():
    # find the cheapest product on the catalog list 
    highest = catalog[0]
    for prod in catalog:
        prod_invest = prod["price"] * prod["stock"]
        high_invest =  highest["price"] * highest["stock"]

        if prod_invest > high_invest:
            highest = prod
    

    # return it as json
    return json.dumps(highest)



# start the server
app.run(debug = True)
