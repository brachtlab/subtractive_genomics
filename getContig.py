#!/usr/bin/python
from Bio import SeqIO
import sys
from sys import argv
#getContig.py <assemblyfile> <scaffold or contig>
scafname=argv[2]
outHandle=open("%s.fasta"%argv[2],'w')
genome_handle=open("%s"%argv[1],"r")
for seq_record in SeqIO.parse(genome_handle,"fasta"):
	seqlength=len(seq_record.seq)
	ident=seq_record.id
	if ident==scafname:
		outHandle.write(">%s\n%s\n"%(ident,seq_record.seq))
		print "found it!"
		break
		
genome_handle.close()
outHandle.close()
