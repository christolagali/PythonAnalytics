import pyodbc
import pygal
import lxml
import cairosvg
import pandas as pd
from pandas import read_csv
from pandas import Series
from matplotlib import pyplot
from pylab import *
import datetime
from datetime import datetime

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


    def getData(self,reportType):
        cur = self.con.cursor()
        if reportType == 'totalSalesdata':
            query = "SELECT [Dealer Id],COUNT([Has Sale]) As Sales_Total,[Month] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table] where [Dealer Id] in (SELECT [Dealer Id] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table])  and [Has Sale]=1  Group by [Month],[Dealer Id]  Order by [Dealer Id],[Month]"
        if reportType == 'totalCustdata':
            query = "SELECT [Dealer Id],COUNT([Customer Number]) As Cust_Total,[Month] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table] where [Dealer Id] in (SELECT [Dealer Id] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table]) Group by [Month],[Dealer Id]  Order by [Dealer Id],[Month]"
        if reportType == 'totalNewCust':
            query = "SELECT DISTINCT [Dealer Id],COUNT([Customer Number]),[Month] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table] where [Dealer Id] in (SELECT [Dealer Id] FROM [sftodbexample].[dbo].[Vehicle_Sales_Table]) Group by [Dealer Id],[Customer Number],[Month] Order by [Dealer Id]"
        cur.execute(query)
        rows =cur.fetchall()
        cur.close()
        return rows

    def displayLineChart(self,distid,totals,dates,charttxt):
        l1 = []
        l2 = []
        l3 = []
        l1.clear()
        l2.clear()
        l3.clear()
        l1.append(distid)
        l2.append(totals)
        l3.append(dates)
        line_chart = pygal.Bar()
        line_chart.title = 'Dist ID'+ str(l1[0][0])
        line_chart.x_labels = map(str, dates)
        mylabel = str(l1[0][0])
        line_chart.add(mylabel, totals)
        if charttxt == 'q1':
            file_name = 'charts/quest1Charts/chart'+str(l1[0][0])+'.png'
        if charttxt == 'q2':
            file_name = 'charts/quest2Charts/chart'+str(l1[0][0])+'.png'
        if charttxt == 'q3':
            file_name = 'charts/quest3Charts/chart' + str(l1[0][0]) + '.png'

        print(file_name)
        line_chart.render_to_png(file_name)



    def getNextItem(self,rows,r):
        if rows.index(r) != len(rows) - 1:
            next_item = rows[rows.index(r) + 1]
            return next_item[0]



    def displayRawNumbers(self,resulset,txt,charttxt):
        distid =[]
        totals =[]
        dates = []
        print(txt)
        print('Dealer ID' , '|' , 'Month' , '|' , 'Totals')
        for r in resulset:
            if r[0] == 0:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 1:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 2:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 3:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 4:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 5:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 6:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 7:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 8:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 9:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 10:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 11:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 12:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 13:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 14:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 15:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 16:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 17:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 18:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 19:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 20:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 21:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 22:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 23:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 24:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 25:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 26:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 27:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 28:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 29:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            else:
                # print charts
                next_item = self.getNextItem(self, resulset, r)
                if r[0] != next_item:
                    self.displayLineChart(self,distid,totals,dates,charttxt)
                    distid.clear()
                    totals.clear()
                    dates.clear()


    def displayForecastCharts(self,distid,totals,dates,charttxt):
        l1 = []
        l2 = []
        l3 = []
        l1.append(distid)
        l2.append(totals)
        l3.append(dates)

        for r in distid:
            if r == 0:

                series0 = Series.from_csv('charts\ForecastCharts1\Forecast0.csv', sep=',', header=0)
                print(series0.head())
                series0.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart0.png')

            if r == 1:
                series1 = Series.from_csv('charts\ForecastCharts1\Forecast1.csv', sep=',', header=0)
                print(series1.head())
                series1.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart1.png')

            if r == 2:
                series2 = Series.from_csv('charts\ForecastCharts1\Forecast2.csv', sep=',', header=0)
                print(series2.head())
                series2.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart2.png')

            if r == 3:
                series3 = Series.from_csv('charts\ForecastCharts1\Forecast3.csv', sep=',', header=0)
                print(series3.head())
                series3.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart3.png')

            if r == 4:
                series4 = Series.from_csv('charts\ForecastCharts1\Forecast4.csv', sep=',', header=0)
                print(series4.head())
                series4.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart4.png')

            if r == 5:
                series5 = Series.from_csv('charts\ForecastCharts1\Forecast5.csv', sep=',', header=0)
                print(series5.head())
                series5.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart5.png')

            if r == 6:
                series6 = Series.from_csv('charts\ForecastCharts1\Forecast6.csv', sep=',', header=0)
                print(series6.head())
                series6.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart6.png')

            if r == 7:
                series7 = Series.from_csv('charts\ForecastCharts1\Forecast7.csv', sep=',', header=0)
                print(series7.head())
                series7.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart7.png')

            if r == 8:
                series8 = Series.from_csv('charts\ForecastCharts1\Forecast8.csv', sep=',', header=0)
                print(series8.head())
                series8.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart8.png')
            if r == 9:
                series9 = Series.from_csv('charts\ForecastCharts1\Forecast9.csv', sep=',', header=0)
                print(series9.head())
                series9.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart9.png')
            if r == 10:
                series10 = Series.from_csv('charts\ForecastCharts1\Forecast10.csv', sep=',', header=0)
                print(series10.head())
                series10.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart10.png')
            if r == 11:
                series11 = Series.from_csv('charts\ForecastCharts1\Forecast11.csv', sep=',', header=0)
                print(series11.head())
                series11.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart11.png')
            if r == 12:
                series12 = Series.from_csv('charts\ForecastCharts1\Forecast12.csv', sep=',', header=0)
                print(series12.head())
                series12.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart12.png')
            if r == 13:
                series13 = Series.from_csv('charts\ForecastCharts1\Forecast13.csv', sep=',', header=0)
                print(series13.head())
                series13.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart13.png')
            if r == 14:
                series14 = Series.from_csv('charts\ForecastCharts1\Forecast14.csv', sep=',', header=0)
                print(series14.head())
                series14.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart14.png')
            if r == 15:
                series15 = Series.from_csv('charts\ForecastCharts1\Forecast15.csv', sep=',', header=0)
                print(series15.head())
                series15.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart15.png')
            if r == 16:
                series16 = Series.from_csv('charts\ForecastCharts1\Forecast16.csv', sep=',', header=0)
                print(series16.head())
                series16.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart16.png')
            if r == 17:
                series17 = Series.from_csv('charts\ForecastCharts1\Forecast17.csv', sep=',', header=0)
                print(series17.head())
                series17.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart17.png')
            if r == 18:
                series18 = Series.from_csv('charts\ForecastCharts1\Forecast18.csv', sep=',', header=0)
                print(series18.head())
                series18.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart18.png')
            if r == 19:
                series19 = series = Series.from_csv('charts\ForecastCharts1\Forecast19.csv', sep=',', header=0)
                print(series19.head())
                series19.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart19.png')
            if r == 20:
                series20 = Series.from_csv('charts\ForecastCharts1\Forecast20.csv', sep=',', header=0)
                print(series20.head())
                series20.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart20.png')
            if r == 21:
                series21 = Series.from_csv('charts\ForecastCharts1\Forecast21.csv', sep=',', header=0)
                print(series21.head())
                series21.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart21.png')
            if r == 22:
                series22 = Series.from_csv('charts\ForecastCharts1\Forecast22.csv', sep=',', header=0)
                print(series22.head())
                series22.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart22.png')
            if r == 23:
                series23 = Series.from_csv('charts\ForecastCharts1\Forecast23.csv', sep=',', header=0)
                print(series23.head())
                series23.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart23.png')
            if r == 24:
                series24 = Series.from_csv('charts\ForecastCharts1\Forecast24.csv', sep=',', header=0)
                print(series24.head())
                series24.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart24.png')
            if r == 25:
                series25 = Series.from_csv('charts\ForecastCharts1\Forecast25.csv', sep=',', header=0)
                print(series25.head())
                series25.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart25.png')
            if r == 26:
                series26 = Series.from_csv('charts\ForecastCharts1\Forecast26.csv', sep=',', header=0)
                print(series26.head())
                series26.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart26.png')
            if r == 27:
                series27 = Series.from_csv('charts\ForecastCharts1\Forecast27.csv', sep=',', header=0)
                print(series27.head())
                series27.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart27.png')
            if r == 28:
                series28 = Series.from_csv('charts\ForecastCharts1\Forecast28.csv', sep=',', header=0)
                print(series28.head())
                series28.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart28.png')
            if r == 29:
                series29 = Series.from_csv('charts\ForecastCharts1\Forecast29.csv', sep=',', header=0)
                print(series29.head())
                series29.plot()
                # pyplot.show()
                savefig('charts\ForecastCharts1\chart29.png')
        #for r in l3:
            #for r1 in r:
                #st = str(r1)
                #st = st.replace('-', '/')
                # stint = int(st)
                #sdate = pd.date = pd.to_datetime(r1, format='%Y-%m-%d')
                #stdate = str(sdate)
                #dt = datetime.strptime(stdate, '%Y-%m-%d %H:%M:%S')
        #         l4.append(stime)
        #
        #
        # if charttxt == 'q1':
        #     file_name = 'charts/ForecastCharts1/chart' + str(l1[0][0]) + '.png'
        # if charttxt == 'q2':
        #     file_name = 'charts/ForecastCharts2/chart' + str(l1[0][0]) + '.png'
        # if charttxt == 'q3':
        #     file_name = 'charts/ForecastCharts3/chart' + str(l1[0][0]) + '.png'
        # series = Series.from_array(l2, l4)
        # print(series.head())
        # series.plot()
        # savefig(file_name)




    def displayForecastNumbers(self,resulset,txt,charttxt):
        distid =[]
        totals =[]
        dates = []
        print(txt)
        print('Dealer ID' , '|' , 'Month' , '|' , 'Totals')
        for r in resulset:
            if r[0] == 0:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 1:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 2:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 3:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 4:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 5:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 6:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 7:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 8:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 9:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 10:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 11:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 12:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 13:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 14:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 15:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 16:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 17:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 18:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 19:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 20:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 21:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 22:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 23:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 24:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 25:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 26:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 27:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 28:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            if r[0] == 29:
                print(r[0] ,' | ', r[2], '|' ,r[1])
                distid.append(r[0])
                totals.append(r[1])
                dates.append(r[2])
            else:
                # print charts
                next_item = self.getNextItem(self, resulset, r)
                if r[0] != next_item:
                    self.displayForecastCharts(self,distid,totals,dates,charttxt)
                    distid.clear()
                    totals.clear()
                    dates.clear()
