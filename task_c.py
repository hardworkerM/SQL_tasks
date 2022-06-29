from connection import connect_to_db

conn, curr = connect_to_db()


def useful_item(curr):
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
