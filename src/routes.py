from flask import Flask
from flask_cors import CORS
from src.models import *




app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})


@app.route("/")
def bienvenido():
    return "Bienvenido al proyecto Escuela Montaño"

#get all categories - Funciona
@app.route("/categorias", methods=['GET'])
def all_categories():
    data = get_categories()
    return data

#Add a categoria - Funciona
@app.route("/add_categoria", methods=['POST'])
def new_categoria():
    add_categoria()
    return "Categoria agregada"

#delete one categorie by id - funciona
@app.route("/categorias/<idcat>", methods=['DELETE'])
def delete_category(idcat):
    delete_category_by_id(idcat)
    return "Category deleted"

#Get all products grouped by category - funciona
@app.route("/productos/<idcat>", methods=['GET'])
def get_products(idcat):
    data = get_products_by_category(idcat)
    return data

#Get one product - funciona
@app.route("/producto_by_id/<id>", methods=['GET'])
def get_product(id):
    data = get_product_by_id(id)
    return data

# Get all products -funciona
@app.route("/all_products", methods=['GET'])
def get_productos():
    data = get_todo_products()
    return data

#Add a product - funciona
@app.route("/add_producto", methods=['POST'])
def new_product():
    add_producto()
    return "Producto agregado"

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


##########Rutas Usuarios#############

#Add user - funciona
@app.route("/add_user", methods=['POST'])
def new_user():
    add_user()
    return "Usuario agregado"


#get one user by id - funciona
@app.route("/get_user/<id>", methods=['GET'])
def obtener_user(id):
    data = get_user(id)
    return data

#get all users - funciona
@app.route("/usuarios", methods=['GET'])
def all_users():
    data = get_usuarios()
    return data


#update one user by id - funciona
@app.route("/update_usuario/<id>", methods=['PATCH'])
def update_usuario_route(id):
    data = update_usuario(id)
    return data


#delete a user - funciona
@app.route("/delete_usuario/<id>", methods=['DELETE'])
def delete_usuario(id):
    delete_usuario_by_id(id)
    return "Usuario was deleted"


if __name__ == "__main__":
    app.run(debug=True)