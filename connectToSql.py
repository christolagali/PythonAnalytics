import pyodbc

class ConnectToSql():
    #print("I reached here")
    #con = pyodbc.connect("DRIVER={SQL Server};server=//CHRISTO-ADMIN\SQLEXPRESS;port=1433;database=sftodbexample;uid=chris;pwd=PraiseLord77")

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
