"""У меня есть SQL база с таблицами:
1) Users(userId, age)
2) Purchases (purchaseId, userId, itemId, date)
3) Items (itemId, price).

Напишите SQL запросы для расчета следующих метрик:

a) какую сумму в среднем в месяц тратит:
- пользователи в возрастном диапазоне от 18 до 25 лет включительно
- пользователи в возрастном диапазоне от 26 до 35 лет включительно
b) в каком месяце года выручка от пользователей в возрастном диапазоне 35+ самая большая
c) какой товар обеспечивает  наибольший вклад в выручку за последний год
d) топ-3 товаров по выручке и их доля в общей выручке за любой год"""


from connection import connect_to_db
conn, curr = connect_to_db()


"""А) какую сумму в среднем в месяц тратит:
- пользователи в возрастном диапазоне от 18 до 25 лет включительно
- пользователи в возрастном диапазоне от 26 до 35 лет включительно"""


def task_a(curr, age1, age2):
    curr.execute(f"""SELECT AVG(a.summa)
                     FROM (
                            SELECT SUM(i.price) AS summa, strftime('%Y-%m', p.date) AS date
                            FROM Items i
                            JOIN Purchases p 
                            ON p.ItemId = i.itemId
                            WHERE p.userId IN (SELECT u.userId FROM Users u WHERE u.age BETWEEN {age1} and {age2})
                            GROUP BY strftime('%Y-%m', p.date)
                            ) AS a          
            """)
    res = curr.fetchall()
    return res[0][0]


"""B) в каком месяце года выручка от пользователей в возрастном диапазоне 35+ самая большая"""


def task_b(curr, year):
    curr.execute(f"""SELECT A.month
                    FROM (
                            SELECT SUM(i.price) AS number, 
                                    strftime('%m', p.date) AS month
                            FROM Items i
                            JOIN Purchases p
                            ON p.itemId = i.itemId
                            WHERE strftime('%Y', p.date) = '{year}'
                            AND p.userId = (SELECT userId FROM Users u WHERE u.age >= 35)
                            GROUP BY strftime('%m', p.date)
                            ) AS A
                    ORDER BY A.number DESC
                    LIMIT 1;
                """)
    res = curr.fetchall()
    return res[0][0]


"""C) какой товар обеспечивает/дает наибольший вклад в выручку за последний год"""


def task_с(curr):
    curr.execute("""
                    SELECT a.item
                    FROM (
                            SELECT SUM(i.price) as summa, i.itemId as item
                            FROM Items i
                            JOIN Purchases p
                            ON   i.itemId = p.itemId
                            WHERE strftime('%Y-%m-%d', p.date) 
                            BETWEEN strftime('%Y-%m-%d', 'now', '-1 year') 
                            AND strftime('%Y-%m-%d', 'now') 
                            GROUP BY i.itemId
                            ) AS a
                    ORDER BY a.summa DESC
                    LIMIT 1;
            """)
    res = curr.fetchall()
    return res[0][0]


"""D) топ-3 товаров по выручке и их доля в общей выручке за любой год"""


def task_d(curr, year):
    curr.execute(f"""
                    SELECT a.item, a.summa
                    FROM (
                            SELECT SUM(i.price) as summa, i.itemId as item
                            FROM Items i
                            JOIN Purchases p
                            ON   i.itemId = p.itemId
                            WHERE strftime('%Y', p.date) = '{year}'
                            GROUP BY i.itemId
                            ) AS a
                    ORDER BY a.summa DESC
                    LIMIT 3;
            """)
    res = curr.fetchall()
    return res


def show_top3(top):
    for i in top:
        print(f'Индекс - {i[0]}, сумма - {i[1]}')


if __name__ == '__main__':
    print(f'Задание A: \n'
          f'Пользователь в диапазоне\n'
          f'18-25 {task_a(curr, 18, 25)} \n'
          f'26-35 {task_a(curr, 26, 35)}\n')
    print(f'Задание B:\n'
          f'Самая большая выручка в от людей 35+\n'
          f'Была в  {task_b(curr, 2020)} месяце, 2020 года\n')
    print(f'Задание С:\n'
          f'Наибольший вклад в выручку за последний год принёс\n'
          f'Товар под индексом {task_с(curr)}\n')
    print(f'Задание D:\n'
          f'Топ три товара за 2020:')
    show_top3(task_d(curr, 2020))

