from enum import Enum
class Allele(Enum):
    DOMINANT = 1,
    RECESSIVE = 2,
    HET = 3


def mate(x,y):
    if x == Allele.DOMINANT and y == Allele.DOMINANT:
        return [Allele.DOMINANT]*4
    if x == Allele.RECESSIVE and y == Allele.RECESSIVE:
        return [Allele.RECESSIVE]*4
    if x == Allele.HET and y == Allele.HET:
        return [Allele.DOMINANT, Allele.HET, Allele.HET, Allele.RECESSIVE]
    if x == Allele.HET:
        return [Allele.HET, Allele.HET, y, y]
    if y == Allele.HET:
        return [Allele.HET, Allele.HET, x, x]
    else:#DOMINANT AND RECISSIVE
        return [Allele.HET]*4


def get_pairs(organisms):
    if len(organisms) < 2:
        return list()
    first = organisms[0]
    pairs = [(first, organisms[second_index]) for second_index in range(1, len(organisms))]
    other_pairs = get_pairs(organisms[1:])
    pairs.extend(other_pairs)
    return pairs

def f(AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa):
    children = list()
    for i in range(AAAA):
        children.extend(mate(Allele.DOMINANT, Allele.DOMINANT))
    for i in range(AAAa):
        children.extend(mate(Allele.DOMINANT, Allele.HET))
    for i in range(AAaa):
        children.extend(mate(Allele.DOMINANT, Allele.RECESSIVE))
    for i in range(AaAa):
        children.extend(mate(Allele.HET, Allele.HET))
    for i in range(Aaaa):
        children.extend(mate(Allele.HET, Allele.RECESSIVE))
    for i in range(aaaa):
        children.extend(mate(Allele.RECESSIVE, Allele.RECESSIVE))

    count_dominant_presence = 0
    for child in children:
        if child is not Allele.RECESSIVE:
            count_dominant_presence += 1

    return count_dominant_presence/2

AAAA = 18498 
AAAa = 19963
AAaa = 19188
AaAa = 16663
Aaaa = 17533
aaaa = 19871

print(f(AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa))