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
    SELECT AVG(new_tests)
    FROM covid_vaccination AS x
    WHERE new_tests <> ''
        AND positive_rate <> ''
        AND positive_rate > (SELECT AVG(positive_rate) 
                                FROM covid_vaccination AS y
                                WHERE new_tests <> '' AND positive_rate <> '')
    ;""")

# (Decimal('33455.7899'),)

print(', '.join(str(row) for row in cursor.fetchall()))
