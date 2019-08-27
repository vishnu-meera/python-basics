import shutil
#shutil.copy()
#shutil.copytree()
#shuil.move()
#renaming is done by moving the file to same directory with other name

import os

#os.unlink('file.txt')
#os.rmddir('folder')

#shutil.removetree('folder name')

#before deleting do a TRY RUN

# send2trash.send2trash will delete file to recyle bin

for folderName,subfolders, files in os.walk('..\All'):
	print('The folder is ' + folderName)
	print('The subfolder in ' + folderName +' are : ' + str(subfolders))
	print('The files in ' + folderName +' are : ' + str(files))
	print('\n')