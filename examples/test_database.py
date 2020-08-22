import mysql.connector as db_connector

perform_select = False
perform_insert = True
operations = ""

try:
    mydb = db_connector.connect(
      host = "185.201.11.128",
      user = "u927028353_eOjaQ",
      password = "BlaBla123",
      database = "u927028353_DCbrh"
    )

    mycursor = mydb.cursor()

    if perform_insert:
        print("Ejecutando un INSERT")
        operations = "INSERT "
        sql_raw = "INSERT INTO drivers (car_number, driver_name) VALUES (18, 'L. Stroll')"
        #sql = "INSERT INTO drivers (car_number, driver_name) VALUES (%s, %s)" #prepared statement
        #values = ("26", "D. Kvyat")
        mycursor.execute(sql_raw)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    if perform_select:
        print("Ejecutando un SELECT")
        operations += "SELECT "
        mycursor.execute("SELECT * FROM driverss")
        myresult = mycursor.fetchall() #Obtener el resulSet de la consulta

        for x in myresult:
          print(type(x))

    mycursor.close()

except db_connector.Error as error:
    print("Error al ejecutar la(s) operación(es) {} sobre la base de datos:\n {}".format(operations,error))
    
finally:
    if (mydb.is_connected()):
        mydb.close()
        print("La conexión ha sido cerrada exitosamente")
