from collections import Counter

nucleotides=['A','C','G','T']
string='input'
counts = Counter(string)

for n in nucleotides:
    a = counts[n]
    print ("The count for",n,"is:",a)