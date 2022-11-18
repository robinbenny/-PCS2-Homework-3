# from __future__ import division


max_gc = 0.0

with open(r'R:\bioinformatics 2 year\PCS2\HW 3\rosalind_gc.txt') as f:
    content = f.readlines()
    for i, line in enumerate(content):
        if line.startswith('>'):
            id = line[1:]
            seq = ''
        else:
            newseq = line.strip()
            seq = seq + newseq
            
            if i==len(content)-1 or content[i+1].startswith('>'):
                gc = 100 * (seq.count('G') + seq.count('C')) / len(seq)
                if gc > max_gc:
                    max_gc = gc
                    max_id = id

print(max_id, end='')
print(max_gc)