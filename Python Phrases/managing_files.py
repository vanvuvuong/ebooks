import zipfile
import tarfile
import os

path = '..'
newpath = '.'

#################################################
# NORMAL FILES
#################################################
# return a tuple of file in the path directory
tree = os.walk(path)

# rename & remove files
os.remove(path)
os.rename(path, newpath)

# remove an empty directory
os.rmdir(path)

#################################################
# TAR FILES
#################################################
# create tar file
list_dir = os.listdir('.')
t_file = tarfile.open('t_file.tar', 'w:gz')
for f in list_dir:
	t_file.add(f)
t_file.close()

# extract tar file
t_file = tarfile.open('t_file.tar', 'r')
for f in t_file.getnames():
	t_file.extract(f, path)


#################################################
# ZIP FILES
#################################################
z_file = zipfile.ZipFile('z_file.zip', 'w')
files = os.listdir('.')
for f in files:
	z_file.write(f)
z_file.namelist()
z_file.close()
