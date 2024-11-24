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
# age = 0
# balance = 1000
# for i in range(10):
#     age += 10
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?,?,?,?)',
#                    (f'name{i}', f'example{i}@gmail.com', f'{age}', f'{balance}')) #Запись в пустую базу.
# connection.commit()
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()
# for user in range(1, len(users), 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (f'{balance - 500}', user)) #Обновление данных.
#     connection.commit()
#
# for user in range(1, len(users), 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (user,))
# connection.commit()
#
# cursor.execute('SELECT * FROM Users') #Выбор всех (*).
# users = cursor.fetchall()
# for user in users:
#     if user[3] != 60:
#         print(f'|{user[1]}|{user[2]}|{user[3]}|{user[4]}|')
# connection.commit()

# cursor.execute('DELETE FROM Users WHERE id = ?', (6,))  #Удаление.
# cursor.execute('DELETE FROM Users WHERE id = ?', (10,))
# connection.commit()

cursor.execute('SELECT COUNT(*) FROM Users')
count_ = cursor.fetchone()[0]
print(count_)
cursor.execute('SELECT SUM(balance) FROM Users')
sum_ = cursor.fetchone()[0]
print(sum_)
cursor.execute('SELECT AVG(balance) FROM Users')
avg_ = cursor.fetchone()[0]
print(avg_)
connection.close()
