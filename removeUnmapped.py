#!/usr/bin/python
from Bio import SeqIO
import sys
from sys import argv
import math
inHandle=open("%s"%argv[1],"r")
outHandle=open("%s_removeUnmapped.sam"%argv[1],"w")
unmappedHandle=open("%s_contigs_with_no_reads.txt"%argv[1],"w")
i=0
j=0
x=0
mappedContigDict={}
for line in inHandle:
	if line[:1] !="@":
		readflag=line.split()[1]
		colons=readflag.count(':')
		if colons !=0:
			mapcontig=line.split()[3]
			readflag=line.split()[2]
		readflag=int(readflag)
                binstring=bin(readflag)
                reversebinstring=binstring[::-1]
                bpos=reversebinstring.find("b")
                binstringclip=reversebinstring[:bpos]
                length=len(binstringclip)
                flag=binstringclip.ljust(11,'0')
                unmapped=int(flag[2])
                if unmapped==0:
			contig=line.split()[2]
			mappedContigDict[contig]=1
inHandle.close()
inHandle=open("%s"%argv[1],"r")
for line in inHandle:
	if line[:1] !="@":
		j+=1
		readflag=line.split()[1]
		colons=readflag.count(':')
		if colons !=0:
			mapcontig=line.split()[3]
			readflag=line.split()[2]
		readflag=int(readflag)
		binstring=bin(readflag)
		reversebinstring=binstring[::-1]
		bpos=reversebinstring.find("b")
		binstringclip=reversebinstring[:bpos]
		length=len(binstringclip)
		flag=binstringclip.ljust(11,'0')
		unmapped=int(flag[2])
		if unmapped==0:
			outHandle.write(line)
			
		else:
			i+=1
		if j%10000==0:
			print "processed %s reads and %s unmapped, kicked out %s contig headers for having no reads"%(j,i,x)
	elif line[:3]=='@SQ':		
		contigplus=line.split()[1]
		contig=contigplus.lstrip("SN:")
		if mappedContigDict.has_key(contig):
                	outHandle.write(line)
                else:
			unmappedHandle.write("%s\n"%contig)
               		x+=1
	
print "removed %s unmapped from %s reads and %s contigs with no reads found (and written to file.)"%(i,j,x)
inHandle.close()
outHandle.close()
unmappedHandle.close()
