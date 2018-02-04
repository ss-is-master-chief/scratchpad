import sqlite3

# 
# connecting to example database
#
database = "truemarble.sqlite"
conn = sqlite3.connect(database)
curs = conn.cursor()

#
# get table names from example database
#
curs.execute("SELECT tbl_name FROM sqlite_master WHERE type='table';")
tables = curs.fetchall()

#
# CSV file generation 
#
for i in tables:
    print('Creating CSV for: ',i[0])
    curs.execute("SELECT * FROM %s;" % i[0])
    ex = curs.fetchall()

    for row in ex :
        list = []
        for sub_value in row:
            value = str(sub_value)
            list.append(value)
        file = open('./database/%s.csv'% i[0], 'a') #opens respective CSV file in append mode
        ex = csv.writer(file)
        ex.writerow(list)
