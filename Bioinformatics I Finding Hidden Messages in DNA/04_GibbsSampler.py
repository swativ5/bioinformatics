'''
GibbsSampler(Dna, k, t, N)
    randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    BestMotifs ← Motifs
    for j ← 1 to N
        i ← Random(t)
        Profile ← profile matrix constructed from all strings in Motifs except for Motifi
        Motifi ← Profile-randomly generated k-mer in the i-th sequence
        if Score(Motifs) < Score(BestMotifs)
            BestMotifs ← Motifs
    return BestMotifs

Code Challenge: Implement GibbsSampler.
    Input: Integers k, t, and N, followed by a space-separated collection of strings Dna.
    Output: The strings BestMotifs resulting from running GibbsSampler(Dna, k, t, N) with 20 random starts. Remember to use pseudocounts!

Sample Input:
8 5 100
CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA

Sample Output:
TCTCGGGG CCAAGGTG TACAGGCG TTCAGGTG TCCACGTG
'''

import random

def Random(probabilities):
    n = random.uniform(0, sum(probabilities))
    curr = 0
    for i, p in enumerate(probabilities):
        curr += p
        if curr >= n:
            return i

def parsing(text):
    lines = text.strip().split("\n")
    k, t, N = map(int, lines[0].split())
    Dna = []
    for i in range(1, len(lines)):
        line = lines[i].split()
        for j in range(len(line)):
            Dna.append(line[j])
    return Dna, k, t, N


def PseudoProfileMatrix(Motifs):
    k = len(Motifs[0])
    seq_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    P = [[1.0] * k for _ in range(4)]

    for motif in Motifs:
        for i in range(k):
            P[seq_dict[motif[i]]][i] += 1

    n = len(Motifs) + 4
    for i in range(4):
        for j in range(k):
            P[i][j] /= n

    return P

def Pr(Dna, Profile):
    seq_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    prob = 1
    for i in range(len(Dna)):
        prob *= Profile[seq_dict[Dna[i]]][i]
    return prob

def ProfileRandomlyGeneratedKmer(Text, k, Profile):
    l = len(Text)
    probabilities = [Pr(Text[i:i+k], Profile) for i in range(l - k + 1)]
    total_prob = sum(probabilities)
    if total_prob == 0:
        probabilities = [1/(l - k + 1)] * (l - k + 1)
    else:
        probabilities = [p / total_prob for p in probabilities]
    i = Random(probabilities)
    return Text[i:i+k]


def Score(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    seq_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    count = [[0] * 4 for _ in range(k)]

    for motif in Motifs:
        for i in range(k):
            count[i][seq_dict[motif[i]]] += 1

    total_score = 0
    for i in range(k):
        max_freq = max(count[i])
        total_score += (t - max_freq)
    return total_score

def OneGibbsSampler(Dna, k, t, N):
    l = len(Dna[0])
    m = [random.randint(0, l - k) for _ in range(t)]
    motifs = [Dna[i][m[i]:m[i] + k] for i in range(t)]
    BestMotifs = motifs
    BestScore = Score(BestMotifs)

    for j in range(N):
        i = random.randint(0, t - 1)
        Profile = PseudoProfileMatrix(motifs[:i] + motifs[i+1:])
        motif_i = ProfileRandomlyGeneratedKmer(Dna[i], k, Profile)
        motifs = motifs[:i] + [motif_i] + motifs[i+1:]
        currentScore = Score(motifs)
        if currentScore < BestScore:
            BestMotifs = motifs[:]
            BestScore = currentScore
    return BestMotifs, BestScore

def GibbsSampler(Dna, k, t, N, runs=20):
        BestScore = float('inf')
        BestMotifs = None
        random.seed()
        for _ in range(runs):
            currentBestMotifs, currentBestScore = OneGibbsSampler(Dna, k, t, N)
            if currentBestScore < BestScore:
                BestMotifs = currentBestMotifs
                BestScore = currentBestScore
        return BestMotifs

if __name__ == "__main__":
    for i in range(1):
        file_input = open(f"GibbsSampler/inputs/input_{i + 1}.txt")
        text = file_input.read().strip()
        Dna, k, t, N = parsing(text)
        file_output = open(f"GibbsSampler/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()
        file_output_dna = file_output_text.strip().split()
        predicted_output = GibbsSampler(Dna, k, t, N)

        expected_score = Score(file_output_dna)
        predicted_score = Score(predicted_output)

        if predicted_score <= expected_score:
            print("yes")
        else:
            print("no", file_output_dna, predicted_output, expected_score, predicted_score)
    k = 20
    t = 10
    N = 200
    Dna = """GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC
    CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG
    ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC
    GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC
    GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG
    CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA
    GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA
    GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG
    GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG
    TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"""
    Dna = Dna.strip().split("\n")
    for i in range(len(Dna)):
        Dna[i] = Dna[i].strip()
    # print(GibbsSampler(Dna, k, t, N, runs=2000))
    Dna = ['CGGGACTTCAGGCCCTATCG', 'CGGGTCAAACGACCCTAGTG', 'CGGGACGTAAGTCCCTAACG', 'CCGGGCTTCCAACCGTGGCC', 'CGTGACCGACGTCCCCAGCC', 'GAGGACCTTCGGCCCCACCC', 'GGGGACTTCTGTCCCTAGCC', 'TGGGACTTTCGGCCCTGTCC', 'GGGGACCAACGCCCCTGGGA', 'GGGGACCGAAGTCCCCGGGC']
    print(" ".join(Dna))
