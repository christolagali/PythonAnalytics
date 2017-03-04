import connectToSql
import pygal
import lxml
from array import *

# Establish connection with SQL Server
Connectvar = connectToSql.ConnectToSql
Connectvar.connect(Connectvar)

# This method is used to Test a connection to SQL Server
#Connectvar.testConnection(Connectvar)

# We design 3 resultsets by executing SQL Queries to Derive the following:
# resultset: Query for Month-to-Month Totals of sales for each dealership
# resultset1: Query for Month-to-Month Customers that are present for each dealership
# resultset2: Query for Month-to-Month totals of new customers added per month

resultSet = Connectvar.getData(Connectvar,'totalSalesdata')
resultSet1 = Connectvar.getData(Connectvar,'totalCustdata')
resultSet2 = Connectvar.getData(Connectvar,'totalNewCust')

#close the connection
Connectvar.con.close()

# The Resultsets are then passed to the method for printing raw nos and Generating .png charts
# These charts are present in charts folder
txt = 'Month-to-Month Totals of sales for each dealership :'
Connectvar.displayRawNumbers(Connectvar, resultSet, txt,'q1')

txt = 'Month-to-Month Totals of Customers for each dealership :'
Connectvar.displayRawNumbers(Connectvar, resultSet1, txt,'q2')

txt = 'Month-to-Month Totals of New Customers for each dealership :'
Connectvar.displayRawNumbers(Connectvar, resultSet2, txt,'q3')

txt = 'Month-to-Month Forecast Data :'
Connectvar.displayForecastNumbers(Connectvar,resultSet,txt,'q1')


