import files

def digit_count(num):
	return len(str(num))

def get_zero_padding_format_string(zeros):
	return '{:0'+str(zeros)+'d}'

def zero_padding(zeros, num):
	return get_zero_padding_format_string(zeros).format(num)

def file_number_name(size, number, suffix):
	return zero_padding(size, number)+suffix

def rename_to_numbers(filepaths):
	if not filepaths:
		return
	folder=filepaths[0].parent
	name_size=digit_count(len(filepaths))
	
	new_filepaths=[folder/file_number_name(name_size, i+1, filepaths[i].suffix) for i in range(len(filepaths))]
	files.rename(filepaths, new_filepaths, files.get_nonexisting_file_in(folder))
