import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3306',
    password='futbol77',
    database='axb2024'
)

cursor = connection.cursor()
# cursor.execute('''delete from person where salary<150000''')

cursor.execute('''update car set  first_name = 'Karim' where age < 24 ''')

connection.commit()
cursor.execute('''select * from car where age < 20 ''')

a = cursor.fetchall()

for i in a:
    print(i)

connection.close()