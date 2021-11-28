import exifread
import files
from datetime import datetime

def get_exif(filename):
	try:
		with open(filename, 'rb') as f:
			return exifread.process_file(f)
	except:
		return None

def get_date(file):
	tags=get_exif(file)
	try:
		return datetime.strptime(str(tags['EXIF DateTimeOriginal'].values), '%Y:%m:%d %H:%M:%S')
	except:
		return datetime.fromtimestamp(files.creation_time(file))
