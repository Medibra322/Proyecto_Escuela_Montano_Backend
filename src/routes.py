from flask import Flask
from flask_cors import CORS

from src.models import *



app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    data = get_categories()
    return data

if __name__ == "__main__":
    app.run(debug=True)