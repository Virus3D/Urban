import sqlite3

def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS Products')

    cursor.execute('''
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    for i in range(1, 6):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?,?,?)', (f'Product{i}', f'описание{i}', i*100))

    connection.commit()
    connection.close()
    
def get_all_products():
    cursor = sqlite3.connect('database.db').cursor()
    query = cursor.execute('SELECT * FROM Products')
    colname = [ d[0] for d in query.description ]
    result_list = [ dict(zip(colname, r)) for r in query.fetchall() ]
    cursor.close()
    cursor.connection.close()
    return result_list