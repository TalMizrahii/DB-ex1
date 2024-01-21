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
                SELECT COUNT(total_cases)
                FROM covid_deaths as x
                               """)

print(', '.join(str(row) for row in cursor.fetchall()))
