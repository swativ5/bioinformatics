"""
RandomizedMotifSearch(Dna, k, t)
    randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    BestMotifs ← Motifs
    while forever
        Profile ← Profile(Motifs)
        Motifs ← Motifs(Profile, Dna)
        if Score(Motifs) < Score(BestMotifs)
            BestMotifs ← Motifs
        else
            return BestMotifs

Code Challenge: Implement RandomizedMotifSearch.
    Input: Integers k and t, followed by a space-separated collection of strings Dna.
    Output: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1,000 times. Remember to use pseudocounts!


Sample Input:
8 5
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA

Sample Output:
TCTCGGGG CCAAGGTG TACAGGCG TTCAGGTG TCCACGTG

"""

import random

def parsing(text):
    text = text.split("\n")
    k, t = map(int, text[0].split())
    Dna = text[1:][0].split()
    return k, t, Dna

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

def ProfileMostProbableKmer(Text, k, Profile):
    max_prob = -1
    most_probable_kmer = Text[:k]
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]
        prob = Pr(kmer, Profile)
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    return most_probable_kmer

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

def fMotifs(Profile, Dna):
    motifs = []
    k = len(Profile[0])
    for dna in Dna:
        motifs.append(ProfileMostProbableKmer(dna, k, Profile))
    return motifs

def OneRandomizedMotifSearch(Dna, k, t):
    l = len(Dna[0])
    m = [random.randint(0, l - k) for _ in range(t)]
    motifs = [Dna[i][m[i]:m[i] + k] for i in range(t)]
    BestMotifs = motifs
    BestScore = Score(BestMotifs)

    while True:
        Profile = PseudoProfileMatrix(motifs)
        motifs = fMotifs(Profile, Dna)
        currentScore = Score(motifs)
        if currentScore < BestScore:
            BestMotifs = motifs[:]
            BestScore = currentScore
        else:
            return BestMotifs, BestScore

def RandomizedMotifSearch(Dna, k, t, runs=1000):
    BestMotifs = None
    BestScore = float('inf')
    random.seed()
    for _ in range(runs):
        currentBestMotifs, currentBestScore = OneRandomizedMotifSearch(Dna, k, t)
        if currentBestScore < BestScore:
            BestMotifs = currentBestMotifs
            BestScore = currentBestScore
    return BestMotifs

if __name__ == "__main__":
    # for i in range(3):
    #     file_input = open(f"RandomizedMotifSearch/inputs/input_{i + 1}.txt")
    #     text = file_input.read().strip()
    #     k, t, Dna = parsing(text)
    #     file_output = open(f"RandomizedMotifSearch/outputs/output_{i + 1}.txt")
    #     file_output_text = file_output.read().strip()
    #     file_output_dna = file_output_text.strip().split()
    #     predicted_output = RandomizedMotifSearch(Dna, k, t)

    #     if set(file_output_dna) == set(predicted_output):
    #         print("yes")
    #     else:
    #         print("no", file_output_dna, predicted_output)

    # k, t = 15, 20
    # Dna = """GACTGAGCTTGCCAGGTGATGAGAAGGTGCTACCGTGAATTTATGGCGTATTATTTACCCCAGAATACTCGTAATAGGTGGCACCGCGTGCGTGCATATTGGGCTTGAGCGTTCCCTACCCTACATTGTTACTAGCCGGTTTTTTCGAAAGACTGAGCTTGCCAG GTGATGAGAAGGTGCTACCGTGAATTTATGGCGTATTATTTACCCCAGAATACTCGTAATAGGTGGCACCGCGTGCGTGCATATTGGGCTTGAGCGTTCCCTACCCTACATTGTTACTAGCCGGTTTTTAAGTCGTATCTCGGATCGAAAGACTGAGCTTGCCAG TAGAGACCGATTGCATACTATCAGTGGTCTGAATTTATGAACATATGCGATCCCCTGTAATGATCCCTATCTCGTTTAGGTGTCAGAGGGCGGCCTGCGACAGAGACGATCATTCAACTTAAGAGGTATCTCGGAAGTGGAGTAGCACCAAATTACGCGCGTCAA AGTGCTTATAGCGCGGCAAGGGATCTACTATCTCGGATCATGCGTTCGCCAAACCGGTGACGAGTGAGTTCACTCAGGTAAGGATTCCCACGGTGACTCTACCAAGATGACCAGGTCTGCACCCTCACCGTTATGTAGGACAATGATATCGAGGGATGATTAAAG CAGAAAAGACGAACCACGATATCAGCAAGTTCCTCATGTGTCAAGCGCACAGGAAAAGCACTAAGCCGGACACCGTGCTAGTAAAAGATCCTGGGCAGAAGAGGGACGGCTGGGAGAGTTCCCCGGTCTATTCCCCAGCGAGACTAGCCGGTGAGCCAAATCCTT GACTCGGTTAGTCGCCTAGCATAGTAGCGCGATCTAGTCTACCACAGCGGGTCCCTGCCCCCGGCTATGTGGTGGTCCTAGTTGATCAAATGGGGCCGGCATTTCAGTTGGTTTAACTAGACTCCGTGCCTCTGGGACGTTTGCCTCGGGCACTATCTCGGGCCC CGGGACGGCATGTATTTATGCGGGATGTGGACATGTTAACAGAGACAGGTTTTTCCTCAAATGCTATCTCGGAACTGCGCATTGATCTCCGTCCATTGTAACATGCCATGGAACCCTAAATGTATGTGTTCCAGTGTAATGTTGCAATTCTTCCCGCGATACTAA CTCGGTCACTTTGCAGATTAGTACAGAGGACAGGCACCTCTCGAGGCAGACTATCCCCTATATGTAATTGTATTTGATACCTGAATCGTAAAGCACCGACTCGGACTTAGTTGGTACGGTCGGTTTTTTTCGACCATAGCATTAGGACTCCACTGGAGAGAGGCG GGCTTCGGTGTCGATTAAGCACTATCGTCGACCCGTATAAGGCATCTTCTGATCAAAGTTCTCGCGCTGTGATCCCTTTGAACTGCAAAAGAATGCTGTGCAAGAGATCGTCCATCTTTCGAATGGGGCGTACGTATAACCAGTCGGCCTGCTGAGTCGTCAATT CATGATTGACCCGGCTACCCCCCAGCAAGCAGAGTCTCGGAATTCTGCCTCCTGGCACGCAGGTGTACTGTTGTTGCGTCATGGTTCGATGGGGTACCGGCGTAGCAAGCAACACATCGAAACTGTTAGTAACGGAGGGTGGAATTCGACCGTCGACTTGAGCCT AGCGGGTGGGGGATCCTAAGCACTATCTCCCCGGATCGTTCGTAATGCGATCTATAGAGAGGTGTGCTAACATTTCTGTATCGACACGCCTATATCATATGTATGGTCGCCTGTCGCGGGCGGTAAATGTCCCTCAGCAAGGCAGCGGTACGCGGCTAAAATAGA CAACATCCCCAGAAGCGACATCTCGGATTAGTTCAGACTTTTCTGAAAGGACCGGGTGTCTCGACGGAGTACCTCGGGCTGTTACGGACTAAGGGACAGGTGATTGCCCTAAACGAGTGTACGCTAACCAAGAATGGATACGGTATGCATGGCGGCAGGTCTATA CCCGTTAAAGGTTTTATACAATATTACCCTTAAGCGTTACTGTACCCACCTGTAAAGCCTCGGCGGGATTATAGAAGGGGACAGGCGCCACTATCTCGGACAGCCAGATAGGTTTTCCGATGCCCCTTAACCGGTCTGAGACTCATTTTCTCGGATTGCACTACA CGTGCGTTGCCACCCGTCCATGTATCCGCGGGCAAAGCGTGCTATCAGCATCTAATTAAAGTGAACTATAATGAGGGGAAAAGTTCGGTACGCTGGGTGGTTCAGTGAAGCACTATCTAAAAGTCCTAGAAAACCCGCACAGGAAGGACGGCGTATGACCTTCTC TTCTCCCGCCAGATGCTAGAGTTAACCACTACGACAGCTTGAAGGTGAAACGATAAATAAGCACAGCCTCGGAGTACAATTGGTTTATATCTTGCTAACTTTGATAGATGATGCTACCGGTCCTTCCAGTCCTACAAAGCGACTGCTGCGAAGGGTGAGGCAGCT GTTGAGAAAACCTCACTCCGAGTCGTGAAGCACTGCGTCGGAGCCGTTGCGGTCTGAGGTGGAGGCAGTCAACAAGATGCTGCTTTCACTGTATTGGATCCCTTTGAAAACCACGCTGACACTGGAGTGCCAGGGATAGAATGGCAAAACAGGCACCGTACCGTG TCGGGAGTCTCCCCTACAACCAGGGGGCTTGTGTAAAGAGATTCCGTCTTGAATGTGCTTGCAGGGGTTAGTCGTGGTTGGGGACGAATGCGGGTCACTAGTCTCTCACGGATGAGCTAGGATTGGACTCTAAGCAGATTCTCGGACTGCGTATTAAAAGCGCTA GTACGTGAACAAACACAGTTTGTAGTCCGAGGGCATGAGTAGCACTATCTCGCTTCCAAAACGTTTGCGCATCATATTATAGGATACTCTCATGCACTGTCAGGTGATGCCTTACTGCATGTAACCGAAAATTACGCCGTTGGTAGACAGAGAGGGGTTAGATAC AGTGACGACTGAAGGGCAATAAACACAGGAAAGCACTATGCAGGACGTGGACTAGGAGCTTGGTCTCACCGATTTGTCTCTCTTCCCTGCTAATGCAGCGTTCCTGTCCACGACCACTAAATGGAGTAGTTGGTTGCTTAAACGAATTTGGTAACAGTATAGTGA GCCTATTAACGGCGCTGGTCACGATAGACCACTAGGCCAGCCGACCCACTAGCGTCGCATATCTAGAAGCGACATCTCGGAGGTTACTGCACAAGGATACCTCTCCTCCGGCCACTAACGGTCCGGGGCAGGCACACCGGGGCAACTTCCGTGCCCTCCCACATA""".split()
    # print(" ".join(RandomizedMotifSearch(Dna, k, t)))
    #
    motifs = ["GTC", "CCC", "ATA", "GCT"]
    profile = PseudoProfileMatrix(motifs)
    dna = ["ATGAGGTC", "GCCCTAGA", "AAATAGAT", "TTGTGCTA"]
    print(" ".join(fMotifs(profile, dna)))
