import sqlite3

database = "truemarble.sqlite"
conn = sqlite3.connect(database)
curs = conn.cursor()

curs.execute("SELECT tbl_name FROM sqlite_master WHERE type='table';")
tables = curs.fetchall()

for i in tables:
    print('Creating CSV for: ',i[0])
    curs.execute("SELECT * FROM %s;" % i[0])
    ex = curs.fetchall()

    for row in ex :
        list = []
        for j in row:
            value = str(j)
            list.append(value)
        file = open('./database/%s.csv'% i[0], 'a')
        ex = csv.writer(file)
        ex.writerow(list)
