import mysql.connector

def connectdb():
    try:
        conn = mysql.connector.connect(
            host='containers-us-west-112.railway.app',
            port=7521,
            user='root',
            password='EVmAebrs7eckR1vJm8Dh',
            database='railway'
    )
        print('Connecting to MontañoDB')

    except Exception as e:
        print(f'Error connecting to MontañoDB: {e}')

    return conn

connectdb()