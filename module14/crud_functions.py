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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
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

def add_user(username: str, email: str, age: int, balance: int = 1000):
    cursor = sqlite3.connect('database.db').cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)', (username, email, age, balance))
    cursor.connection.commit()
    cursor.close()
    cursor.connection.close()
    
def is_included(username: str):
    cursor = sqlite3.connect('database.db').cursor()
    query = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    result = query.fetchone()
    cursor.close()
    cursor.connection.close()
    if result:
        return True
    else: 
        return False
    