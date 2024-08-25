@app.route('/update', methods=['POST'])
def update_table():
    item_code_in = request.form.get('item_code')
    in_qty_in = request.form.get('in_qty')

    try:
        connection = mysql.connector.connect(**DatabaseConfig.config_server)
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM inventory WHERE item_code = %s', (item_code_in,))
        result = cursor.fetchone()

        if not result:
            logging.info(f'{item_code_in} does not exist')
            return render_template('update.html', message=f'{item_code_in} does not exist')

        cursor.execute('UPDATE inventory SET in_qty = %s WHERE item_code = %s', (in_qty_in, item_code_in))
        connection.commit()

        logging.info(f'Updated item_code: {item_code_in} to new quantity: {in_qty_in}')
        message = f'Successfully updated item_code {item_code_in} with new quantity {in_qty_in}.'

    except mysql.connector.Error as e:
        logging.error(f'MySQL error: {e}')
        message = 'An error occurred while updating the inventory.'

    finally:
        cursor.close()
        connection.close()

    return render_template('update.html', message=message)