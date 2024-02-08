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
SELECT SUM(result.new_cases)
FROM covid_deaths AS result,
    (SELECT location
    FROM covid_deaths AS t
    GROUP BY t.location
    HAVING AVG(t.new_cases) > 3) AS loc_avg
WHERE result.location = loc_avg.location
AND result.location IN (
    SELECT x.location
    FROM covid_deaths AS x,
        (SELECT date, MAX(population) AS maxP
        FROM covid_deaths AS c
        GROUP BY date) AS y
    WHERE x.date = y.date AND y.maxP = x.population
);""")


print(', '.join(str(row) for row in cursor.fetchall()))
