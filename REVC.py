sequence = 'input'
ans = []
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

for nucleotide in sequence:
    ans.append(complement[nucleotide])

print (''.join(ans[::-1]))