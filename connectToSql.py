import pyodbc
import pygal
import lxml

class ConnectToSql():

    theserver = "//CHRISTO-ADMIN\SQLEXPRESS:1433"
    thedatabase = "sftodbexample"
    theuser = "chris"
    thepassword="PraiseLord77"

    def connect(self):
        self.con=pyodbc.connect('DRIVER={SQL Server};SERVER=CHRISTO-ADMIN\SQLEXPRESS;PORT=1433;DATABASE=sftodbexample;UID=chris;PWD=PraiseLord77')


    def insertValues(self,data):
        cur = self.con.cursor()
        for item in data:
            if item['soldVehicleVin'] == 'none':
                item['soldVehicleVin'] = 'null'
            cur.execute("insert into dbo.Vehicle_Sales_Table(Manufacturer,[Current Vehicle Vin],[Customer Number],[Dealer Id],[Has Sale],[Month]) values (?,?,?,?,?,?)",item['Manufacturer'],item['currentVehicleVin'],item['customerNumber'],item['dealerId'],item['hasSale'],item['month'])
            self.con.commit()
        print('Value inserted!')
        cur.close()

    def testConnection(self):
        cur = self.con.cursor()
        cur.execute("select * from [sftodbexample].[dbo].[mydummytable]")
        rows = cur.fetchall()
        for row in rows:
            print(row.myname, row.mycity)
        cur.close()


    def getTotalSalesData(self):
        cur = self.con.cursor()
        cur.execute("SELECT [Dealer Id],COUNT([Has Sale]) As Sales_Total,[Month] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table] where [Dealer Id] in (SELECT [Dealer Id] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table])  and [Has Sale]=1  Group by [Month],[Dealer Id]  Order by [Dealer Id],[Month]")
        rows =cur.fetchall()
        cur.close()
        return rows

    def displayLineChart(self,distid,totals,dates):
        l1 = []
        l2 = []
        l3 = []
        for r in distid:
            if r == 0:
                l1.append(r)
                l2.append(totals)
                l3.append(dates)
            line_chart = pygal.Line()
            line_chart.title = 'Dist ID 0'
            line_chart.x_labels = map(str, dates)
            line_chart.add('0', totals)
            line_chart.render_to_file('charts/chart.svg')

    def getTotalCustData(self):
        cur = self.con.cursor()
        cur.execute("SELECT [Dealer Id],COUNT([Customer Number]) As Cust_Total,[Month] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table] where [Dealer Id] in (SELECT [Dealer Id] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table]) Group by [Month],[Dealer Id]  Order by [Dealer Id],[Month]")
        rows = cur.fetchall()
        cur.close()
        return rows

    def getNextItem(self,rows,r):
        if rows.index(r) != len(rows) - 1:
            next_item = rows[rows.index(r) + 1]
            return next_item[0]

    def getTotalNewCustData(self):
        cur = self.con.cursor()
        cur.execute("SELECT DISTINCT [Dealer Id],COUNT([Customer Number]),[Month] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table] where [Dealer Id] in (SELECT [Dealer Id] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table]) Group by [Dealer Id],[Customer Number],[Month] Order by [Dealer Id]")
        rows = cur.fetchall()
        cur.close()
        return rows

    def displayRawNumbers(self,resulset,txt):
        print(txt)
        print('Dealer ID' , '|' , 'Month' , '|' , 'Totals')
        for r in resulset:
            if r[0] == 0:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 1:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 2:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 3:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 4:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 5:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 6:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 7:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 8:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 9:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 10:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 11:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 12:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 13:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 14:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 15:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 16:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 17:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 18:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 19:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 20:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 21:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 22:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 23:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 24:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 25:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 26:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 27:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 28:
                print(r[0] ,' | ', r[2], '|' ,r[1])
            if r[0] == 29:
                print(r[0] ,' | ', r[2], '|' ,r[1])