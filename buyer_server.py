from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)
from server_side.connect_mysql_server import DatabaseConfig



import logging



# Configure logging
logging.basicConfig(level=logging.INFO)



@app.route('/')
def homepage():
    return render_template('homepage.html')



@app.route('/navbar')
def navbar():
    return render_template('navbar.html')



@app.route('/item')
def hello():
    try:
        connection = mysql.connector.connect(**DatabaseConfig.config_server)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM inventory')
        result = cursor.fetchall()

    except mysql.connector.Error as e:
            print(f'MySQL error: {e}')
    finally:
        print('cute')

    return render_template('index.html',result=result)








if __name__ == '__main__':
    app.run(debug=True)
