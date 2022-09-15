import files, exif, strnum

def sorted_with_timestamps(paths):
	with_timestamps = exif.with_timestamps(paths)
	with_timestamps.sort(key = lambda pair: pair[1])
	return with_timestamps

def count_same_times(images):
	result = []
	same_max = 1
	last_i = 0
	last_same = 0
	for i, (path, timestamp) in enumerate(images):
		if timestamp == images[last_i][1]:
			last_same += 1
			same_max = max(same_max, last_same)
		else:
			last_i = i
			last_same = 1
		result.append((path, timestamp, last_same))
	return same_max, result

def number(paths):
	if not paths:
		return
	same_max, images = count_same_times(sorted_with_timestamps(paths))
	
	time_size = strnum.digits(images[-1][1])
	ending_size = strnum.digits(same_max - 1, min_length = 0)

	files.rename(paths, [path.with_stem(strnum.convert(timestamp, time_size) + strnum.convert(order, ending_size)) for path, timestamp, order in images])
