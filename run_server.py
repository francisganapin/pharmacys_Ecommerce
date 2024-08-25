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



@app.route('/update',  methods=['GET', 'POST'])
def update_table():
    item_code_in = request.form.get('item_code')
    in_qty_in = request.form.get('in_qty')

    try:
        connection = mysql.connector.connect(**DatabaseConfig.config_server)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM inventory where item_code = %s',(item_code_in,))
        result = cursor.fetchone()

        if not result:
            print(f'{item_code_in} does not exist')
            return render_template('update.html', message=f'{item_code_in} does not exist')


        cursor.execute('UPDATE inventory SET in_qty = %s WHERE item_code =%s',(in_qty_in,item_code_in,))
        connection.commit()

        print(f'Updated item_code: {item_code_in} to new quantity: {in_qty_in}')
        message = f'Successfully updated item_code {item_code_in} with new quantity {in_qty_in}.'

    except mysql.connector.Error as e:
            print(f'MySQL error: {e}')
            message=f''
    finally:
        cursor.close()
        connection.close()

    return render_template('update.html',message=message)



if __name__ == '__main__':
    app.run(debug=True)
