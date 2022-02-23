from pymol import cmd
import sys
import math
import subprocess
import os

asd=open('overview.csv','r')
KLIFS_CSV=asd.readlines()
asd.close()


LIGDICT={}
LIGDICT_A={}
#LIGDICT_O={}

for f in KLIFS_CSV[1:]:
	if f.split(',')[3].strip():	#alt
		LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]]=[]
	else:
		LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]]=[]
	if f.split(',')[3].strip():	#alt
		LIGDICT_A[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]]=[]
#		LIGDICT_O[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]]=[]
	else:
		LIGDICT_A[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]]=[]
#		LIGDICT_O[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]]=[]

for f in KLIFS_CSV[1:]:
	if f.split(',')[5] != '-':
		if f.split(',')[3].strip():	#alt
			if f.split(',')[5][0].isalpha():
				LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append(f.split(',')[5])
			else:
				LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append('Q'+f.split(',')[5][0:2])
#				print('Q'+f.split(',')[5][0:2])
		else:
			if f.split(',')[5][0].isalpha():
				LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append(f.split(',')[5])
			else:
				LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append('Q'+f.split(',')[5][0:2])
#				print('Q'+f.split(',')[5][0:2])
	if f.split(',')[6] != '-':
		if f.split(',')[3].strip():	#alt
			if f.split(',')[6][0].isalpha():
				LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append(f.split(',')[6])
				LIGDICT_A[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]]=f.split(',')[6]
			else:
				LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append('Q'+f.split(',')[6][0:2])
				LIGDICT_A[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]]='Q'+f.split(',')[6][0:2]
#				print('Q'+f.split(',')[6][0:2])
		else:
			if f.split(',')[6][0].isalpha():
				LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append(f.split(',')[6])
				LIGDICT_A[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]]=f.split(',')[6]
			else:
				LIGDICT[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append('Q'+f.split(',')[6][0:2])
				LIGDICT_A[f.split(',')[0].upper()+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]]='Q'+f.split(',')[6][0:2]
#				print('Q'+f.split(',')[6][0:2])



'''
for f in KLIFS_CSV[1:]:
	if f.split(',')[5] != '-' and f.split(',')[6] != '-':
		if f.split(',')[5] == '-':
			if f.split(',')[3].strip():	#alt
				LIGDICT_O[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append('-')
			else:
				LIGDICT_O[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append('-')
		else:
			if f.split(',')[3].strip():	#alt
				LIGDICT_O[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append(f.split(',')[5])
			else:
				LIGDICT_O[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append(f.split(',')[5])
		if f.split(',')[6] == '-':
			if f.split(',')[3].strip():	#alt
				LIGDICT_A[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append('-')
			else:
				LIGDICT_A[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append('-')
		else:
			if f.split(',')[3].strip():	#alt
				LIGDICT_A[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append(f.split(',')[6])
			else:
				LIGDICT_A[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append(f.split(',')[6])
'''
for f in list(LIGDICT):
	if len(LIGDICT[f]) == 0:
		del LIGDICT[f]

for f in list(LIGDICT_A):
	if len(LIGDICT_A[f]) == 0:
		del LIGDICT_A[f]
#FROM PDB
zxc=open('KLIFS_PDB_list.txt','r')
KLIFS=zxc.readlines()
zxc.close()

DICT=[]
for f in KLIFS:
	DICT.append(f.strip('\n'))

KLIFS_POCK=open(sys.argv[1].split('.')[0]+'_KLIFSPOCKET.txt','w')
KLIFS_POCK.write('PDB\tLIGID\tRMSD\tD0\tD1\tD2\tD3\tD4\tD5Type\n')

for kin in DICT[1:]:
	if LIGDICT.get(kin,0) != 0:
		print(kin)
	#	if os.path.isfile('KLIFS_PDB/'+kin+'.pdb'):
	#		for z in DICT[kin]:
		cmd.load(sys.argv[1])	#INPUT
		cmd.load('KLIFS_PDB/'+kin+'.pdb')	#KLIFS
		rms=cmd.align(cmd.get_names()[1],cmd.get_names()[0],cutoff=2, cycles=5,object='SAM',transform=1)
		cmd.save('asd1.pdb',cmd.get_names()[0],format='pdb')
		cmd.save('asd2.pdb',cmd.get_names()[1],format='pdb')
		asd=open('asd1.pdb','r')
		FILE1=asd.readlines()
		asd.close()
		POCK=[]
		for f in FILE1:
			if f[0:6].strip() == 'HETATM':
				POCK.append(f.strip('\n'))
		asd=open('asd2.pdb','r')
		FILE2=asd.readlines()
		asd.close()
		LIGID=[]
		for f in FILE2:
			if f[0:6].strip() == 'HETATM':
				if f[17:20].strip() != 'HOH' and f[17:20].strip() != 'CL' and f[17:20].strip() != 'MG' and f[17:20].strip() != 'SO4' and f[17:20].strip() != 'CA' and f[17:20].strip() != 'ZN' and f[17:20].strip() != 'EDO' and f[17:20].strip() != 'GOL':
					if  f[17:20].strip() in LIGDICT[kin]:
						LIGID.append(f[17:20].strip())
		LIGLIST=set(sorted(LIGID))
		if len(LIGLIST) != 0:
			for lig in LIGLIST:
				PID={0:[],1:[],2:[],3:[],4:[],5:[]}
				for f in FILE2:
			#		if f[0:6].strip() == 'HETATM':
			#			print(kin,f[17:20].strip(),lig)
					if f[0:6].strip() == 'HETATM' and f[17:20].strip() == lig:
						for x in POCK:
							DIST=math.sqrt((float(f[30:38])-float(x[30:38]))**2+ (float(f[38:46])-float(x[38:46]))**2+(float(f[46:54])-float(x[46:54]))**2)
		#					print(f[30:38],x[30:38],f[38:46],x[38:46],f[46:54],x[46:54],DIST)
							if DIST <= 5:
								PID[int(DIST)].append(x[22:26].strip())
				OUTPUT=kin+'\t'+lig+'\t'+str(rms[0])
				for f in PID.keys():
					COUNT=set(sorted(PID[f]))
					if COUNT:
						OUTPUT+='\t'+','.join(set(sorted(PID[f])))
					else:
						OUTPUT+='\t'+'0'
	#			print(kin,LIGDICT.get(kin,0),lig)
				templig=LIGDICT_A.get(kin,0)
				if templig == 0:
					OUTPUT+='\tO'
				else:
					if templig == lig:
						OUTPUT+='\tA'
					else:
						OUTPUT+='\tO'
				KLIFS_POCK.write(OUTPUT+'\n')
		cmd.delete('all')
		subprocess.call(['rm','asd1.pdb'])
		subprocess.call(['rm','asd2.pdb'])
		#	print(cmd.get_names())
		#	print(cmd.get_names())

KLIFS_POCK.close()



















'''
Back with overview.csv as input

DICT={}
for f in KLIFS_CSV[0:]:
	if f.split(',')[3].strip():	#alt
		DICT[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]]=[]
	else:
		DICT[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]]=[]

for f in KLIFS_CSV[0:]:
	if f.split(',')[5] != '-':
		if f.split(',')[3].strip():	#alt
			DICT[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append(f.split(',')[5])
		else:
			DICT[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append(f.split(',')[5])
	if f.split(',')[6] != '-':
		if f.split(',')[3].strip():	#alt
			DICT[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_alt'+f.split(',')[3]+'_chain'+f.split(',')[4]].append(f.split(',')[6])
		else:
			DICT[f.split(',')[0]+'_'+f.split(',')[1]+'_'+f.split(',')[2]+'_chain'+f.split(',')[4]].append(f.split(',')[6])

for f in list(DICT):
	if len(DICT[f]) == 0:
		del DICT[f]

KLIFS_POCK=open(sys.argv[1].split('.')[0]+'_KLIFSPOCKET.txt','w')
KLIFS_POCK.write('PDB\tLIGID\tRMSD\tD0\tD1\tD2\tD3\tD4\tD5\n')

for kin in list(DICT)[0:50]:
	if os.path.isfile('KLIFS_PDB/'+kin+'.pdb'):
		for z in DICT[kin]:
			LIGNAME=z
			cmd.load(sys.argv[1])	#INPUT
			cmd.load('KLIFS_PDB/'+kin+'.pdb')	#KLIFS
			rms=cmd.align(cmd.get_names()[1],cmd.get_names()[0],cutoff=2, cycles=5,object='SAM',transform=1)
			cmd.save('asd1.pdb',cmd.get_names()[0],format='pdb')
			cmd.save('asd2.pdb',cmd.get_names()[1],format='pdb')
			asd=open('asd1.pdb','r')
			FILE1=asd.readlines()
			asd.close()
			POCK=[]
			for f in FILE1:
				if f[0:6].strip() == 'HETATM':
					POCK.append(f.strip('\n'))
			asd=open('asd2.pdb','r')
			FILE2=asd.readlines()
			asd.close()
			PID={0:[],1:[],2:[],3:[],4:[],5:[]}
			for f in FILE2:
#				if f[0:6].strip() == 'HETATM':
#					print(kin,f[17:20].strip(),LIGNAME)
				if f[0:6].strip() == 'HETATM' and f[17:20].strip() == LIGNAME:
					for x in POCK:
						DIST=math.sqrt((float(f[30:38])-float(x[30:38]))**2+ (float(f[38:46])-float(x[38:46]))**2+(float(f[46:54])-float(x[46:54]))**2)
			#			print(f[30:38],x[30:38],f[38:46],x[38:46],f[46:54],x[46:54],DIST)
						if DIST <= 5:
							PID[int(DIST)].append(x[22:26].strip())
			OUTPUT=kin+'\t'+z+'\t'+str(rms[0])
			for f in PID.keys():
				COUNT=set(sorted(PID[f]))
				if COUNT:
					OUTPUT+='\t'+','.join(set(sorted(PID[f])))
				else:
					OUTPUT+='\t'+'0'
			KLIFS_POCK.write(OUTPUT+'\n')
			subprocess.call(['rm','asd1.pdb'])
			subprocess.call(['rm','asd2.pdb'])
#			print(cmd.get_names())
			cmd.delete('all')
#			print(cmd.get_names())
	else:
		print(kin)

KLIFS_POCK.close()

'''

