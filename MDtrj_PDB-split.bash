#!/bin/bash
#a=0;while read -r l;do echo "$l" >>MODEL_"$a".pdb; if [ "$l" == 'ENDMDL' ]; then echo "$a";python mdfilename.py MODEL_"$a".pdb; echo -e "$(ls *.pdb | cut -d'.' -f1)\t$(perl dfgcluster.pl *.pdb 368 384 478 | grep 'Kinase')" >>3s95_dunbark.txt;rm *.pdb;a=`expr $a + 1`;break;fi;done <../3S95A/microsecond_analysis/3S95_trj.pdb

a=0
while read -r l
do
	echo "$l" >>MODEL_"$a".pdb

#	temp=$(echo "$l" | grep 'TITLE')
#	if [ -n "$temp" ]
#	then 
#		NAME=$(echo "$l" | head ../3S95A/microsecond_analysis/3S95_trj.pdb | grep 'TITLE' | cut -d ' ' -f12 | cut -d'.' -f1)
#	fi
	if [ "$l" == 'ENDMDL' ]
	then
		NAME=$(python mdfilename.py MODEL_"$a".pdb)
		echo "$NAME"
		echo -e "$(echo "$NAME"),$(perl dfgcluster.pl "$NAME".pdb 368 384 478 | grep 'Kinase' | sed "s/\s\s\s\s\s/,/g;s/\s\s\s\s/,/g;s/\s\s/,/g;s/\s/,/g")" >>trj_5nxc.txt
#awk -OFS'\t' '{print $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13}'
		a=`expr $a + 1`
		 "$NAME".pdb
	fi
done < ../5nxc_mdtrj.pdb
