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
# cursor.execute("""
#     SELECT SUM(x.total_cases) - SUM(y.total_cases)
#     FROM covid_deaths AS x, covid_deaths AS y
#     WHERE x.date LIKE '%/02/%' AND y.date LIKE '%/_3/%'
#     ;""")
# (Decimal('19882294343775'),)


cursor.execute("""
    SELECT SUM(x.total_cases) - SUM(y.total_cases)
    FROM covid_deaths AS x, covid_deaths AS y
    WHERE MONTH(x.date)=2 AND MONTH(y.date) = 3
    ;""")
# (Decimal('19882294343775'),)

print(', '.join(str(row) for row in cursor.fetchall()))
