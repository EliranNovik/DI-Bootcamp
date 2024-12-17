import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        try:
            connection = psycopg2.connect(
                dbname='menues',
                user='postgres',
                password='',
                host='localhost',
                port='5432'
            )
            cursor = connection.cursor()
            query = "INSERT INTO Menu_items (name, price) VALUES (%s, %s);"
            cursor.execute(query, (self.name, self.price))
            connection.commit()
            print("Item saved successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()

    def delete(self):
        try:
            connection = psycopg2.connect(
                dbname='menues',
                user='postgres',
                password='',
                host='localhost',
                port='5432'
            )
            cursor = connection.cursor()
            query = "DELETE FROM Menu_items WHERE name = %s;"
            cursor.execute(query, (self.name,))
            connection.commit()
            print("Item deleted successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()

    def update(self, new_name, new_price):
        try:
            connection = psycopg2.connect(
                dbname='menues',
                user='postgres',
                password='',
                host='localhost',
                port='5432'
            )
            cursor = connection.cursor()
            query = "UPDATE Menu_items SET name = %s, price = %s WHERE name = %s;"
            cursor.execute(query, (new_name, new_price, self.name))
            connection.commit()
            print("Item updated successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()
