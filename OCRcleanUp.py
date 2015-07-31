'''Script to clean up the original OCR file
looks easiest to rewrite out to new file. Line by line means only curr line in RAM.

we want to:
	-get rid of non letter characters. 
	-replace dashes with spaces unless EOL
	-get rid of line denoting the next file
	-make all characters lowercase
'''

import re

input= open('testOCRFull.txt', 'r')
output=open('cleanTestData.txt','w')
newFileRE=re.compile("-+File:")
reunite=None

for line in input:

	if line.isspace():
		continue
	if newFileRE.match(line):
		continue
		
	line=line.lower()
	
	if reunite !=None:
		print(reunite)
		line=reunite.strip()+ line
		reunite=None
		
	if line.rstrip()[-1]=='-':
		#save the word start
		reunite=line.rpartition(" ")[-1]
		#remove it from original line
		line=line.rsplit(' ', 1)[0]
	#now replace all with space
	line=line.replace("-"," ")
	#now strip all non letter chars.
	line=re.sub("[^a-z \n]", "",line)
	#write to new file
	output.write(line)
	
input.close()
output.close()
		

