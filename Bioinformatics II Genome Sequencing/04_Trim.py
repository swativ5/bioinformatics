'''
Code Challenge: Implement Trim (reproduced below).
    Input: A collection of peptides Leaderboard, a collection of integers Spectrum, and an integer N.
    Output: The N highest-scoring linear peptides on Leaderboard with respect to Spectrum.

Trim(Leaderboard, Spectrum, N, Alphabet, AminoAcidMass)
    for j ← 1 to |Leaderboard|
        Peptide ← j-th peptide in Leaderboard
        LinearScores(j) ← LinearScore(Peptide, ﻿Alphabet, AminoAcidMass, Spectrum)
    sort Leaderboard according to the decreasing order of scores in LinearScores
    sort LinearScores in decreasing order
    for j ← N + 1 to |Leaderboard|
        if LinearScores(j) < LinearScores(N)
            remove all peptides starting from the j-th peptide from Leaderboard
            return Leaderboard
    return Leaderboard

Sample Input:
LAST ALST TLLT TQAS
0 71 87 101 113 158 184 188 259 271 372
2

Sample Output:
LAST ALST
'''
def LinearSpectrum(Peptide):
    PrefixMass = [0] * (len(Peptide) + 1)
    for i in range(1, len(Peptide) + 1):
        PrefixMass[i] = PrefixMass[i - 1] + AminoAcidMass[Peptide[i - 1]]

    LinearSpectrumList = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrumList.append(PrefixMass[j] - PrefixMass[i])

    return sorted(LinearSpectrumList)


def Score(Peptide, Spectrum):
    SpectrumValues = list(map(int, Spectrum.strip().split()))
    SpectrumDictionary = {}
    for mass in SpectrumValues:
        SpectrumDictionary[mass] = SpectrumDictionary.get(mass, 0) + 1

    PeptideDictionary = {}
    for mass in LinearSpectrum(Peptide):
        PeptideDictionary[mass] = PeptideDictionary.get(mass, 0) + 1
    
    score = 0
    for mass in PeptideDictionary:
        score += min(PeptideDictionary[mass], SpectrumDictionary.get(mass, 0))

    return score

def Trim(Leaderboard, Spectrum, N):
    LinearScoresDictionary = dict()
    
    for j in range(0, len(Leaderboard)):
        Peptide = Leaderboard[j]
        LinearScoresDictionary[Peptide] = Score(Peptide, Spectrum)
    
    LeaderboardSorted = sorted(LinearScoresDictionary.items(), key = lambda a : a[1], reverse=True)
    Leaderboard = [p[0] for p in LeaderboardSorted]
    LinearScores = [p[1] for p in LeaderboardSorted]

    for j in range(N, len(Leaderboard)):
        if LinearScores[j] < LinearScores[N - 1]:
            return Leaderboard[:j]

    return Leaderboard


if __name__ == "__main__":
    AminoAcidMass = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
        'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128,
        'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

    file_input = open("/home/swativ5/Downloads/dataset_30249_3.txt", "r")
    file_input_text = file_input.read()

    Peptides, Spectrum, N = file_input_text.strip().split("\n")
    Leaderboard = Peptides.split()
    N = int(N)
    Leaderboard = Trim(Leaderboard, Spectrum, N)
    f = open("test.txt", "w")
    f.write(" ".join(Leaderboard))