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
    SELECT SUM(new_cases)
    FROM covid_deaths AS result
    WHERE result.location IN (
        SELECT z.location
        FROM covid_deaths AS z
        GROUP BY z.location
        HAVING AVG(z.new_cases) > 3
    ) AND result.location IN (
        SELECT x.location
        FROM covid_deaths AS x,
            (SELECT date, MAX(population) AS maxP
                FROM covid_deaths AS c
                GROUP BY date
            ) AS y
        WHERE x.date = y.date AND y.maxP = x.population)
    ;""")


print(', '.join(str(row) for row in cursor.fetchall()))
