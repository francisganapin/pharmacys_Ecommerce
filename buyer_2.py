from flask import Flask, render_template, request
import mysql.connector
import math
import logging
from server_side.connect_mysql_server import DatabaseConfig

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/item')
def items():
    try:
        connection = mysql.connector.connect(**DatabaseConfig.config_server)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM inventory')
        results = cursor.fetchall()
    except mysql.connector.Error as e:
        logging.error(f"MySQL error: {e}")
        return "Database connection failed", 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    # Pagination
    per_page = 12
    page = request.args.get('page', 1, type=int)
    total_pages = math.ceil(len(results) / per_page)

    start = (page - 1) * per_page
    end = start + per_page
    items = results[start:end]

    return render_template(
        'buyers.html',
        items=items,
        page=page,
        total_pages=total_pages,
    )

@app.route('/detail<int:result_id>')
def detail(result_id):
    try:
        connection = mysql.connector.connect(**DatabaseConfig.config_server)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM inventory WHERE id = %s', (result_id,))
        result = cursor.fetchone()
    except mysql.connector.Error as e:
        logging.error(f"MySQL error: {e}")
        return "Database connection failed", 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    if result:
        return render_template('detail.html', item=result)
    return 'Item not found', 404





if __name__ == '__main__':
    app.run(debug=True)
