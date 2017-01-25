#!/usr/bin/env python3

# external modules

# my modules
import DCC
import Config as CF
import FileSys

# Prerequisite:
#	1. Have a collection number for which collections and documents you would like mirrored on 
#	your personal computer. If there are collections you would like to exclude ensure
#	that they are appended to the 'exclude' variable with a comma
#	2. Have a directory in which you would like to save all the documents on your PC

# Expected Output:
#	As this script runs all collections and documents (except for excluded ones)
#	will be printed to the screen. Once traversed, it will the display all
#	information about documents located in the collection chosen and determine if they already exist
#	in the directory selected. Once the process is complete
#	you will be able to locate all files in the directory selected.


# Login to DCC
s = DCC.login(CF.dcc_url + CF.dcc_login)

coll = 'Collection-13735'
dir = '/Users/sroberts/Dropbox/TMT/Current Tasks/STR FDR P3 Review/'
exclude = []

FileSys.create_DCC_mirror(s, coll, dir, SaveFiles = True, MaxFileSize = 25000000, Exclude = exclude)