import pyodbc

#print("I reached here")
#con = pyodbc.connect("DRIVER={SQL Server};server=//CHRISTO-ADMIN\SQLEXPRESS;port=1433;database=sftodbexample;uid=chris;pwd=PraiseLord77")

theserver = "//CHRISTO-ADMIN\SQLEXPRESS:1433"
thedatabase = "sftodbexample"
theuser = "chris"
thepassword="PraiseLord77"

#con = pyodbc.connect(driver='{SQL Server Native Client 11.0}',host=theserver,database=thedatabase,trusted_connection='yes',user=theuser,password=thepassword)
con=pyodbc.connect('DRIVER={SQL Server};SERVER=CHRISTO-ADMIN\SQLEXPRESS;PORT=1433;DATABASE=sftodbexample;UID=chris;PWD=PraiseLord77')
