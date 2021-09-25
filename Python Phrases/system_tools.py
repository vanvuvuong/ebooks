import platform
import os

###########################################
# OS MODULE
###########################################
# print current directory
current_path = os.path.abspath(".")
parent_path = os.path.abspath("..")

# check file/folder and return a boolean value
os.path.exists('test')
os.path.isfile('test.txt')
os.path.isdir('test/')

# change current directory
os.chdir('Mastering Docker')

# environment variables - return a list
env_var = os.environ

# run a system function
os.system('mkdir')

# execute a application in the system
os.execvp('run.exe', ['--verbose'])

###########################################
# PLATFORM MODULE
###########################################

# architecture
platform.architecture()

# machine information
platform.uname()
