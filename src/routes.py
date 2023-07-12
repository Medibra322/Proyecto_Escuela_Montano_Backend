from flask import Flask
from flask_cors import CORS

from src.models import *
from src.models_euskera import *



app = Flask(__name__)
CORS(app)

@app.route("/")
def bienvenido():
    return "Bienvenido al proyecto Escuela Montaño"

#get all categories in spanish
@app.route("/categorias", methods=['GET'])
def all_categories():
    data = get_categories()
    return data

#get all categories in basque
@app.route("/kategoriak", methods=['GET'])
def all_categories_eus():
    data = get_categories_eus()
    return data

#delete one categorie by id
@app.route("/kategoriak/<idcat>", methods=['DELETE'])
def delete_category_eus(idcat):
    delete_category_by_id(idcat)
    return ""

if __name__ == "__main__":
    app.run(debug=True)