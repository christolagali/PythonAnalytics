import json
from pprint import pprint
import connectToSql


#load and read from JSON file
with open('lease.json') as data_file:
    data = json.load(data_file)


# Establish connection with SQL Server
Connectvar = connectToSql.ConnectToSql
Connectvar.connect(Connectvar)

# Insert all the values from JSON object into SQL Server: Executed only once
Connectvar.insertValues(Connectvar,data)


#close the connection
Connectvar.con.close()

# Maybe we could check the file size
# if filesize is >2048 then we do the buffersize else line by line