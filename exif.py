import exifread, files, datetime

def get_exif(path):
    try:
        with open(str(path), 'rb') as f:
            return exifread.process_file(f)
    except:
        return None

def get_from_exif(exif, *indices):
    for index in indices:
        try:
            return datetime.datetime.strptime(str(exif[index].values), '%Y:%m:%d %H:%M:%S')
        except:
            pass
    return None

def get_datetime(path):
    exif = get_exif(path)
    time = get_from_exif(exif, 'EXIF DateTimeOriginal', 'EXIF MediaCreateDate', 'EXIF CreateDate')
    return time or datetime.datetime.fromtimestamp(files.creation_time(path))

def get_timestamp(path):
    return int(get_datetime(path).timestamp())

def with_timestamps(paths):
    return [(path, get_timestamp(path)) for path in paths]
