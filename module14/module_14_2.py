import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Users')

cursor.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)', (f'User{i}', f'example{i}@gmail.com', i*10, 1000))

cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 != 0')

cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)
    
connection.commit()
connection.close()

