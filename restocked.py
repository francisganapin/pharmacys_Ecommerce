@app.route('/update', methods=['GET', 'POST'])
def update_table():
    item_code_in = request.form.get('item_code')
    in_qty_in = int(request.form.get('in_qty'))  # Convert to integer
    Restocked = 'Restocked' 
    Destocked = 'Destocked'

    try:
        connection = mysql.connector.connect(**DatabaseConfig.config_server)
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM inventory WHERE item_code = %s', (item_code_in,))
        result = cursor.fetchone()

        if not result:
            print(f'{item_code_in} does not exist')
            return render_template('update.html', message=f'{item_code_in} does not exist')

        cursor.execute('SELECT in_qty FROM inventory WHERE item_code = %s', (item_code_in,))
        result2 = cursor.fetchone()

        current_qty = result2[0]  # Fetch the current quantity from the result

        if in_qty_in > current_qty:
            cursor.execute(
                'UPDATE inventory SET in_qty = %s, remarks = %s WHERE item_code = %s',
                (in_qty_in, Restocked, item_code_in)
            )
            connection.commit()
            print(f'Updated item_code: {item_code_in} to new quantity: {in_qty_in} and restocked')
            message = f'Successfully updated item_code {item_code_in} with new quantity {in_qty_in}.'
        else:
            cursor.execute(
                'UPDATE inventory SET in_qty = %s, remarks = %s WHERE item_code = %s',
                (in_qty_in, Destocked, item_code_in)
            )
            connection.commit()
            print(f'Updated item_code: {item_code_in} to new quantity: {in_qty_in} and destocked')
            message = f'Successfully updated item_code {item_code_in} with new quantity {in_qty_in}.'

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        message = f"An error occurred: {err}"
    finally:
        cursor.close()
        connection.close()

    return render_template('update.html', message=message)
