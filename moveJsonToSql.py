import json
from pprint import pprint
import connectToSql
with open('lease.json') as data_file:
    data = json.load(data_file)

#pprint(data[0])

cur = connectToSql.con.cursor()
cur.execute("insert into dbo.mydummytable(myid,myname,myage,mycity) values (?,?,?,?)",'8','Jayant','32','Pune')
connectToSql.con.commit()

cur.execute("select myid,myname,myage,mycity from dbo.mydummytable")
for row in cur:
    print(row.myid , "," , row.myname)

cur.close()
connectToSql.con.close()

# Maybe we could check the file size
# if filesize is >2048 then we do the buffersize else line by line