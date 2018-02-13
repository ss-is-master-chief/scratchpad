import sqlite3, os, csv, glob


def get_tif_files():

    files = []
    for file in glob.glob("*.tif"):
        files.append(file)
    return files

def load_data(file_name):

    os.system("rasterlite_load -d {}.sqlite -T {} -D . -t".format(file_name,file_name))
    os.system("rasterlite_load -d {}.sqlite -T {} -D . -v".format(file_name,file_name))

def create_csv(tables, file_name, curs):

    for i in tables:
        print('Creating CSV for: ',i[0])
        curs.execute("SELECT * FROM {};".format(i[0]))
        ex = curs.fetchall()
        for row in ex :
            list = []
            for j in row:
                value = str(j)
                list.append(value)
            file_data = open('.{}_files/{}.csv'.format(file_name,i[0]), 'a')
            ex = csv.writer(file_data)
            ex.writerow(list)

def create_db():

    files = get_tif_files()

    for file in files:

        file_name = file.strip(".tif")
        database = ("{}.sqlite".format(file_name))
        conn = sqlite3.connect(database)
        curs = conn.cursor()

        curs.execute("SELECT InitSpatialMetadata()")
        curs.fetchall()

        load_data(file_name)

        curs.execute("SELECT tbl_name FROM sqlite_master WHERE type='table';")
        tables = curs.fetchall()

        os.system("mkdir {}_files".format(file_name))

        create_csv(tables, file_name, curs)
