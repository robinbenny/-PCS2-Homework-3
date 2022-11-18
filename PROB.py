
import math

dataset = "sample string"
number_line = "sample number"
gcc = [float(i) for i in number_line.split()]


outputs = []
prob = 0
for a_gcc in gcc:
    prob = 0
    chances = {
        'A' : (1-a_gcc)/2,
        'C' : a_gcc/2,
        'G' : a_gcc/2,
        'T' : (1-a_gcc)/2
    }
    for c in dataset:
        prob = prob + math.log10(chances[c])
    outputs.append(prob)

print(" ".join([str(i) for i in outputs]))