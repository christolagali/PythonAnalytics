import connectToSql
import pygal
import lxml
from array import *

# Establish connection with SQL Server
Connectvar = connectToSql.ConnectToSql
Connectvar.connect(Connectvar)
#Connectvar.testConnection(Connectvar)

resultSet = Connectvar.getTotalSalesData(Connectvar)
resultSet1 = Connectvar.getTotalCustData(Connectvar)
resultSet2 = Connectvar.getTotalNewCustData(Connectvar)
#close the connection
Connectvar.con.close()

# process records in resultset2
#print(resultSet2)

#Connectvar.displayLineChart(Connectvar, l1, l2, l3)
#Connectvar.displayRawNumbers(Connectvar, l[0], l[1], l[2])
#Connectvar.displayLineChart(Connectvar, l1, l2, l3)
txt = 'Month-to-Month Totals of sales for each dealership :'
Connectvar.displayRawNumbers(Connectvar, resultSet, txt)

txt = 'Month-to-Month Totals of Customers for each dealership :'
Connectvar.displayRawNumbers(Connectvar, resultSet1, txt)

txt = 'Month-to-Month Totals of New Customers for each dealership :'
Connectvar.displayRawNumbers(Connectvar, resultSet2, txt)



