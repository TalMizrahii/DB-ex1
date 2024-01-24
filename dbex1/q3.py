import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="covid_db",
        port='3307',
    )
cursor = mydb.cursor()

cursor.execute("""
    SELECT AVG(y.new_tests)
    FROM (
        SELECT date, AVG(positive_rate) AS day_avg
        FROM covid_vaccination
        WHERE new_tests <> '' AND positive_rate <> ''
        GROUP BY date
    ) AS x,
    covid_vaccination AS y
    WHERE y.new_tests <> ''
        AND y.positive_rate <> ''
        AND y.date = x.date
        AND y.positive_rate > x.day_avg
    ;""")

# (Decimal('28727.4124'),)

print(', '.join(str(row) for row in cursor.fetchall()))
