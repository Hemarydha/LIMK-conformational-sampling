import sys
import os
asd=open(sys.argv[1],'r')
FILE1=asd.readlines()
asd.close()

for f in FILE1:
	if f.split()[0] == 'TITLE':
		NAME=f.split()[5].split('.')[0]
		break

os.rename(sys.argv[1],NAME+'.pdb')
print(NAME)
