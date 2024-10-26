import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sathish",
  database="st"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT empname,salary FROM emp")

myresult = mycursor.fetchall()
  
x= np.array([row[0] for row in myresult])
y= np.array([row[1] for row in myresult])
plt.bar(x,y) 
plt.show()
