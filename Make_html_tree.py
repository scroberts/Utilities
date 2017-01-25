#!/usr/bin/env python3

# external modules

# my modules
import Tree
import DCC
import time

tic = time.time()


# Login to DCC
s = DCC.login(Site = 'Production')



# This utility creates an html report of the content below the specified collection

# Prerequisites:
	# Specified collection number to create a html report on



# Expected output: 
	# As the program runs a list of all Documents and Collections located in specified collection
	# will be displayed on the screen, once complete the user will automatically be logged-out
	# In the specified report file path (Config.py) a html file created from this script will be saved.


# froot = 'B. Enclosure Pre-Preliminary Design and Requirements Phase'
# coll = 'Collection-2219'

# froot = 'C. Enclosure Preliminary Design Phase'
# coll = 'Collection-2219'

coll = 'Collection-13735'

# coll = 'Collection-10259'
froot = coll

tr = Tree.return_tree(s, coll, froot)
Tree.html_tree(s,tr,froot)

toc = time.time()
delta_t = toc - tic
print('Elapsed time is: ', delta_t)