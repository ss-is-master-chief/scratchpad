import sys
import glob

'''Add proper path variables as follows'''
sys.path.insert(0,'/Library/Frameworks/GDAL.framework/Versions/2.2/Python/3.6/site-packages')

try:
	from osgeo import gdal
	print("Gdal Version: ",gdal.__version__,"\n")
except:
	sys.exit("Cannot find osgeo")

class Gather:

	files = []
	formats = ('*.tif','*.jp2','*.h5','*.png','*.jpg')

	def __init__(self):
		self.get_files()
		for file_name in self.files:
			self.get_metadata(file_name)

	def get_files(self):
		for types in self.formats:
			self.files.extend(glob.glob(types))
		for content in self.files:
			print(content)

	def get_metadata(self,file_name):
		file = gdal.Open(file_name)
		metadata = file.GetMetadata()
		print("#-",file_name,"-#\n")
		for key, item in metadata.items():
			print(key,"|",item)
		print("\nRaster Count:",file.RasterCount)
		print("Raster X Size:",file.RasterXSize)
		print("Raster Y Size:",file.RasterYSize)
		print("\n")

if __name__=="__main__":
	obj = Gather()
	

