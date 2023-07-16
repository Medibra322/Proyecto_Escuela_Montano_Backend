from flask import Flask
from flask_cors import CORS

from src.models import *




app = Flask(__name__)
CORS(app)

@app.route("/")
def bienvenido():
    return "Bienvenido al proyecto Escuela Montaño"

#get all categories
@app.route("/categorias", methods=['GET'])
def all_categories():
    data = get_categories()
    return data

#delete one categorie by id
@app.route("/categorias/<idcat>", methods=['DELETE'])
def delete_category(idcat):
    delete_category_by_id(idcat)
    return ""

#Get all products grouped by category
@app.route("/productos/<idcat>", methods=['GET'])
def get_products(idcat):
    data = get_products_by_category(idcat)
    return data

#Get all products grouped by category
@app.route("/producto_by_id/<id>", methods=['GET'])
def get_product(id):
    data = get_product_by_id(id)
    return data

#Add a product
@app.route("/add_producto", methods=['POST'])
def new_product():
    add_producto()
    return ""

if __name__ == "__main__":
    app.run(debug=True)