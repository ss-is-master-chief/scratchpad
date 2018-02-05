import sqlite3
import os
import csv

#
# data to be imported fron current working directory
#
image = "NLCD2011_LC_N39W105.tif"
database = "truemarble.sqlite"

conn = sqlite3.connect(database)
curs = conn.cursor()

#
# setting up metadata
#
curs.execute("SELECT load_extension('mod_spatialite');") # OperationalError: not authorized
curs.execute("SELECT InitSpatialMetaData(1);") # if Line 17 removed : Error - no such function 'InitSpatialMetaData()'

curs.fetchall()

#
# loading raster data from objects
#
os.system("rasterlite_load -d truemarble.sqlite -T TrueMarble -D . -t")
os.system("rasterlite_load -d truemarble.sqlite -T TrueMarble -D . -v")

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
        file = open('./%s.csv'% i[0], 'a')
        ex = csv.writer(file)
        ex.writerow(list)
