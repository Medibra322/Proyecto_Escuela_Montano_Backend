from flask import jsonify, request
from database.db import connectdb

# Obtain all categories

def get_categories():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM categorias')
    categorias = cur.fetchall()
    data = [{'idcat': dato[0], 'descripcion': dato[1]} for dato in categorias]
    conn.close()
    return jsonify(data)