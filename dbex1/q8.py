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
    FROM covid_deaths
    GROUP BY continent
    HAVING AVG(new_cases) > 
        (SELECT AVG(new_cases)
        FROM covid_deaths
        WHERE population < (
            SELECT AVG(population)
            FROM covid_db.covid_deaths))
     ;""")


print(', '.join(str(row) for row in cursor.fetchall()))
