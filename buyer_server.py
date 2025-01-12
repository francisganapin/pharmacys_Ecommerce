from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)
from server_side.connect_mysql_server import DatabaseConfig
import math



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

        per_page = 12
        page = request.args.get('page',1,type=int)
        total_pages = math.ceil(len(result)/per_page)

        start = (page -1) * per_page
        end = start + per_page
        items = result[start:end]

    except mysql.connector.Error as e:
            print(f'MySQL error: {e}')
    finally:
        print('cute')

    return render_template('buyers.html',
                           items=items,
                           page=page,
                           total_pages=total_pages,
                           )








if __name__ == '__main__':
    app.run(debug=True)
