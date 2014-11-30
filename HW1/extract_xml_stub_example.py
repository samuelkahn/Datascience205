#! /usr/local/bin/python
#### SAMUEL KAHN --- ASSIGNMENT 1
import os
from xml.etree import ElementTree


# Load and parse an XML file
def parseXmlFile(fname):
    try:
        tree = ElementTree.parse(fname)		
    except Exception as inst:
	print ("error opening file: %s", inst)
	return
    return tree


def main():
	# open up the output files
    ftitle = open("pages.txt", 'w')
    fuser = open("users.txt", 'w')
    ftile_user = open("page_users.txt", 'w')
	# read and parse the xml data into an element tree
    tree = parseXmlFile("./enwiki-latest-stub-articles1.xml")
    if tree is not None:
	root = tree.getroot()
	print "Root of the XML is %s"% root.tag
		#to get the list of titles in all the docs
	count = 0
     
	for child in root.iter('page'):
         ### Title for each page, use text() function to get the actual text
         title= child.find('title').text
         ### Scan the first 7 or 11 characters in sting to see if there is a match
         if 'America' == title[0:7] or 'Afghanistan' in title[0:11]:
             ### Increment counter
             count+=1
             ### page_id
             page_id=child.find('id').text
             ### write to ftitle file
             ftitle.write(page_id+', '+title+'\n')
             ### get element objects for usernme and d
             username=child.find('revision').find('contributor').find('username')
             username_id=child.find('revision').find('contributor').find('id')
             ### If element username objects are not None, then contributers exist
             if username is not None and username_id is not None:
                 ### username_id and username written to file
                 fuser.write(username_id.text+', '+username.text+'\n')
                 ### page_id and username id written to file
                 ftile_user.write(page_id+', '+username_id.text+'\n')
             
    ### Print the number of reevenant pages
    print 'There are '+str(count)+' pages which start with either "Afghanistan" or "America"'
#
    ftitle.close()	
    fuser.close()	
    ftile_user.close()	

if __name__ == '__main__':
	main()
	




