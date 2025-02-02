from flask import Flask, render_template,jsonify,request
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



@app.route('item/buy/buyer/<int:item_id>')
def buyer_buy(item_id):
    try:
        connection = mysql.connector.connect(**DatabaseConfig.config_server)
        cursor = connection.cursor(buffered=True)
        cursor.execute('SELECT * FROM invetory WHERE ID = %s',(item_id,))
        item = cursor.fetchone()
    except:
        print('item was not available')
        return 'Server Error',500
    finally:
        cursor.close()
        connection.close()

    return render_template('buy_buyer.html',item = item)




@app.route('/item')
def buyer_homepage():
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

    return render_template('buyers_.html',
                           items=items,
                           page=page,
                           total_pages=total_pages,
                           )








# this our code will deduct the item on inventory maybe we should refactor this.
# we could add buyer details 
@app.route('/item/buy/user/<int:item_id>')
def buyer_will_buy(item_id):
    try:
        connection = mysql.connector.connect(**DatabaseConfig.config_server)
        cursor = connection.cursor(buffered=True)
        cursor.execute('SELECT balance FROM inventory WHERE id = %s', (item_id,))




        cursor.execute('UPDATE inventory SET in_qty = in_qty -1 WHERE id =%s',(item_id,))
        connection.commit()

        return jsonify({'message':f'tha you for buying this one'})

    except mysql.connector.Error as e:
        return jsonify({'error':f'Mysq error:{e}'}),500
    
    finally:
        if connection.is_connected():
           cursor.close()
           connection.close()


@app.route('/item')
def buyer_homepage():
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
