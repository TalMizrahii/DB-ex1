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
    SELECT continent
    FROM (
        SELECT continent, SUM(new_cases) as total_new_cases
        FROM covid_deaths AS x
        WHERE x.location NOT LIKE 'A%'
        GROUP BY continent
    ) AS y
        WHERE total_new_cases > (
        SELECT AVG(total_new_cases)
        FROM (
            SELECT continent, SUM(new_cases) as total_new_cases
            FROM covid_deaths
            WHERE location NOT LIKE 'A%'
            GROUP BY continent
        ) AS x)
    ;""")

print(', '.join(str(row) for row in cursor.fetchall()))
