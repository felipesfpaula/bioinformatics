import numpy as np
from Bio import SeqIO


handle = open("putative alpha-amylase.fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
    lutzomyia = record.seq
handle.close()   


handle = open("alpha-amylase [Drosophila kikkawai].fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
    drosophila = record.seq
handle.close()  


#Dot matrix algorithm
seq_a = lutzomyia
seq_b = drosophila

dim_x = len(lutzomyia)
dim_y = len(drosophila)

dotmatrix = np.zeros((dim_x, dim_y),  dtype=np.int)

for i in xrange( len(lutzomyia) ):
	for j in xrange( len(drosophila) ):
		if lutzomyia[i] == drosophila[j]:
			dotmatrix[i][j] = 1

			
np.savetxt("matrix",dotmatrix, fmt="%.0d",)

