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
        SELECT x.date, x.new_cases, x.location
        FROM (
            SELECT date, new_cases, location
            FROM covid_deaths
            LIMIT 1000
        ) AS x, (
            SELECT date, new_cases, location
            FROM covid_deaths
            LIMIT 1000
        ) AS y
        WHERE x.date = y.date
            AND x.new_cases > 1000
            AND x.new_cases = y.new_cases
            AND x.location < y.location
    ;""")

# Empty

print(', '.join(str(row) for row in cursor.fetchall()))
