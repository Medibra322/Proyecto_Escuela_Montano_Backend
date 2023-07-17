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

#Add a categoria - 
@app.route("/add_categoria", methods=['POST'])
def new_categoria():
    add_categoria()
    return "Categoria agregada"

#delete one categorie by id -
@app.route("/categorias/<idcat>", methods=['DELETE'])
def delete_category(idcat):
    delete_category_by_id(idcat)
    return "Category deleted"

#Get all products grouped by category
@app.route("/productos/<idcat>", methods=['GET'])
def get_products(idcat):
    data = get_products_by_category(idcat)
    return data

#Get one product - funciona
@app.route("/producto_by_id/<id>", methods=['GET'])
def get_product(id):
    data = get_product_by_id(id)
    return data

#Add a product - funciona
@app.route("/add_producto", methods=['POST'])
def new_product():
    add_producto()
    return ""

#Update one product - funciona
@app.route("/update_producto/<id>", methods=['PATCH'])
def update_product(id):
    data= update_producto(id)
    return data

#Delete one product - funciona
@app.route("/delete_producto/<id>", methods=['DELETE'])
def delete_product(id):
    delete_producto_by_id(id)
    return "Producto was deleted"


if __name__ == "__main__":
    app.run(debug=True)