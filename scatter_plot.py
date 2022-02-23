import pandas as pd
import matplotlib.pyplot as plt
import sys
from matplotlib import rc

OPTION = int(sys.argv[2])
asd = pd.read_csv(sys.argv[1],delimiter='\t')
fig, ax = plt.subplots()
plt.rcParams.update({'font.family':'sans-serif'})
#rc('font',**{'family':'serif','serif':['Times']})

if OPTION == 1:
	#D1 vs. D2
	val_colour=[]
	val_label=[]
	#print(len(asd['D1']))
	IN=pd.DataFrame(columns=['D1','D2','Time', 'P2', 'P1','DP','XS', 'D3', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	OUT=pd.DataFrame(columns=['D1','D2','Time','P2', 'P1','DP','XS', 'D3', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	INTER=pd.DataFrame(columns=['D1','D2','Time','P2', 'P1','DP','XS', 'D3', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	NA=pd.DataFrame(columns=['D1','D2','Time','P2', 'P1','DP','XS', 'D3', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	for f in range(0,len(asd['D1'])):
		print(f,asd['D1'][f],asd['D2'][f])
		if asd['D1'][f] <= 11 and asd['D2'][f] >= 11:
			IN = IN.append({'D1':asd['D1'][f],'D2':asd['D2'][f],'Time':asd['Time'][f],'P2':asd['P2'][f], 'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D3':asd['D3'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
	#		ax.scatter(asd['D1'][f],asd['D2'][f],s=1,c='green',label='in')
	#		val_colour.append('green') #in
	#		val_label.append('in')
		elif asd['D1'][f] > 11 and asd['D2'][f] <= 14:
			OUT = OUT.append({'D1':asd['D1'][f],'D2':asd['D2'][f],'Time':asd['Time'][f],'P2':asd['P2'][f], 'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D3':asd['D3'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
	#		ax.scatter(asd['D1'][f],asd['D2'][f],s=1,c='red',label='out')
	#		val_colour.append('red') #out
	#		val_label.append('out')
		elif asd['D1'][f] <= 11 and asd['D2'][f] <= 11:
			INTER = INTER.append({'D1':asd['D1'][f],'D2':asd['D2'][f],'Time':asd['Time'][f],'P2':asd['P2'][f], 'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D3':asd['D3'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
	#		ax.scatter(asd['D1'][f],asd['D2'][f],s=1,c='blue',label='inter')
	#		val_colour.append('blue') #inter
	#		val_label.append('inter')
		else:
			NA = NA.append({'D1':asd['D1'][f],'D2':asd['D2'][f],'Time':asd['Time'][f],'P2':asd['P2'][f], 'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D3':asd['D3'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
	#		ax.scatter(asd['D1'][f],asd['D2'][f],s=1,c='black',label='NA')
	#		val_colour.append('black')
	#		val_label.append('NA')
	#print(len(val_*9+colour))
	#asd = plt.scatter(asd['D1'],asd['D2'],s=1,c=val_colour)
	#print(asd.legend_elements())
	ax.scatter(IN['D1'],IN['D2'],s=10,marker='o',c='green',label='DFG_in')
	ax.scatter(OUT['D1'],OUT['D2'],s=10,marker=',',c='red',label='DFG_out')
	ax.scatter(INTER['D1'],INTER['D2'],s=10,marker='v',c='blue',label='DFG_inter')
	ax.scatter(NA['D1'],NA['D2'],s=10,marker='o',c='black',label='NA')
	IN.to_csv('dfg_in.csv',index=False)
	INTER.to_csv('dfg_inter.csv',index=False)
	OUT.to_csv('dfg_out.csv',index=False)
	NA.to_csv('dfg_NA.csv',index=False)
	plt.xlabel('D1',fontweight='bold')
	plt.ylabel('D2',fontweight='bold')
#	plt.xlim(12,26)
#	plt.ylim(5,15)
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=4)
	fig.savefig('D1_D2_plot.jpg', dpi=600, format="jpeg")
	plt.show()
	
	if len(NA['D1']) >0:
		for f in range(0,len(asd['Time'])):
			if f in NA['Time']:
				print('NA',asd['Time'][f],asd['P1'][f],asd['P2'][f])

elif OPTION == 2:
	#P2 vs P1
	'''
	#23-08-2021
	DFG_IN=pd.DataFrame(columns=['D1','D2','Time', 'P2', 'P1','DP','XS', 'D3', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	DFG_OUT=pd.DataFrame(columns=['D1','D2','Time', 'P2', 'P1','DP','XS', 'D3', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])

	for f in range(0,len(asd['P1'])):
		print(f,asd['P2'][f],asd['P1'][f])
		if asd['P1'][f]  < 120:
			DFG_IN = DFG_IN.append({'D1':asd['D1'][f],'D2':asd['D2'][f],'Time':asd['Time'][f],'P2':asd['P2'][f], 'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D3':asd['D3'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif asd['P1'][f] >= 120:
			DFG_OUT = DFG_OUT.append({'D1':asd['D1'][f],'D2':asd['D2'][f],'Time':asd['Time'][f],'P2':asd['P2'][f], 'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D3':asd['D3'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
	'''
	DFG_IN=asd[asd['P1'] < 120]
	DFG_OUT=asd[asd['P1'] > 120]
	ax.scatter(DFG_IN['P2'],DFG_IN['P1'],s=10,marker='o',c='green',label='DFG-in')
	ax.scatter(DFG_OUT['P2'],DFG_OUT['P1'],s=10,marker=',',c='red',label='DFG-out')
#	ax.scatter(G_DOWN['P1'],G_DOWN['P2'],s=10,marker='v',c='blue',label='G Down')
#	ax.scatter(NA_P['P1'],NA_P['P2'],s=10,marker='o',c='black',label='NA')
#	ax.legend(loc='upper right')
#	DFG_IN.to_csv('dfg_in.csv',index=False)
#	DFG_OUT.to_csv('dfg_out.csv',index=False)
	plt.xlabel('P2',fontweight='bold')
	plt.ylabel('P1',fontweight='bold')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=2)
#	plt.xlim(40,62)
#	plt.ylim(-180,176)
#	fig.savefig('P2_P1_plot.jpg', dpi=600, format="jpeg")
	plt.show()
elif OPTION == 3:
	# DP vs XS
	ax.scatter(asd['DP'],asd['XS'],s=10,c='red')
	plt.xlabel('DP')
	plt.ylabel('XS')
	plt.show()
elif OPTION == 4:
	# P2 vs D3
	aC_in=pd.DataFrame(columns=['P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	aC_inter=pd.DataFrame(columns=['P2','D3','Time','DP','XS', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	aC_out=pd.DataFrame(columns=['P2','D3','Time','DP','XS', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	aC_NA=pd.DataFrame(columns=['P2','D3','Time','DP','XS', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])

	for f in range(0,len(asd['D3'])):
		print(f,asd['P2'][f],asd['D3'][f])
		if asd['D3'][f] < 9:
			aC_in = aC_in.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif asd['D3'][f] >= 9 and asd['D3'][f] < 10.5:
			aC_inter = aC_inter.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif asd['D3'][f] > 10.5:
			aC_out = aC_out.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
	ax.scatter(aC_in['P2'],aC_in['D3'],marker='o',s=10,c='green',label='aC-in')
	ax.scatter(aC_inter['P2'],aC_inter['D3'],marker=',',s=10,c='red',label='aC-inter')
	ax.scatter(aC_out['P2'],aC_out['D3'],marker='v',s=10,c='blue',label='aC-out')
	ax.legend(loc='upper right')
	aC_in.to_csv(sys.argv[1].split('.')[0]+'_aC_in.csv',index=False)
	aC_inter.to_csv(sys.argv[1].split('.')[0]+'_aC_inter.csv',index=False)
	aC_out.to_csv(sys.argv[1].split('.')[0]+'_aC_out.csv',index=False)
	plt.xlabel('P2',fontweight='bold')
	plt.ylabel('D3',fontweight='bold')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=3)
#	plt.xlim([-82,87])
#	plt.ylim([8,20])
	fig.savefig(sys.argv[1].split('.')[0]+'_P2_D3_plot.jpg', dpi=600, format="jpeg")
	plt.show()
elif OPTION == 5:
	# P1 vs D3
	plt.scatter(asd['D3'],asd['P1'],s=10,c='red')
	plt.xlabel('D3')
	plt.ylabel('P1')
#	plt.ylim([0,300])
	plt.show()

elif OPTION == 6:
	# KP vs KS
	ax.scatter(asd['KP'],asd['KS'],s=10,c='red',label='bK')
	ax.scatter(asd['CP'],asd['CS'],s=10,c='blue',label='aCE')
	ax.legend(loc='upper right')
	plt.xlabel('PHI')
	plt.ylabel('PSI')
	plt.ylim([-300,300])
	plt.show()

elif OPTION == 7:
	# K1 vs K1
	ax.scatter(asd['K1'],asd['K2'],s=10,c='red',label='bK')
	ax.scatter(asd['C1'],asd['C2'],s=10,c='blue',label='aCE')
	ax.legend(loc='upper right')
	plt.xlabel('CHI1')
	plt.ylabel('CHI2')
	plt.ylim([-300,300])
	plt.show()

elif OPTION == 8:
	#D8 - Hist
	asd.D8.plot.hist(color='grey')
	plt.xlabel('D8',fontweight='bold')
	plt.ylabel('Frequency',fontweight='bold')
	plt.axvline(x=10,color='red',linestyle='--')
#	plt.xticks([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
	fig.savefig(sys.argv[1].split('.')[0]+'_D8_plot.jpg', dpi=600, format="jpeg")
	plt.show()


elif OPTION == 9:
	#P1 - density
	asd.P1.plot.hist(color='blue')
	plt.xlabel('P1',fontweight='bold')
	plt.ylabel('Frequency',fontweight='bold')
	plt.axvline(x=120,color='red',linestyle='--')
#	plt.xticks([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
	fig.savefig(sys.argv[1].split('.')[0]+'_P1_plot.jpg', dpi=600, format="jpeg")
	plt.show()

elif OPTION == 88:
	#D13 - density
	SET1=asd[asd['D13'] <= 13.5]
	SET2=asd[asd['D13'] > 13.5]
	plt.hist(SET1['D13'],color='red',label='collapsed')
	plt.hist(SET2['D13'],color='blue',label='stretched')
	plt.xlabel('D13',fontweight='bold')
	plt.ylabel('Frequency',fontweight='bold')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=2)
	SET1.to_csv(sys.argv[1].split('.')[0]+'_D13_collapsed.csv',index=False)
	SET2.to_csv(sys.argv[1].split('.')[0]+'_D13_stretched.csv',index=False)
	fig.savefig(sys.argv[1].split('.')[0]+'_D13_plot.jpg', dpi=600, format="jpeg")
	plt.show()

elif OPTION == 77:
	#T11 
	SET1=asd[asd['T11']>80]
	SET2=asd[asd['T11']<50]
	SET3=asd[(asd['T11'] > 50) & (asd['T11'] < 80)]
	plt.hist(SET1['T11'],color='red',label='collapsed')
	plt.hist(SET2['T11'],color='blue',label='stretched')
	plt.hist(SET3['T11'],color='green',label='NA')
	plt.xlim(-180,180)
	plt.xlabel('T11',fontweight='bold')
	plt.ylabel('Frequency',fontweight='bold')
	plt.xticks([-180,-120,-60,0,60,120,180])
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=3)
	SET1.to_csv(sys.argv[1].split('.')[0]+'_T11_collapsed.csv',index=False)
	SET2.to_csv(sys.argv[1].split('.')[0]+'_T11_stretched.csv',index=False)
	SET3.to_csv(sys.argv[1].split('.')[0]+'_T11_NA.csv',index=False)
	fig.savefig(sys.argv[1].split('.')[0]+'_T11_plot.jpg', dpi=600, format="jpeg")
	plt.show()



elif OPTION == 23:
	#T12
	SET1=asd[(asd['T12'] >= 40) & (asd['T12'] <= 100)]
	SET2=asd[(asd['T12'] > 100) & (asd['T12'] <= 180)]
	SET3=asd[asd['T12'] < 40]
	plt.hist(SET1['T12'],color='red',label='collapsed')
	plt.hist(SET2['T12'],color='blue',label='stretched')
	plt.hist(SET3['T12'],color='green',label='NA')
	plt.xlim(-180,180)
	plt.xlabel('T12',fontweight='bold')
	plt.ylabel('Frequency',fontweight='bold')
	plt.xticks([-180,-120,-60,0,60,120,180])
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=3)
	SET1.to_csv(sys.argv[1].split('.')[0]+'_T12_collapsed.csv',index=False)
	SET2.to_csv(sys.argv[1].split('.')[0]+'_T12_stretched.csv',index=False)
	SET3.to_csv(sys.argv[1].split('.')[0]+'_T12_NA.csv',index=False)
	fig.savefig(sys.argv[1].split('.')[0]+'_T12_plot.jpg', dpi=600, format="jpeg")
	plt.show()

elif OPTION == 43:
	#P3
	SET1=asd[(asd['P3'] >= 100) & (asd['P3'] <= 180)]
	SET2=asd[(asd['P3'] > -180) & (asd['P3'] < -100)]
	SET3=asd[(asd['P3'] > -100) & (asd['P3'] < 100)]
	plt.hist(SET1['P3'],color='red',label='collapsed')
	plt.hist(SET2['P3'],color='blue',label='stretched')
	plt.hist(SET3['P3'],color='green',label='NA')
	plt.xlim(-180,180)
	plt.xlabel('P3',fontweight='bold')
	plt.ylabel('Frequency',fontweight='bold')
	plt.xticks([-180,-120,-60,0,60,120,180])
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=3)
	SET1.to_csv(sys.argv[1].split('.')[0]+'_P3_collapsed.csv',index=False)
	SET2.to_csv(sys.argv[1].split('.')[0]+'_P3_stretched.csv',index=False)
	SET3.to_csv(sys.argv[1].split('.')[0]+'_P3_NA.csv',index=False)
	fig.savefig(sys.argv[1].split('.')[0]+'_P3_plot.jpg', dpi=600, format="jpeg")
	plt.show()

	
elif OPTION == 11:
	#T11 - density
	'''
	SET1=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	SET2=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	SET3=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	for f in range(0,len(asd['T11'])):
		print(f,asd['T11'][f])
		if asd['T11'][f] > 80:
			SET1 = SET1.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif asd['T11'][f] <50:
			SET2 = SET2.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		else:
			SET3 = SET3.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
	SET1.plot.hist(color='green')
	SET2.plot.hist(color='blue')
	SET3.plot.hist(color='grey')
	'''
	N, bins, patches = plt.hist(asd['T11'])
	for f in range(0,len(asd['T11'])):
		print(f,asd['T11'][f])
		if asd['T11'][f] > 80:
			patches[f].set_facecolor('blue')
		elif asd['T11'][f] <50:
			patches[f].set_facecolor('red')
		else:
			patches[f].set_facecolor('black')
	plt.xlabel('T11',fontweight='bold')
	plt.ylabel('Frequency',fontweight='bold')
#	plt.axvline(x=80,color='red',linestyle='--')
#	plt.axvline(x=50,color='blue',linestyle='--')
#	plt.xticks([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
#	fig.savefig('P1_plot.jpg', dpi=600, format="jpeg")
	plt.show()


elif OPTION == 10:
	# P1 vs P2 vs D14
	CT2=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	OD=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	CAP=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	NA_D14=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	for f in range(0,len(asd['P1'])):
		print(f,asd['P1'][f],asd['P2'][f],asd['D14'][f])
		if (((asd['P2'][f] < 250) and (asd['P2'][f] >= 210)).all() and asd['D14'][f] > 25).all():
				CT2 = CT2.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif (((asd['P2'][f] < 65) and (asd['P2'][f] >= -30)).all() and asd['D14'][f] < 12).all():
			OD = OD.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif (((asd['P2'][f] < 180) and (asd['P2'][f] >= 105)).all() and asd['D14'][f] > 20).all():
			CAP = CAP.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		else:
			NA_D14 = NA_D14.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)

	ax.scatter(CT2['P2'],CT2['D14'],c='green',marker='o',label='Close-Type-2',s=10)
	ax.scatter(OD['P2'],OD['D14'],c='red',marker=',',label='Open-DFG-out',s=10)
	ax.scatter(CAP['P2'],CAP['D14'],c='blue',marker='v',label='Close-A-under-P',s=10)
	ax.scatter(NA_D14['P2'],NA_D14['D14'],c='black',marker='o',label='NA',s=10)
	plt.xlabel('P2',fontweight='bold')
	plt.ylabel('D14',fontweight='bold')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.125),fancybox=True,ncol=4)
	fig.savefig(sys.argv[1].split('.')[0]+'_AL_plot.jpg', dpi=600, format="jpeg")
	CT2.to_csv(sys.argv[1].split('.')[0]+'_CT2.csv',index=False)
	OD.to_csv(sys.argv[1].split('.')[0]+'_OD.csv',index=False)
	CAP.to_csv(sys.argv[1].split('.')[0]+'_CAP.csv',index=False)
	NA_D14.to_csv(sys.argv[1].split('.')[0]+'_NA.csv',index=False)
	plt.show()
	'''
	ax.scatter(CT2['P1'],CT2['P2'],c=CT2['D14'],marker='.',label='Close-Type-2',vmin=25,vmax=9999)
	ax.scatter(OD['P1'],OD['P2'],c=OD['D14'],marker=',',label='Open-DFG-out',vmin=0,vmax=11.9999)
	ax.scatter(CAP['P1'],CAP['P2'],c=CAP['D14'],marker='v',label='Close-A-under-P',vmin=20,vmax=999)
	ax.scatter(NA_D14['P1'],NA_D14['P2'],c=NA_D14['D14'],marker='o',label='NA')
	ax.set_xlabel('P1',fontweight='bold')
	ax.set_ylabel('P2',fontweight='bold')
	ax.legend()
	'''
	'''
#	CT2.to_csv('CT2.csv',index=False)
#	OD.to_csv('OD.csv',index=False)
#	CAP.to_csv('CAP.csv',index=False)
#	NA_D14.to_csv('NA_D14.csv',index=False)
	fig= plt.figure()
	ax = fig.add_subplot(projection='3d')
	ax.scatter(CT2['P1'],CT2['P2'],CT2['D14'],c='green',marker='.',label='Close-Type-2')
	ax.scatter(OD['P1'],OD['P2'],OD['D14'],c='red',marker=',',label='Open-DFG-out')
	ax.scatter(CAP['P1'],CAP['P2'],CAP['D14'],c='blue',marker='v',label='Close-A-under-P')
	ax.scatter(NA_D14['P1'],NA_D14['P2'],NA_D14['D14'],c='black',marker='o',label='NA')
	ax.set_xlabel('P1')
	ax.set_ylabel('P2')
	ax.set_zlabel('D14')	
	plt.show()
	'''
elif OPTION == 33:
	# XDFG PHI VS PSI
	ax.scatter(asd['XP'],asd['XS'],s=10,c='black',label='X',marker='o')
	ax.scatter(asd['DP'],asd['DS'],s=10,c='red',label='D',marker=',')
	ax.scatter(asd['FP'],asd['FS'],s=10,c='blue',label='F',marker='v')
	ax.scatter(asd['GP'],asd['GS'],s=10,c='green',label='G',marker='o')
	#ax.legend(loc='upper right')
	plt.xlabel('PHI',fontweight='bold')
	plt.ylabel('PSI',fontweight='bold')
	plt.axvline(x=0,color='grey',linestyle='--')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=4)
	plt.xlim([-180,180])
	plt.ylim([-180,180])
	plt.axvline(x=0,color='grey',linestyle='--')
	plt.axhline(y=0,color='grey',linestyle='--')
	plt.xticks([-180,-120,-60,0,60,120,180])
	plt.yticks([-180,-120,-60,0,60,120,180])
	fig.savefig('PHI_PSI_plot.jpg', dpi=600, format="jpeg")
	plt.show()


##### CHI1 VS CHI2


elif OPTION == 55:
	# XDFG CHI1 VS CHI2
#	ax.scatter(asd['X1'],asd['X2'],s=10,c='black',label='X',marker='o')
	ax.scatter(asd['DC1'],asd['DC2'],s=10,c='red',label='D',marker=',')
	ax.scatter(asd['F1'],asd['F2'],s=10,c='blue',label='F',marker='v')
#	ax.scatter(asd['G1'],asd['G2'],s=10,c='green',label='G',marker='o')
	#ax.legend(loc='upper right')
	plt.xlabel('CHI1',fontweight='bold')
	plt.ylabel('CHI2',fontweight='bold')
	plt.legend(loc="upper center", bbox_to_anchor=(0.5,1.1),fancybox=True,ncol=4)
	plt.xlim([-180,180])
	plt.ylim([-180,180])
	plt.axvline(x=0,color='grey',linestyle='--')
	plt.axhline(y=0,color='grey',linestyle='--')
	plt.xticks([-180,-120,-60,0,60,120,180])
	plt.yticks([-180,-120,-60,0,60,120,180])
	fig.savefig('CHI1_CHI2_plot.jpg', dpi=600, format="jpeg")
	plt.show()







elif OPTION == 99:
	# Master index with Time,DFG-1,DFG-2,aC,AL,PL
	MASTER_DICT={'Time':[],'DFG-1':[],'DFG-2':[],'aC':[],'AL':[],'PL':[]}
	#D1 vs. D2
	for f in range(0,len(asd['P1'])):
		print(f)
		MASTER_DICT['Time'].append(asd['Time'][f])
		if asd['D1'][f] <= 11 and asd['D2'][f] >= 11: #in
			MASTER_DICT['DFG-1'].append('IN')
		elif asd['D1'][f] > 11 and asd['D2'][f] <= 14: #out
			MASTER_DICT['DFG-1'].append('OUT')
		elif asd['D1'][f] <= 11 and asd['D2'][f] <= 11:	#inter
			MASTER_DICT['DFG-1'].append('INTER')
		else:	#NA
			MASTER_DICT['DFG-1'].append('NA')
		if asd['P1'][f]  < 120:	#in
			MASTER_DICT['DFG-2'].append('IN')
		elif asd['P1'][f] >= 120:	#out
			MASTER_DICT['DFG-2'].append('OUT')
		if asd['D3'][f] < 9:	#aC in
			MASTER_DICT['aC'].append('IN')
		elif asd['D3'][f] >= 9 and asd['D3'][f] < 10.5:	#ac inter
			MASTER_DICT['aC'].append('INTER')
		elif asd['D3'][f] > 10.5:	#aC out
			MASTER_DICT['aC'].append('OUT')
		PL_TEMP=""
		if asd['P1'][f] > 120:
			if asd['P2'][f] < 250:
				print()
				if asd['P2'][f] >= 210:
					if asd['D14'][f] > 25:	#CT2
						PL_TEMP='CT2'
		
		if asd['P1'][f] > 120:
			if asd['P2'][f] < 65:
				if asd['P2'][f] >= -30:
					if asd['D14'][f] < 12: #OD
						PL_TEMP='OD'

		if asd['P1'][f] > 120:
			if asd['P2'][f] < 180:
				if asd['P2'][f] >= 105:
					if asd['D14'][f] > 20: #CAP
						PL_TEMP='CAP'
		if PL_TEMP:
			MASTER_DICT['AL'].append(PL_TEMP)
		else: #NA
			MASTER_DICT['AL'].append('NA')
		PLC=0
		PLS=0
		if asd['T11'][f] > 80:
			PLC+=1
		elif asd['T11'][f] < 50:
			PLS+=1
		if (asd['T12'][f] <= 100 and asd['T12'][f] >=40).all():
			PLC+=1
		elif (asd['T12'][f] <= 180 and asd['T12'][f] > 100).all():
			PLS+=1
		if (asd['P3'][f] <= 180 and asd['P3'][f] >= 100).all():
			PLC+=1
		elif (asd['P3'][f] < -100 and asd['P3'][f] > -180).all():
			PLS+=1
		if asd['D13'][f] <= 13.5:
			PLC+=1
		elif asd['D13'][f] > 13.5:
			PLS+=1
		if PLC >= 3:
			MASTER_DICT['PL'].append('CL')
		elif PLS >= 3:
			MASTER_DICT['PL'].append('ST')
		else:
			MASTER_DICT['PL'].append('NA')

	MASTER = pd.DataFrame(MASTER_DICT)
	MASTER.to_csv('MASTER_file.txt',index=False,sep='\t')
	

	'''
	# P2 vs D3
	aC_in=pd.DataFrame(columns=['P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	aC_inter=pd.DataFrame(columns=['P2','D3','Time','DP','XS', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	aC_out=pd.DataFrame(columns=['P2','D3','Time','DP','XS', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	aC_NA=pd.DataFrame(columns=['P2','D3','Time','DP','XS', 'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])

	for f in range(0,len(asd['D3'])):
		print(f,asd['P2'][f],asd['D3'][f])
		if asd['D3'][f] < 9:
			aC_in = aC_in.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif asd['D3'][f] >= 9 and asd['D3'][f] < 10.5:
			aC_inter = aC_inter.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif asd['D3'][f] > 10.5:
			aC_out = aC_out.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
	ax.scatter(aC_in['P2'],aC_in['D3'],marker='.',s=10,c='green',label='aC-in')
	ax.scatter(aC_inter['P2'],aC_inter['D3'],marker=',',s=10,c='red',label='aC-inter')
	ax.scatter(aC_out['P2'],aC_out['D3'],marker='v',s=10,c='blue',label='aC-out')
	ax.legend(loc='upper right')
	aC_in.to_csv('aC_in.csv',index=False)
	aC_inter.to_csv('aC_inter.csv',index=False)
	aC_out.to_csv('aC_out.csv',index=False)

	# P1 vs P2 vs D14
	CT2=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	OD=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	CAP=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	NA_D14=pd.DataFrame(columns=['P1','P2','D3','Time','DP','XS',  'D8', 'D9A', 'C1', 'C2', 'D9B','D11','D14', 'D13', 'P3', 'T11', 'T12', 'KP', 'KS', 'K1', 'K2', 'CP', 'CS', 'XP', 'DS', 'DC1', 'DC2', 'FP', 'FS', 'F1', 'F2', 'GP', 'GS'])
	for f in range(0,len(asd['P1'])):
		print(f,asd['P1'][f],asd['P2'][f],asd['D14'][f])
		if ((asd['P1'][f] > 120).all() and ((asd['P2'][f] < 250) and (asd['P2'] >= 210)).all() and asd['D14'][f] > 25).all():
				CT2 = CT2.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif ((asd['P1'][f] > 120).all() and ((asd['P2'][f] < 65) and (asd['P2'] >= -30)).all() and asd['D14'][f] < 12).all():
			OD = OD.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		elif ((asd['P1'][f] > 120).all() and ((asd['P2'][f] < 180) and (asd['P2'] >= 105)).all() and asd['D14'][f] > 20).all():
			CAP = CAP.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)
		else:
			NA_D14 = NA_D14.append({'P2':asd['P2'][f],'D3':asd['D3'][f],'Time':asd['Time'][f],'P1':asd['P1'][f],'DP':asd['DP'][f],'XS':asd['XS'][f], 'D8':asd['D8'][f], 'D9A':asd['D9A'][f], 'C1':asd['C1'][f], 'C2':asd['C2'][f], 'D9B':asd['D9B'][f],'D11':asd['D11'][f],'D14':asd['D14'][f], 'D13':asd['D13'][f], 'P3':asd['P3'][f], 'T11':asd['T11'][f], 'T12':asd['T12'][f], 'KP':asd['KP'][f], 'KS':asd['KS'][f], 'K1':asd['K1'][f], 'K2':asd['K2'][f], 'CP':asd['CP'][f], 'CS':asd['CS'][f], 'XP':asd['XP'][f], 'DS':asd['DS'][f], 'DC1':asd['DC1'][f], 'DC2':asd['DC2'][f], 'FP':asd['FP'][f], 'FS':asd['FS'][f], 'F1':asd['F1'][f], 'F2':asd['F2'][f], 'GP':asd['GP'][f], 'GS':asd['GS'][f]},ignore_index = True)


	CT2.to_csv('CT2.csv',index=False)
	OD.to_csv('OD.csv',index=False)
	CAP.to_csv('CAP.csv',index=False)
	NA_D14.to_csv('NA_D14.csv',index=False)
	'''

'''
	#D3 - density
	asd.D3.plot.density(color='black')
	plt.xlabel('D3')


	# P1 vs D3
	plt.scatter(asd['P1'],asd['D3'],s=1)
	plt.xlabel('P1')
	plt.ylabel('D3')
	#plt.xlim([0,300])
	#plt.ylim([0,25])

	#D8 - density
	asd.D8.plot.density(color='black')
	plt.xlabel('D8')


	#D9 - density
	asd.D9.plot.density(color='black')
	plt.xlabel('D9')


	# D3 vs P2
	plt.scatter(asd['D3'],asd['P2'],s=1)
	plt.xlabel('D3')
	plt.ylabel('P2')
	#plt.xlim([0,300])
	#plt.ylim([0,25])


'''


'''
#psi 468 vs phi 469
plt.scatter(asd['Psi'],asd['Phi'],s=1)
plt.xlabel('Psi')
plt.ylabel('Phi')
'''


#plt.rcParams["font.family"] = "Arial"

#fig.savefig('D1_D2_plot.jpg', dpi=600, format="jpeg")
#fig.savefig('D1_D2_plot.tiff', dpi=600, format="tiff", pil_kwargs={"compression": "tiff_lzw"})
#plt.show()

