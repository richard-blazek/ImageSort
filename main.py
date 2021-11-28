import files
import renaming
import sorting
import logging
import pathlib

def sort_all(folder):
	filepaths=files.get_folder_files(folder)
	
	print('Sorting', folder)
	filepaths=sorting.sort_by_date(filepaths)
		
	print('Renaming', folder)
	renaming.rename_to_numbers(filepaths)
	print('Finished!')

def rename_all(folder):
	filepaths=files.get_folder_files(folder)

	print('Renaming', folder)
	renaming.rename_to_numbers(filepaths)
	print('Finished!')

def sort_subfolders(folder):
	for subfolder in files.get_subdirectories(folder):
		sort_all(subfolder)
	print('Everything finished!')
	
def rename_subfolders(folder):
	for subfolder in files.get_subdirectories(folder):
		rename_all(subfolder)
	print('Everything finished!')

def print_help():
	print('sort <F>    sort images in the <F> folder by date and rename them as numbers')
	print('sort+ <F>   sort images in all subfolders of the <F> folder by date and rename them as numbers')
	print('num <F>     rename images in the <F> folder as numbers preserving their order')
	print('num+ <F>    rename images in all subfolders of the <F> folder as numbers preserving their order')
	print('files <F>   list files in the <F> folder')
	print('folders <F> list subfolders of the <F> folder')
	print('quit        quit the program')

def loop():
	while True:
		entered=input('Enter a command: ').split(maxsplit=1)
		cmd, par=entered[0].lower() if len(entered)>=1 else None, entered[1] if len(entered)==2 else None
		if not cmd:
			print('Command missing')
			print_help()
		elif cmd=='quit':
			break
		elif not par:
			print('Parameter missing')
			print_help()
		elif not pathlib.Path(par).exists():
			print('Folder "' + par + '" does not exist')
			print_help()
		elif cmd=='sort':
			sort_all(pathlib.Path(par))
		elif cmd=='sort+':
			sort_subfolders(pathlib.Path(par))
		elif cmd=='num':
			rename_all(pathlib.Path(par))
		elif cmd=='num+':
			rename_all(pathlib.Path(par))
		elif cmd=='folders':
			subdirs=files.get_subdirectories(pathlib.Path(par))
			print('   '.join(sd.name for sd in subdirs))
		elif cmd=='files':
			filepaths=files.get_folder_files(pathlib.Path(par))
			print('   '.join(f.name for f in filepaths))
		else:
			print('Invalid command.')
			print_help()

logging.getLogger('exifread').setLevel(logging.CRITICAL)

print_help()
try:
	loop()
except Exception as e:
	print(e)
	input()
