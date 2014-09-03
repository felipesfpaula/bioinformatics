import numpy as np

#Smith–Waterman algorithm for global sequence alignment written
#in a 'didatic' way

#Inputs
seq_a = "ACACACTA" 
dim_x = len(seq_a)
seq_b ="AGCACACA"
dim_y = len(seq_b)

#Algorithm's parameters
gap = -1
amatch = 2
amismatch = -1

#Put a symbol in the begging to mantain indexes' consistency
seq_a = "." + seq_a
seq_b = "." + seq_b
def match(i,j):
	if seq_a[i] ==  seq_b[j]:
		return amatch
	else: 
		return amismatch


#Matrix init
S = np.zeros((dim_x+1, dim_y+1),  dtype=np.int)

for i in xrange(1,dim_x+1):
	for j in xrange(1,dim_y+1):
		S[i][j] = max( 0 ,
					   S[i-1][j-1] + match(i,j) , 
					   S[i][j-1] + gap ,
					   S[i-1][j] + gap)
					  

#Backtrack
sequence1 = ""	
sequence2 = ""	

i,j =  np.unravel_index(S.argmax(), S.shape)
score = S[i][j]
while(S[i][j] != 0):
	
	if (i > 0 and j > 0 and S[i-1][j-1] >= S[i-1][j] and S[i-1][j-1] >= S[i][j-1]):
		sequence1 = seq_a[i] + sequence1
		sequence2 = seq_b[j] + sequence2
		i -= 1
		j -= 1
	elif (i > 0 and S[i-1][j] >= S[i-1][j-1] and S[i-1][j] >= S[i][j-1]):
		sequence1 = seq_a[i] + sequence1
		sequence2 = "-" + sequence2
		i = i-1

	elif (j > 0 and S[i][j-1] >= S[i-1][j-1]  and S[i][j-1] >= S[i-1][j]):
		sequence2 = seq_b[j] + sequence2
		sequence1 = "-" + sequence1
		j = j-1

	score += S[i][j]

print S
print sequence1
print sequence2
print score

np.savetxt("matrix",S, fmt="%1.1d",)
