'''
Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

Input: A DNA string Genome.
Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
'''

def MinimumSkew(genome):
    skew = [0]
    min_skew = 0
    for i in range(len(genome)):
        if genome[i] == "C":
            skew.append(skew[i] - 1)
        elif genome[i] == "G":
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
        if skew[i+1] < min_skew:
            min_skew = skew[i+1]
    return " ".join(map(str, [i for i, x in enumerate(skew) if x == min_skew]))


def MaximumSkew(genome):
    skew = [0]
    max_skew = 0
    for i in range(len(genome)):
        if genome[i] == "C":
            skew.append(skew[i] - 1)
        elif genome[i] == "G":
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
        if skew[i+1] > max_skew:
            max_skew = skew[i+1]
    return " ".join(map(str, [i for i, x in enumerate(skew) if x == max_skew]))

if __name__ == "__main__":
    genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    print(MinimumSkew(genome))

    for i in range(5):
        file_input = open(f"MinimumSkew/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        Genome = file_input_text.strip()

        file_output = open(f"MinimumSkew/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        if file_output_text == MinimumSkew(Genome).strip():
            print("yes")
        else:
            print(f"{i+1} no {MinimumSkew(Genome)}, {file_output_text}")
    
    genome = "GCATACACTTCCCAGTAGGTACTG"
    print(MaximumSkew(genome))
    