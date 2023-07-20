from flask import Flask, jsonify, request
from flask_cors import CORS
from utils.jwt import encode_jwt, decode_jwt
from src.models import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def bienvenido():
    return "Bienvenido al proyecto Escuela Montaño"

# Ruta para el inicio de sesión (autenticación)
@app.route("/login", methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Verificar si el correo electrónico y la contraseña son válidos en la base de datos
        user = verify_user_credentials(email, password)
        if user is None:
            return jsonify({'message': 'Credenciales inválidas'}), 401

        # Si las credenciales son válidas, generar el token JWT
        token = encode_jwt({'user_id': user.id, 'email': user.email})

        # Devolver el token JWT al cliente
        return jsonify({'token': token}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Ruta protegida - Solo accesible si se proporciona un token JWT válido
@app.route("/intranet", methods=['GET'])
def intranet():
    try:
        # Verificar el token JWT antes de permitir el acceso
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token de autenticación faltante'}), 401

        # Verificar el token JWT y obtener el usuario autenticado
        decoded_token = decode_jwt(token)
        # Aquí deberías verificar que el token es válido y contiene la información adecuada para autenticar al usuario.
        # Por ejemplo, puedes verificar el ID del usuario o su rol.

        # Si el token es válido, se permite el acceso a la zona protegida
        return jsonify({'message': 'Bienvenido a la zona protegida'}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 400








#get all categories
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