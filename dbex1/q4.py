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
    SELECT date, SUM(new_vaccinations) as daily_vaccinations
    FROM covid_vaccination
    WHERE continent = 'Asia'
    GROUP BY date
    HAVING daily_vaccinations > 20000000
    ;""")

#('01/06/21', Decimal('25873915')), ('01/07/21', Decimal('29279061')), ('02/06/21', Decimal('28590696')), ('02/07/21', Decimal('22808660')), ('03/06/21', Decimal('24640253')), ('03/07/21', Decimal('23811836')), ('04/06/21', Decimal('28994344')), ('05/06/21', Decimal('22485673')), ('07/06/21', Decimal('22293346')), ('08/06/21', Decimal('22130616')), ('09/06/21', Decimal('22823265')), ('10/06/21', Decimal('28262588')), ('11/06/21', Decimal('25783103')), ('12/06/21', Decimal('20677004')), ('13/06/21', Decimal('20287639')), ('15/06/21', Decimal('27361693')), ('16/06/21', Decimal('30454414')), ('17/06/21', Decimal('32392448')), ('18/06/21', Decimal('32527629')), ('19/06/21', Decimal('28304768')), ('20/05/21', Decimal('20634584')), ('20/06/21', Decimal('25813524')), ('21/06/21', Decimal('33757265')), ('22/06/21', Decimal('32065065')), ('23/06/21', Decimal('31338400')), ('24/05/21', Decimal('20728068')), ('24/06/21', Decimal('35845215')), ('25/05/21', Decimal('23784262')), ('25/06/21', Decimal('34147209')), ('26/05/21', Decimal('24870986')), ('26/06/21', Decimal('32942715')), ('27/05/21', Decimal('23163775')), ('27/06/21', Decimal('27657095')), ('28/05/21', Decimal('22904213')), ('28/06/21', Decimal('28305174')), ('29/05/21', Decimal('23272039')), ('29/06/21', Decimal('29585936')), ('30/05/21', Decimal('21116784')), ('30/06/21', Decimal('25422029')), ('31/05/21', Decimal('26481219'))

print(', '.join(str(row) for row in cursor.fetchall()))
