import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                        port=3306,
                                         database='mydatabase',
                                         user='root',
                                         password='admin123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        #cursor.execute("CREATE DATABASE mydatabase")
        # cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

        # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        # val = ("John", "Highway 21")    
        # cursor.execute(sql, val)
        # connection.commit()
        # print(cursor.rowcount, "record inserted.")

        cursor.execute("SELECT * FROM customers")

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)


        # for x in cursor:
        #     print(x)



        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")