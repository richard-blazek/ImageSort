import files, renaming, logging, pathlib

def sort_all(folder):
	paths = files.get_folder_files(folder)
	
	print('Sorting', folder)
	renaming.number(paths)
	print('Finished!')

def sort_subfolders(folder):
	for subfolder in files.get_subdirectories(folder):
		sort_all(subfolder)
	print('Everything finished!')
	
def print_help():
	print('sort <F>    sort images in the <F> folder by date and rename them as numbers')
	print('sub  <F>    sort images in all subfolders of the <F> folder by date and rename them as numbers')
	print('quit        quit the program')

logging.getLogger('exifread').setLevel(logging.CRITICAL)

print_help()
while True:
	try:
		entered = input('Enter a command: ').split(maxsplit = 1)
		cmd, par = entered[0].lower() if len(entered) >= 1 else None, entered[1] if len(entered) == 2 else None
		if not cmd:
			print('Command missing')
			print_help()
		elif cmd == 'quit':
			break
		elif not par:
			print('Parameter missing')
			print_help()
		elif not pathlib.Path(par).exists():
			print('Folder "' + par + '" does not exist')
			print_help()
		elif cmd == 'sort':
			sort_all(pathlib.Path(par))
		elif cmd == 'sub':
			sort_subfolders(pathlib.Path(par))
		else:
			print('Invalid command.')
			print_help()
	except Exception as e:
		print(e)
