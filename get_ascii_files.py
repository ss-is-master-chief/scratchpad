import glob
import linecache
import pandas as pd
import os.path

def get_grid_files():

    files_grid = []
    for file in glob.glob("*.asc"):
        files_grid.append(file)
    return files_grid

'''Converting asc files into CSV'''

def install_grid(file_name):

    file_name = file_name.strip('.asc')
    print(file_name)

    file_type = 'asc'
    convert_to = 'csv'

    '''Will overwrite/update file if it already exists'''

    if(os.path.exists('{}.{}'.format(file_name,convert_to))):
        print("Overwriting previous changes...")
        open('{}.{}'.format(file_name,convert_to), 'w').close()

    file = open("{}.{}".format(file_name,convert_to),'a')

    '''Fetching meta-data for file'''

    n_col = linecache.getline('{}.{}'.format(file_name,file_type),1).split(' ')
    n_col = n_col[1]

    n_row = linecache.getline('{}.{}'.format(file_name,file_type),2).split(' ')
    n_row = int(n_row[1])
    print(n_row)

    xllcenter = linecache.getline('{}.{}'.format(file_name,file_type),3).split(' ')
    xllcenter = xllcenter[1]

    yllcenter = linecache.getline('{}.{}'.format(file_name,file_type),4).split(' ')
    yllcenter = yllcenter[1]

    cellsize = linecache.getline('{}.{}'.format(file_name,file_type),5).split(' ')
    cellsize = cellsize[1]

    NODATA_value = linecache.getline('{}.{}'.format(file_name,file_type),6).split(' ')
    NODATA_value = NODATA_value[1]

    results = []

    for i in range(7,n_row+7):

        each_line = linecache.getline('{}.{}'.format(file_name,file_type),i).split(' ')
        print("Entering row",(i-6))
        results.append(list(map(int, each_line)))

    print("Creating CSV..")

    data_frame = pd.DataFrame(results)
    data_frame.to_csv(file, header=False, index=False)

    print("Done")

    file.close()

'''Interative for installing for all .asc files'''

def process_grid():

    files = get_grid_files()
    print(files)
    for file in files:
        install_grid(file)

if __name__=='__main__':
    
    process_grid()
