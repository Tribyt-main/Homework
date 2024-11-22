import sqlite3

connection = sqlite3.Connection("not_telegram_bot.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users(email) ")
age = 0
balance = 1000
for i in range(10):
    age += 10
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)',
                   (f'name{i}', f'example{i}@gmail.com', f'{age}', f'{balance}'))
connection.commit()
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in range(1, len(users), 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (f'{balance - 500}', user))
    connection.commit()

for user in range(1, len(users), 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (user,))
connection.commit()

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    if user[3] != 60:
        print(f'|{user[1]}|{user[2]}|{user[3]}|{user[4]}|')
connection.commit()
connection.close()
