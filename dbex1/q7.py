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
# I assume the MONTH checks all valid date formats.
cursor.execute("""
    SELECT
        location,
        AVG(month_sum) AS avg,
        MAX(month_sum) AS max_monthly,
        MIN(month_sum) AS min_monthly
    FROM
        (SELECT location, MONTH(date) AS month, SUM(new_cases) AS month_sum
        FROM covid_deaths
        GROUP BY location, MONTH(date)) AS z
    GROUP BY
        location;
     ;""")

print(', '.join(str(row) for row in cursor.fetchall()))
