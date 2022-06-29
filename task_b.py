from connection import connect_to_db

conn, curr = connect_to_db()


def max_month(curr, year):
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