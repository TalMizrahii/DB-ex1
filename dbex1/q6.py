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

# Assuming that the average is the general average of new_cases in the table (NO A% locations).
# Obviously, we will get all continent, since the average is on the total number of rows, and NOT for the average
# of the sum per continent.
# Implemented as asked in the course site.
cursor.execute("""
        SELECT continent
        FROM (
            SELECT continent, SUM(new_cases) as total_new_cases
            FROM covid_deaths AS x
            WHERE x.location NOT LIKE 'A%'
            GROUP BY continent
        ) AS y
        WHERE total_new_cases > (
            SELECT AVG(new_cases)
            FROM covid_deaths AS x
            WHERE x.location NOT LIKE 'A%'
        )
    ;""")

print(', '.join(str(row) for row in cursor.fetchall()))
