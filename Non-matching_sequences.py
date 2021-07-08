#!/usr/bin/env python
from Bio import SeqIO
import sys
from sys import argv                        
genome_handle=open("%s"%argv[1], "r")
blast_handle=open("%s"%argv[2], "r")
out_handle=open("%s_non-matching_%s.fasta"%(argv[1],argv[2]), "w")
Dict={}
for line in blast_handle:
	ID=line.split()[0]
	Dict[ID]=1
#	print ID
for seq_record in SeqIO.parse(genome_handle, "fasta"):
	if Dict.has_key(seq_record.id):
		pass
	else: 
		out_handle.write(">%s\n%s\n"%(seq_record.id, seq_record.seq))

genome_handle.close()
blast_handle.close()
out_handle.close()
