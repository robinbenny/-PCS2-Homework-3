import re

profile = []
bases = {"A": 0, "C": 1, "G": 2, "T": 3}

file = open(r"C:\Users\robin\Downloads\rosalind_cons (5).txt")
groups = re.findall("[ATCG]+", file.read().replace('\n', ''))
for group in groups:
    if not profile:
        profile = [[0 for n in range(len(group))] for m in range(4)]

    for i in range(len(group)):
        profile[bases[group[i]]][i] += 1

file.close()

consensus = ""
for i in range(len(profile[0])):
    highest = 0
    for j in range(1, 4):
        if profile[j][i] > profile[highest][i]:
            highest = j

    
    consensus += list(bases.keys())[highest]

print(consensus)
for i in range(len(profile)):
    row = ""
    row += list(bases.keys())[i] + ": "
    for n in profile[i]:
        row += str(n) + " "
    print(row)