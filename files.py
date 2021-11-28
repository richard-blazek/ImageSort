import shutil
import os
import pathlib
import stat

def has_hidden_attribute(file):
	return bool(os.stat(str(file)).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def is_hidden(file):
	return file.name.startswith('.') or has_hidden_attribute(file)

def move(old, new):
	shutil.move(str(old), str(new))

def rename(old_paths, new_paths, tmp_path):
	for old, new in zip(old_paths, new_paths):
		if new==old:
			pass
		elif new.exists():
			move(new, tmp_path)
			move(old, new)
			move(tmp_path, old)
		else:
			move(old, new)

def get_nonexisting_file_in(folder):
	name = '+'
	while (folder/name).exists():
		name = name + '+'
	return folder/name

def get_folder_files(folder):
	return [path for path in folder.iterdir() if not path.is_dir() and not is_hidden(path)]

def get_subdirectories(folder):
	return [path for path in folder.iterdir() if path.is_dir() and path!=folder and path!=folder.parent]

def creation_time(file):
	return os.path.getctime(file)
