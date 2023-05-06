import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost',
        user='admin',
        password='admin123',
        # database='db',
        port='5432'
        )

    # db_Info = connection.info()
    # print("Connected to PostGres Server version ", db_Info)
    cursor = connection.cursor()
        #cursor.execute("CREATE DATABASE mydatabase")
        # cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

        # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        # val = ("John", "Highway 21")    
        # cursor.execute(sql, val)
        # connection.commit()
        # print(cursor.rowcount, "record inserted.")

        # cursor.execute("SELECT * FROM customers")

        # myresult = cursor.fetchall()

        # for x in myresult:
        #     print(x)


        # for x in cursor:
        #     print(x)



        # cursor.execute("select database();")
        # record = cursor.fetchone()
        # print("You're connected to database: ", record)

except :
    print("Error while connecting to MySQL")
finally:
    # cursor.close()
    # connection.close()
    print("MySQL connection is closed")