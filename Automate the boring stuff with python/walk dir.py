import os

for folder, subfolder, filename in os.walk('E:\\  ASHISH\\StudioCode'):
    print('Current Folder is: '+ folder)
    print('List of Subfolder in ' + folder + ' folder is: ' + str(subfolder))
    print('List of Filename in ' + folder + ' folder is: ' + str(filename))
    print()