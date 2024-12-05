import sqlite3

from Module_14.module_14_4 import product1


def initiate_db():
    connection = sqlite3.connect('initiate_db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products
    (id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)',
                       (f'Название: Product{i}', f'Описание: описание {i}', f'Цена: {i * 100}'))
    cursor.execute('DELETE from Products')
    connection.commit()
    connection.close()


connection = sqlite3.connect('initiate_db')
cursor = connection.cursor()
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
