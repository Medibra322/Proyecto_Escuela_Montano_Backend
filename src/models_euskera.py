from flask import jsonify, request
from database.db import connectdb

# Obtain all categories

def get_categories_eus():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM kategoriak')
    categorias = cur.fetchall()
    data = [{'idcat': dato[0], 'descripcion': dato[1]} for dato in categorias]
    conn.close()
    return jsonify(data)

def delete_category_by_id(idcat):
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('DELETE FROM kategoriak WHERE idcat = %s', (idcat,))
    conn.commit()
    conn.close()
    print("The category was deleted !!")
    return ""