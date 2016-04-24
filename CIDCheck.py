#!/usr/bin/env python3
import CID

# Precondition:
#   Change dirpath to reflect location that the CID will be generated
#   Change CID_coll to the collection number of which you would like to make the CID for
#   Change htmlfile to reflect the name of the html file that will be generated
#   Chenge outroot to reflect what will be appended to the beginning of the file names as they are saved
# Expected output:
#   As the code runs the collection number will be traversed to check version history
#   as well as display all information about the collections and files as they are read
#   Another output are files with the following appearances:
#       "outroot"_bothlist.txt, "outroot"_doclist.txt, "outroot"_verlist.txt,
#       "outroot"_CID.txt, "outoot"_doc_list.txt, "outroot"_ver_list.txt
#   These files will be located in dirpath that the user has set

dirpath = r'/Users/paulb/Documents/TMT/Python/Reports/'
CID_coll = 'Collection-10669'
htmlfile = 'Test for collection 10669.html'
outroot = 'STRCID_'

# This calls the function in CID.py, documentation for this code is included under the Library script CID.py
CID.make_cid(dirpath, CID_coll, htmlfile, outroot)
