import mysql.connector as db_connector

try:
    mydb = db_connector.connect(
      host = "185.201.11.128",
      user = "u927028353_eOjaQ",
      password = "BlaBla123",
      database = "u927028353_DCbrh"
    )

    mycursor = mydb.cursor()
    print(type(mycursor))

    sql_raw = "INSERT INTO drivers (car_number, driver_name) VALUES (18, 'L. Stroll')"
    sql = "INSERT INTO drivers (car_number, driver_name) VALUES (%s, %s)" #prepared statement
    values = ("26", "D. Kvyat")
    #mycursor.execute(sql_raw)
    #mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM drivers")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(type(x))

    mycursor.close()

except db_connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

finally:
    if (mydb.is_connected()):
        mydb.close()
        print("MySQL connection is closed")
