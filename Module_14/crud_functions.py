import sqlite3

connection = sqlite3.connect('initiate_db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products
    (id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)',
                       (f'Название: Product{i}', f'Описание: описание {i}', f'Цена: {i * 100}'))
    # cursor.execute('DELETE from Products')
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * From Products')
    result = cursor.fetchall()
    for i in result:
        print(i)


initiate_db()



cursor.execute('SELECT id, title, description, price FROM Products WHERE id = 1')
products = cursor.fetchone()
product_1 = (f'{products[1]} | {products[2]} | {products[3]}')
cursor.execute('SELECT id, title, description, price FROM Products WHERE id = 2')
products = cursor.fetchone()
product_2 = (f'{products[1]} | {products[2]} | {products[3]}')
cursor.execute('SELECT id, title, description, price FROM Products WHERE id = 3')
products = cursor.fetchone()
product_3 = (f'{products[1]} | {products[2]} | {products[3]}')
cursor.execute('SELECT id, title, description, price FROM Products WHERE id = 4')
products = cursor.fetchone()
product_4 = (f'{products[1]} | {products[2]} | {products[3]}')


def add_user(username, email, age, balance = 1000):
    check_user = cursor.execute('SELECT * FROM Users WHERE username =?', (username,))
    if check_user.fetchone() is None:
        cursor.execute(f'''
INSERT INTO Users VALUES('{username}', '{email}' , '{age}', 0)
''')


connection.commit()


def is_included(username):
    check_username = cursor.execute('SELECT * FROM Users WHERE username =?', (username,))
    if check_username.fetchone() is None:
        return False
    else:
        return True



