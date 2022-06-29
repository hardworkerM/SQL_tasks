from connection import connect_to_db


conn, curr = connect_to_db()


def avg_sum(curr, age1, age2):
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
    result = curr.fetchall()
    return result[0][0]