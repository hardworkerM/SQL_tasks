from connection import connect_to_db

conn, curr = connect_to_db()

# Расчёты пока неверны

def top_3(curr, year):
    curr.execute(f"""
                    SELECT SUM(i.price)
                    FROM Items i
                    JOIN Purchases p
                    ON i.itemId = p.itemId

            """)
    res = curr.fetchall()
    return res


def top_3_2(curr, year):
    curr.execute(f"""SELECT top_items.itemId, INTEGER(top_items.amount*100 /  (SELECT SUM(i.price)
                                                                            FROM Items i
                                                                            JOIN Purchases p
                                                                            ON i.itemId = p.itemId))
                    FROM (SELECT i.itemId, SUM(i.price) AS amount
                            FROM  Items i
                            JOIN  Purchases p
                              ON  i.itemId = p.itemId
                            WHERE strftime('%Y', p.date) = '{year}'
                            GROUP BY i.itemId
                            ORDER BY amount DESC
                            LIMIT 3) AS top_items
            """)
    res = curr.fetchall()
    return res

print(top_3_2(curr, 2020))
