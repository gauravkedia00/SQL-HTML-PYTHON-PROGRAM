import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SERVER-NAME;'
                      'Database=DATABASE-NAME;'
                      'Trusted_Connection=yes;')
 
cursor = conn.cursor()
cursor.execute('SELECT * FROM DATABASE-NAME.dbo.TABLE-NAME')
 


strTable = "<html><head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css'><script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js'></script></head><table class='table'><tr><th>Name</th><th>URL</th><th>ATTRIBUTES</th><th>TAGS</th></tr>"
 
for row in cursor:
 symb = row[1]
 strRW = "<tr><td class='danger'>"+str(row[0])+ "</td><td class='success'>"+str(row[1])+"</td><td class='info'>"+str(row[2])+"</td><td class='active'>"+str(row[3])+"</td></tr>"
 strTable = strTable+strRW
 
strTable = strTable+"</table></html>"
 
hs = open("asciiCharHTMLTable_11.html", 'w')
hs.write(strTable)