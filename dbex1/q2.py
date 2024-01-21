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
        SELECT x.date, x.new_cases, x.location
        FROM (
            SELECT date, new_cases, location
            FROM covid_deaths
            WHERE new_cases > 1000
        ) AS x, (
            SELECT date, location, new_cases
            FROM covid_deaths
            WHERE new_cases > 1000
        ) AS y
        WHERE x.date = y.date
            AND x.new_cases = y.new_cases
            AND x.location < y.location
    ;""")

print(', '.join(str(row) for row in cursor.fetchall()))


# ('13/07/20', 3099, 'Argentina'), ('20/05/21', 1457, 'Bangladesh'), ('21/05/21', 2858, 'Bahrain'), ('11/11/20', 1202, 'Azerbaijan'), ('13/04/21', 1060, 'Bahrain'), ('31/12/20', 2254, 'Belgium'), ('25/03/21', 1429, 'Azerbaijan'), ('22/10/20', 1595, 'Bulgaria'), ('19/05/21', 1160, 'Egypt'), ('24/07/20', 1091, 'France'), ('16/04/21', 1973, 'Ethiopia'), ('11/11/20', 3945, 'Bulgaria'), ('01/02/21', 1124, 'Austria'), ('11/08/20', 1693, 'Bolivia'), ('26/11/20', 1085, 'Algeria'), ('28/03/21', 1783, 'Ecuador'), ('10/10/20', 1235, 'Austria'), ('24/10/20', 1820, 'Hungary'), ('27/03/21', 1690, 'Azerbaijan'), ('08/06/21', 1581, 'Guatemala'), ('25/04/21', 1324, 'Ethiopia'), ('07/04/21', 1120, 'Bahrain'), ('23/01/21', 1074, 'Ecuador'), ('16/05/21', 1233, 'Cuba'), ('22/01/21', 1138, 'Honduras'), ('25/11/20', 1330, 'Costa Rica'), ('21/01/21', 1071, 'Guatemala'), ('27/11/20', 1621, 'Belarus'), ('29/06/21', 1746, 'Ecuador'), ('08/09/20', 1136, 'Ethiopia'), ('04/05/21', 1304, 'Costa Rica'), ('04/03/21', 1019, 'Botswana'), ('04/05/21', 1914, 'Bangladesh'), ('12/05/21', 1539, 'Bahrain'), ('01/05/21', 1615, 'Austria'), ('07/02/21', 6670, 'Germany'), ('17/11/20', 1255, 'Bosnia and Herzegovina'), ('12/01/21', 3243, 'Chile'), ('26/04/21', 1759, 'Bulgaria'), ('12/03/21', 1357, 'Estonia'), ('26/06/21', 1279, 'Honduras'), ('24/04/21', 1259, 'Jordan'), ('28/12/20', 1594, 'Lebanon'), ('31/12/20', 1861, 'Latvia'), ('30/03/21', 1271, 'Kuwait'), ('27/03/21', 1199, 'Malaysia'), ('20/01/21', 1088, 'Latvia'), ('08/02/21', 1685, 'Jordan'), ('15/02/21', 1331, 'Romania'), ('16/01/21', 2045, 'Philippines'), ('09/10/20', 1461, 'Myanmar'), ('28/12/20', 7458, 'Netherlands'), ('30/06/20', 1293, 'Indonesia'), ('23/09/20', 1767, 'Romania'), ('13/06/21', 1019, 'Pakistan'), ('27/06/21', 1007, 'Namibia'), ('28/01/21', 1408, 'Panama'), ('29/06/21', 1249, 'Panama'), ('28/03/21', 2128, 'United Arab Emirates')