import shutil, os, stat

def has_hidden_attribute(file):
	return bool(os.stat(str(file)).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def is_hidden(file):
	return file.name.startswith('.') or has_hidden_attribute(file)

def is_relevant(path):
    return not path.is_dir() and not is_hidden(path)

def move(old, new):
	shutil.move(str(old), str(new))

def swap(old, new, tmp):
	if new == old:
		pass
	elif new.exists():
		move(new, tmp)
		move(old, new)
		move(tmp, old)
	else:
		move(old, new)

def get_nonexisting_file_in(folder):
	name = 'y'
	while (folder / name).exists():
		name += 'y'
	return folder / name

def rename(old_paths, new_paths):
	if not old_paths:
		return
	tmp_path = get_nonexisting_file_in(old_paths[0].parent)
	for old, new in zip(old_paths, new_paths):
		swap(old, new, tmp_path)


def get_folder_files(folder):
	return [path for path in folder.iterdir() if is_relevant(path)]

def get_subdirectories(folder):
	return [path for path in folder.iterdir() if path.is_dir() and path not in [folder, folder.parent]]

def creation_time(file):
	return os.path.getctime(file)
