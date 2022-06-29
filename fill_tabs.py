import random
from connection import connect_to_db


def create_tabs():
    conn, curr = connect_to_db()
    curr.execute('CREATE TABLE IF NOT EXISTS Users(userId int, age int)')
    curr.execute('CREATE TABLE IF NOT EXISTS Purchases (purchaseId int, userId int, itemId int, date date)')
    curr.execute('CREATE TABLE IF NOT EXISTS  Items (itemId int, price DECIMAL(8, 2))')
    fill_tabs(curr)
    conn.commit()


def fill_tabs(curr):
    for i in range(10000):
        insert_into(curr, 'Users', fill_user(i))
        insert_into(curr, 'Purchases', fill_purchase(i))
        insert_into(curr, 'Items', fill_item(i))
    show_result(curr)


def fill_user(i):
    age = [i for i in range(16, 78)]
    user = (i, random.choice(age))
    return user


def fill_item(i):
    price = random.randint(1000, 10000)
    item = (i, price)
    return item


def fill_purchase(i):
    purchaseId = i
    userId = random.randint(0, 10000)
    itemId = random.randint(0, 10000)
    date = make_date()
    purchase = (purchaseId, userId, itemId, date)
    return purchase


def make_date():
    y = random.choice([i for i in range(2018, 2022)])
    m = random.choice([f'{i}' if i > 9 else f'0{i}' for i in range(1, 13)])
    d = random.choice([f'{i}' if i > 9 else f'0{i}' for i in range(1, 28)])
    date = f'{y}-{m}-{d}'
    return date


def insert_into(curr, tab_name, element):
    curr.execute(f"INSERT INTO {tab_name} VALUES {element}")


def show_result(curr):
    curr.execute("""SELECT *
                    FROM Purchases
                    LIMIT 10
                """)
    nb = curr.fetchall()
    print(nb)


if __name__ == '__main__':
    create_tabs()
