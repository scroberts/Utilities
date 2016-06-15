#!/usr/bin/env python3
import DISC

# Prototype for writing discussion group spreadsheets.
# Make a new copy of this file for each discussion board


# url is the html address of the Bulletein Board
# htmlfile is the name of the file you are going to save to extract data from
# xlsfile is the name of the spreadsheet that will be created



# Prerequisite:
# 	Have the URL existing discussion board in which you would like to make a excel and html file of


# Expected Output:
# 	As the program runs, all postings within the discussion board will be displayed, while
# 	simultaneously  a html file file will be created and stored in the dccfilepath
#	directory. The excel file will be stored in the current working directory.


url = 'https://docushare.tmt.org/docushare/dsweb/View/BulletinBoard-354?init=true'
htmlfile = 'CRYO CoDR Review Comments Action Items 20151118.html'
xlsfile = 'CRYO CoDR Review Comments Action Items 20151118.xlsx'

# Call get_discussion

DISC.get_discussion(url, htmlfile, xlsfile)
