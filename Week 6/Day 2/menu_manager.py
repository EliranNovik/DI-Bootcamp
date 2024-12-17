import psycopg2

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        try:
            connection = psycopg2.connect(
                dbname='menues',
                user='postgres',
                password='',
                host='localhost',
                port='5432'
            )
            cursor = connection.cursor()
            query = "SELECT * FROM Menu_items WHERE name = %s;"
            cursor.execute(query, (name,))
            result = cursor.fetchone()
            if result:
                return {'name': result[0], 'price': result[1]}
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()

    @classmethod
    def all_items(cls):
        try:
            connection = psycopg2.connect(
                dbname='menues',
                password='',
                host='localhost',
                port='5432'
            )
            cursor = connection.cursor()
            query = "SELECT * FROM Menu_items;"
            cursor.execute(query)
            results = cursor.fetchall()
            return [{'name': item[0], 'price': item[1]} for item in results]
        except Exception as e:
            print(f"Error: {e}")
        finally:
            connection.close()
