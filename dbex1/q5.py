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
    SELECT SUM(x.new_cases)
    FROM covid_deaths AS x
    WHERE x.location = (
        SELECT y.location
        FROM covid_deaths AS y
        GROUP BY y.location
        ORDER BY MAX(y.population) DESC
        LIMIT 1
    )
    AND x.location IN (
        SELECT z.location
        FROM covid_deaths AS z
        GROUP BY z.location
        HAVING AVG(z.new_cases) > 3
    )
    ;""")


print(', '.join(str(row) for row in cursor.fetchall()))
