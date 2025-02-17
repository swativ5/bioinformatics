'''
Note that we can compute Skew i+1(Genome) from Skew i(Genome) according to the nucleotide in position i of Genome. 
If this nucleotide is G, then Skewi+1(Genome) = Skewi(Genome) + 1; 
if this nucleotide is C, then Skewi+1(Genome)= Skewi(Genome) – 1; 
otherwise, Skewi+1(Genome) = Skewi(Genome).
'''

def skew(genome):
    skew = [0]
    for i in range(len(genome)):
        if genome[i] == "C":
            skew.append(skew[i] - 1)
        elif genome[i] == "G":
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew

if __name__ == "__main__":
    # genome = "CATGGGCATCGGCCATACGCC"
    # print(skew(genome))
    genome = "GAGCCACCGCGATA"
    print(skew(genome)) 

    genome = "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"
    print(skew(genome))
    m = max(skew(genome))
    print([i for i, x in enumerate(skew(genome)) if x == m])