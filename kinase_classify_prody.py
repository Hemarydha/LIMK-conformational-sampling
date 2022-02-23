from prody import *
import sys
PROTEIN=parsePDB(sys.argv[1])


ID='LIMK2'


chi1atom={ "ARG":"N-CA-CB-CG","ASN":"N-CA-CB-CG","ASP":"N-CA-CB-CG","CYS":"N-CA-CB-SG","GLN":"N-CA-CB-CG","GLU":"N-CA-CB-CG","HIS":"N-CA-CB-CG","ILE":"N-CA-CB-CG1","LEU":"N-CA-CB-CG","LYS":"N-CA-CB-CG","MET":"N-CA-CB-CG","PHE":"N-CA-CB-CG","PRO":"N-CA-CB-CG","SER":"N-CA-CB-OG","THR":"N-CA-CB-OG1","TRP":"N-CA-CB-CG","TYR":"N-CA-CB-CG","VAL":"N-CA-CB-CG1"}
chi2atom={"ARG":"CA-CB-CG-CD","ASN":"CA-CB-CG-OD1" ,"ASP":"CA-CB-CG-OD1" ,"GLN":"CA-CB-CG-CD","GLU":"CA-CB-CG-CD" ,"HIS":"CA-CB-CG-ND1" ,"ILE":"CA-CB-CG1-CD1" ,"LEU":"CA-CB-CG-CD1" ,"LYS":"CA-CB-CG-CD" ,"MET":"CA-CB-CG-SD" ,"PHE":"CA-CB-CG-CD1" ,"PRO":"CA-CB-CG-CD" ,"TRP":"CA-CB-CG-CD1" ,"TYR":"CA-CB-CG-CD1"}
chi3atom={"ARG":"CB-CG-CD-NE" ,"GLN":"CB-CG-CD-OE1" ,"GLU":"CB-CG-CD-OE1" ,"LYS":"CB-CG-CD-CE" ,"MET":"CB-CG-SD-CE"}
chi4atom={"ARG":"CG-CD-NE-CZ" ,"LYS":"CG-CD-CE-NZ"}
chi5atom={"ARG":"CD-NE-CZ-NH1"}

def calc_torsion(residue):
	phi=calcPhi(PROTEIN[' ',residue])
	psi=calcPsi(PROTEIN[' ',residue])
	omega=calcOmega(PROTEIN[' ',residue])
	chi1=0
	chi2=0
	chi3=0
	chi4=0
	chi5=0
	RESNAME=PROTEIN[' ',residue].getResname()
	if RESNAME in chi1atom.keys():
		chi1=calcDihedral(PROTEIN[' ',residue][chi1atom[RESNAME].split('-')[0]],PROTEIN[' ',residue][chi1atom[RESNAME].split('-')[1]],PROTEIN[' ',residue][chi1atom[RESNAME].split('-')[2]],PROTEIN[' ',residue][chi1atom[RESNAME].split('-')[3]])
	if RESNAME in chi2atom.keys():
		chi2=calcDihedral(PROTEIN[' ',residue][chi2atom[RESNAME].split('-')[0]],PROTEIN[' ',residue][chi2atom[RESNAME].split('-')[1]],PROTEIN[' ',residue][chi2atom[RESNAME].split('-')[2]],PROTEIN[' ',residue][chi2atom[RESNAME].split('-')[3]])
	if RESNAME in chi3atom.keys():
		chi3=calcDihedral(PROTEIN[' ',residue][chi3atom[RESNAME].split('-')[0]],PROTEIN[' ',residue][chi3atom[RESNAME].split('-')[1]],PROTEIN[' ',residue][chi3atom[RESNAME].split('-')[2]],PROTEIN[' ',residue][chi3atom[RESNAME].split('-')[3]])
	if RESNAME in chi4atom.keys():
		chi4=calcDihedral(PROTEIN[' ',residue][chi4atom[RESNAME].split('-')[0]],PROTEIN[' ',residue][chi4atom[RESNAME].split('-')[1]],PROTEIN[' ',residue][chi4atom[RESNAME].split('-')[2]],PROTEIN[' ',residue][chi4atom[RESNAME].split('-')[3]])
	if RESNAME in chi5atom.keys():
		chi5=calcDihedral(PROTEIN[' ',residue][chi5atom[RESNAME].split('-')[0]],PROTEIN[' ',residue][chi5atom[RESNAME].split('-')[1]],PROTEIN[' ',residue][chi5atom[RESNAME].split('-')[2]],PROTEIN[' ',residue][chi5atom[RESNAME].split('-')[3]])
	tor_temp=str(residue)+'\t'+RESNAME+'\t'
	for z in [phi,psi,omega,chi1,chi2,chi3,chi4,chi5]:
		tor_temp+=str(z)+'\t'
#	return str(residue+'\t'+RESNAME+'\t'+phi+'\t'+psi+'\t'+omega+'\t'+chi1+'\t'+chi2+'\t'+chi3+'\t'+chi4+'\t'+chi5)
	return tor_temp


#~~~ DFG state
if ID == 'LIMK1':
	RESIDUE_D={'D1':[388,479],'D2':[368,479],'D3':[478,384],'D4':[479,478],'D5':[479,481],'D8':[368,384],'D9':[368,384],'D10':[384,479],'D11':[483,457],'D12':[416,479],'D13':[350,464],'D14':[454,483]}
else:
	RESIDUE_D={'D1':[380,470],'D2':[360,470],'D3':[469,376],'D4':[470,469],'D5':[470,472],'D8':[360,376],'D9':[360,376],'D10':[376,470],'D11':[474,448],'D12':[408,470],'D13':[342,455],'D14':[445,474]}


#D1
D1=calcDistance(PROTEIN[ ' ',RESIDUE_D['D1'][0]]['CA'],PROTEIN[ ' ',RESIDUE_D['D1'][1]]['CZ'])

#D2
D2=calcDistance(PROTEIN[ ' ',RESIDUE_D['D2'][0]]['CA'],PROTEIN[ ' ',RESIDUE_D['D2'][1]]['CZ'])

#D3
D3=calcDistance(PROTEIN[' ',RESIDUE_D['D3'][0]]['CA'],PROTEIN[' ',RESIDUE_D['D3'][1]]['CA'])

#D4
D4=calcDistance(PROTEIN[' ',RESIDUE_D['D4'][0]]['N'],PROTEIN[' ',RESIDUE_D['D4'][1]]['O'])

#D5
D5=calcDistance(PROTEIN[' ',RESIDUE_D['D5'][0]]['O'],PROTEIN[' ',RESIDUE_D['D5'][1]]['N'])

#D8
D8=calcDistance(PROTEIN[' ',RESIDUE_D['D8'][0]]['CB'],PROTEIN[' ',RESIDUE_D['D8'][1]]['CB'])

#D9-check
D9a=calcDistance(PROTEIN[' ',RESIDUE_D['D9'][0]]['NZ'],PROTEIN[' ',RESIDUE_D['D9'][1]]['OE1'])
D9b=calcDistance(PROTEIN[' ',RESIDUE_D['D9'][0]]['NZ'],PROTEIN[' ',RESIDUE_D['D9'][1]]['OE2'])


#D10
D10=calcDistance(PROTEIN[' ',RESIDUE_D['D10'][0]]['CA'],PROTEIN[' ',RESIDUE_D['D10'][1]]['CA'])

#D11
D11=calcDistance(PROTEIN[' ',RESIDUE_D['D11'][0]]['N'],PROTEIN[' ',RESIDUE_D['D11'][1]]['O'])

#D12
D12=calcDistance(PROTEIN[' ',RESIDUE_D['D12'][0]]['N'],PROTEIN[' ',RESIDUE_D['D12'][1]]['CA'])

#D13
D13=calcDistance(PROTEIN[' ',RESIDUE_D['D13'][0]]['CA'],PROTEIN[' ',RESIDUE_D['D13'][1]]['CA'])

#D14
D14=calcDistance(PROTEIN[' ',RESIDUE_D['D14'][0]]['CA'],PROTEIN[' ',RESIDUE_D['D14'][1]]['CA'])


D1_D2_state='NA'

if D1 <= 11 and D2 >= 11:
	D1_D2_state='in'
elif D1 > 11 and D2 <= 14:
	D1_D2_state='out'
elif D1 <= 11 and D2 <= 11:
	D1_D2_state='inter'

D3state='NA'
if D3 <= 10.5:
	D3state='in'
elif D3 > 10.5:
	D3state='out'

D4state='NA'

if D4 <= 3.5:
	D4state='in'
else:
	D4state='out'
D5state='NA'
if D5 <= 3.5:
	D5state='in'
else:
	D5state='out'
D8state='NA'
if D8 <= 10:
	D8state='in'
elif D8 > 10:
	D8state='out'
D9astate='NA'
if D9a <= 4:
	D9astate='in'
elif D9a >= 8.5:
	D9astate='out'
else:
	D9astate='NA'

D9bstate='NA'
if D9b <= 4:
	D9bstate='in'
elif D9b >= 8.5:
	D9bstate='out'
else:
	D9bstate='NA'



D10state='NA'
if D10 < 10.5:
	D10state='in'
else:
	D10state='out'
D11state='NA'
if D11 <= 3.5:
	D11state='Extended'
else:
	D11state='NA'
D12state='NA'
if D12 <= 15:
	D12state='in'
else:
	D12state='NA'
D13state='NA'
if D13 <= 13.5:
	D13state='Collapsed'
elif D13 > 13.5:
	D13state='Stretched'
D14state='NA'
if D14 > 25:
	D14state='Close-type-2'
elif D14 < 12:
	D14state='Open-DFG-out'
elif D14 > 20:
	D14state='Closed-A-under-P'

asd=open(sys.argv[1].split('.')[0]+'_D.txt','w')
D_temp=sys.argv[1].split('.')[0]+'\t'
for f in [D1,D2,D1_D2_state,D3,D3state,D4,D4state,D5,D5state,D8,D8state,D9a,D9astate,D9b,D9bstate,D10,D10state,D11,D11state,D12,D12state,D13,D13state,D14,D14state]:
	D_temp+=str(f)+'\t'
asd.write(D_temp+'\n')
asd.close()


#TORSION
if ID == 'LIMK1':
	TOR_RES={'T1':368,'T2':458,'T3':459,'T4':460,'T5':477,'T6':478,'T7':479,'T8':480,'T9':481,'T10':384,'T11':345,'T12':352,'T13':346,'T14':347,'T15':348,'T16':349,'T17':350,'T18':351}
else:
	TOR_RES={'T1':360,'T2':449,'T3':450,'T4':451,'T5':468,'T6':469,'T7':470,'T8':471,'T9':376,'T10':472,'T11':337,'T12':344,'T13':338,'T14':339,'T15':340,'T16':341,'T17':342,'T18':343}

T1 = calc_torsion(TOR_RES['T1'])

T2 = calc_torsion(TOR_RES['T2'])

T3 = calc_torsion(TOR_RES['T3'])

T4 = calc_torsion(TOR_RES['T4'])

T5 = calc_torsion(TOR_RES['T5'])

T6 = calc_torsion(TOR_RES['T6'])

T7 = calc_torsion(TOR_RES['T7'])

T8 = calc_torsion(TOR_RES['T8'])

T9 = calc_torsion(TOR_RES['T9'])

T10 = calc_torsion(TOR_RES['T10'])

T11 = calc_torsion(TOR_RES['T11'])

T12 = calc_torsion(TOR_RES['T12'])

T13 = calc_torsion(TOR_RES['T13'])

T14 = calc_torsion(TOR_RES['T14'])

T15 = calc_torsion(TOR_RES['T15'])

T16 = calc_torsion(TOR_RES['T16'])

T17 = calc_torsion(TOR_RES['T17'])

T18 = calc_torsion(TOR_RES['T18'])


asd=open(sys.argv[1].split('.')[0]+'_T.txt','w')
T_temp=''
for f in [T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18]:
	T_temp+=sys.argv[1].split('.')[0]+'\t'+str(f)+'\n'
asd.write(T_temp+'\n')
asd.close()

#print('Torsion',T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18)


#Pesudo-torsion

if ID == 'LIMK1':
	PESUDO_RES={'P1':[477,478,479,480],'P2':[478,479,480,481],'P3':[351,352,353,354]}
else:
	PESUDO_RES={'P1':[468,469,470,471],'P2':[469,470,471,472],'P3':[343,344,345,346]}

P1 = calcDihedral(PROTEIN[' ',PESUDO_RES['P1'][0]]['CA'],PROTEIN[' ',PESUDO_RES['P1'][1]]['CA'],PROTEIN[' ',PESUDO_RES['P1'][2]]['CA'],PROTEIN[' ',PESUDO_RES['P1'][3]]['CA'])

P2 = calcDihedral(PROTEIN[' ',PESUDO_RES['P2'][0]]['CA'],PROTEIN[' ',PESUDO_RES['P2'][1]]['CA'],PROTEIN[' ',PESUDO_RES['P2'][2]]['CA'],PROTEIN[' ',PESUDO_RES['P2'][3]]['CA'])

P3 = calcDihedral(PROTEIN[' ',PESUDO_RES['P3'][0]]['CA'],PROTEIN[' ',PESUDO_RES['P3'][1]]['CA'],PROTEIN[' ',PESUDO_RES['P3'][2]]['CA'],PROTEIN[' ',PESUDO_RES['P3'][3]]['CA'])


asd=open(sys.argv[1].split('.')[0]+'_P.txt','w')
P_temp=sys.argv[1].split('.')[0]+'\t'
for f in [P1,P2,P3]:
	P_temp+=str(f)+'\t'
asd.write(P_temp+'\n')
asd.close()



#print('Pesudo',P1,P2,P3)


#Angle
if ID == 'LIMK1':
	ANG_RES={'A1':[477,478,479],'A2':[479,480,481],'A3':[478,479,480],'A6':[368,384,478]}
else:
	ANG_RES={'A1':[468,469,470],'A2':[470,471,472],'A3':[469,470,471],'A6':[360,376,469]}

A1=calcAngle(PROTEIN[' ',ANG_RES['A1'][0]]['CA'],PROTEIN[' ',ANG_RES['A1'][1]]['CA'],PROTEIN[' ',ANG_RES['A1'][2]]['CA'])

A2=calcAngle(PROTEIN[' ',ANG_RES['A2'][0]]['CA'],PROTEIN[' ',ANG_RES['A2'][1]]['CA'],PROTEIN[' ',ANG_RES['A2'][2]]['CA'])

A3=calcAngle(PROTEIN[' ',ANG_RES['A3'][0]]['CA'],PROTEIN[' ',ANG_RES['A3'][1]]['CA'],PROTEIN[' ',ANG_RES['A3'][2]]['CA'])

A6=calcAngle(PROTEIN[' ',ANG_RES['A6'][0]]['CA'],PROTEIN[' ',ANG_RES['A6'][1]]['CA'],PROTEIN[' ',ANG_RES['A6'][2]]['CA'])


asd=open(sys.argv[1].split('.')[0]+'_A.txt','w')
A_temp=sys.argv[1].split('.')[0]+'\t'
for f in [A1,A2,A3,A6]:
	A_temp+=str(f)+'\t'
asd.write(A_temp+'\n')
asd.close()



#print('PesudoAngle',A1,A2,A3,A6)





'''
#backup - 05-07-2021
RESIDUE={'D1':[380,470],'D2':[360,470],'D3':[360,380],'D4':[449,342],'D5':[469,449],'D6':[474,448],'D7':[468,449],'D8':[470,473],'D9':[470,469],'D10':[469,376],'D11':[470,472],'D12':[360,376],'D13':[360,376],'D14':[449,470],'D15':[470,442],'D16':[470,451],'D17':[470,449],'D18':[470,380],'D19':[408,470],'D20':[376,470],'D21':[470,380],'D22':[380,391],'D23':[360,469],'D24':[469,376],'D25':[445,474]}

#PROTEIN[chain,residue_number][atom_name]
#D1 Ca(380M) - Cz(470F)
D1=calcDistance(PROTEIN[' ',RESIDUE['D1'][0]]['CA'],PROTEIN[' ',RESIDUE['D1']][1]['CZ'])

#D2
D2=calcDistance(PROTEIN[' ',RESIDUE['D2'][0]]['CA'],PROTEIN[' ',RESIDUE['D2'][1]]['CZ'])

#D3
D3=calcDistance(PROTEIN[' ',RESIDUE['D3'][0]]['CB'],PROTEIN[' ',RESIDUE['D3'][1]]['CB'])

#D4
D4=calcDistance(PROTEIN[' ',RESIDUE['D4'][0]]['CA'],PROTEIN[' ',RESIDUE['D4'][1]]['CA'])

#D5
D5=calcDistance(PROTEIN[' ',RESIDUE['D5'][0]]['O'],PROTEIN[' ',RESIDUE['D5'][1]]['N'])

#D6
D6=calcDistance(PROTEIN[' ',RESIDUE['D6'][0]]['N'],PROTEIN[' ',RESIDUE['D6'][1]]['O'])

#D7
D7=calcDistance(PROTEIN[' ',RESIDUE['D7'][0]]['O'],PROTEIN[' ',RESIDUE['D7'][1]]['N'])

#D8
D8=calcDistance(PROTEIN[' ',RESIDUE['D8'][0]]['O'],PROTEIN[' ',RESIDUE['D8'][1]]['N'])

#D9
D9=calcDistance(PROTEIN[' ',RESIDUE['D9'][0]]['N'],PROTEIN[' ',RESIDUE['D9'][1]]['OD1'])

#D10
D10=calcDistance(PROTEIN[' ',RESIDUE['D10'][0]]['CA'],PROTEIN[' ',RESIDUE['D10'][1]]['CA'])

#D11
D11=calcDistance(PROTEIN[' ',RESIDUE['D11'][0]]['O'],PROTEIN[' ',RESIDUE['D11'][1]]['N'])

#D12
D12=calcDistance(PROTEIN[' ',RESIDUE['D12'][0]]['NZ'],PROTEIN[' ',RESIDUE['D12'][1]]['OE1'])

#D13
D13=calcDistance(PROTEIN[' ',RESIDUE['D13'][0]]['CB'],PROTEIN[' ',RESIDUE['D13'][1]]['CB'])

#D14-check
#D14=calcDistance(PROTEIN[' ',RESIDUE['D14'][0]][''],PROTEIN[' ',RESIDUE['D14'][1]][''])

#D15-check
#D15=calcDistance(PROTEIN[' ',RESIDUE['D15'][0]][''],PROTEIN[' ',RESIDUE['D15'][1]][''])

#D16-check
#D16=calcDistance(PROTEIN[' ',RESIDUE['D16'][0]][''],PROTEIN[' ',RESIDUE['D16'][1]][''])

#D17
D17=calcDistance(PROTEIN[' ',RESIDUE['D17'][0]]['CA'],PROTEIN[' ',RESIDUE['D17'][1]]['CA'])

#D18
D18=calcDistance(PROTEIN[' ',RESIDUE['D18'][0]]['CA'],PROTEIN[' ',RESIDUE['D18'][1]]['CA'])

#D19
D19=calcDistance(PROTEIN[' ',RESIDUE['D19'][0]]['N'],PROTEIN[' ',RESIDUE['D19'][1]]['CA'])

#D20
D20=calcDistance(PROTEIN[' ',RESIDUE['D20'][0]]['CA'],PROTEIN[' ',RESIDUE['D20'][1]]['CA'])

#D21-check
#D21=calcDistance(PROTEIN[' ',RESIDUE['D21'][0]][''],PROTEIN[' ',RESIDUE['D21'][1]][''])

#D22-check
#D22=calcDistance(PROTEIN[' ',RESIDUE['D22'][0]][''],PROTEIN[' ',RESIDUE['D22'][1]][''])

#D23
D23=calcDistance(PROTEIN[' ',RESIDUE['D23'][0]]['CA'],PROTEIN[' ',RESIDUE['D23'][1]]['CA'])

#D24
D24=calcDistance(PROTEIN[' ',RESIDUE['D24'][0]]['CA'],PROTEIN[' ',RESIDUE['D24'][1]]['CA'])

#D25-check
D25=calcDistance(PROTEIN[' ',RESIDUE['D25'][0]]['CA'],PROTEIN[' ',RESIDUE['D25'][1]]['CA'])


print(D1,D2,D1_D2_state,D3,D3state,D4,D4state,D5,D6,D7,D8,D9,D10,D11,D12,D13,D17,D18,D19,D20,D23,D24)


#TORSION

TOR_RES={'T1':360,'T2':449,'T3':450,'T4':451,'T5':468,'T6':469,'T7':470,'T8':471,'T9':376,'T10':472,'T11':337,'T12':344}

T1 = calc_torsion(TOR_RES['T1'])

T2 = calc_torsion(TOR_RES['T2'])

T3 = calc_torsion(TOR_RES['T3'])

T4 = calc_torsion(TOR_RES['T4'])

T5 = calc_torsion(TOR_RES['T5'])

T6 = calc_torsion(TOR_RES['T6'])

T7 = calc_torsion(TOR_RES['T7'])

T8 = calc_torsion(TOR_RES['T8'])

T9 = calc_torsion(TOR_RES['T9'])

T10 = calc_torsion(TOR_RES['T10'])

T11 = calc_torsion(TOR_RES['T11'])

T12 = calc_torsion(TOR_RES['T12'])

print(T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12)


#Pesudo-torsion

PESUDO_RES={'P1':[468,469,470,471],'P2':[469,470,471,472],'P3':[343,344,345,346]}

P1 = calcDihedral(PROTEIN[' ',PESUDO_RES['P1'][0]]['CA'],PROTEIN[' ',PESUDO_RES['P1'][1]]['CA'],PROTEIN[' ',PESUDO_RES['P1'][2]]['CA'],PROTEIN[' ',PESUDO_RES['P1'][3]]['CA'])

P2 = calcDihedral(PROTEIN[' ',PESUDO_RES['P2'][0]]['CA'],PROTEIN[' ',PESUDO_RES['P2'][1]]['CA'],PROTEIN[' ',PESUDO_RES['P2'][2]]['CA'],PROTEIN[' ',PESUDO_RES['P2'][3]]['CA'])

P3 = calcDihedral(PROTEIN[' ',PESUDO_RES['P3'][0]]['CA'],PROTEIN[' ',PESUDO_RES['P3'][1]]['CA'],PROTEIN[' ',PESUDO_RES['P3'][2]]['CA'],PROTEIN[' ',PESUDO_RES['P3'][3]]['CA'])

print(P1,P2,P3)


#Angle

ANG_RES={'A1':[379,380,381],'A2':[382,383,384],'A3':[383,384,385],'A4':[381,382,383],'A5':[390,391,392],'A6':[468,469,470],'A7':[469,470,471],'A8':[470,471,472],'A9':[360,376,469]}


A1=calcAngle(PROTEIN[' ',ANG_RES['A1'][0]]['CA'],PROTEIN[' ',ANG_RES['A1'][1]]['CA'],PROTEIN[' ',ANG_RES['A1'][2]]['CA'])

A2=calcAngle(PROTEIN[' ',ANG_RES['A2'][0]]['CA'],PROTEIN[' ',ANG_RES['A2'][1]]['CA'],PROTEIN[' ',ANG_RES['A2'][2]]['CA'])

A3=calcAngle(PROTEIN[' ',ANG_RES['A3'][0]]['CA'],PROTEIN[' ',ANG_RES['A3'][1]]['CA'],PROTEIN[' ',ANG_RES['A3'][2]]['CA'])

A4=calcAngle(PROTEIN[' ',ANG_RES['A4'][0]]['CA'],PROTEIN[' ',ANG_RES['A4'][1]]['CA'],PROTEIN[' ',ANG_RES['A4'][2]]['CA'])

A5=calcAngle(PROTEIN[' ',ANG_RES['A5'][0]]['CA'],PROTEIN[' ',ANG_RES['A5'][1]]['CA'],PROTEIN[' ',ANG_RES['A5'][2]]['CA'])

A6=calcAngle(PROTEIN[' ',ANG_RES['A6'][0]]['CA'],PROTEIN[' ',ANG_RES['A6'][1]]['CA'],PROTEIN[' ',ANG_RES['A6'][2]]['CA'])

A7=calcAngle(PROTEIN[' ',ANG_RES['A7'][0]]['CA'],PROTEIN[' ',ANG_RES['A7'][1]]['CA'],PROTEIN[' ',ANG_RES['A7'][2]]['CA'])

A8=calcAngle(PROTEIN[' ',ANG_RES['A8'][0]]['CA'],PROTEIN[' ',ANG_RES['A8'][1]]['CA'],PROTEIN[' ',ANG_RES['A8'][2]]['CA'])

A9=calcAngle(PROTEIN[' ',ANG_RES['A9'][0]]['CA'],PROTEIN[' ',ANG_RES['A9'][1]]['CA'],PROTEIN[' ',ANG_RES['A9'][2]]['CA'])




print(A1,A2,A3,A4,A5,A6,A7,A8,A9)
'''