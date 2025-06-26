'''
Code Challenge: Implement ConvolutionCyclopeptideSequencing.
    Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
    Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).

Sample Input:
20
60
57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493

Sample Output:
99-71-137-57-72-57
'''

def Expand(CandidatePeptide, Masses):
    ExpandedPeptides = set()

    for peptide in CandidatePeptide:
        for mass in Masses:
            if peptide == "":
                ExpandedPeptides.add(str(mass))
            else:
                ExpandedPeptides.add(peptide + "-" + str(mass))

    return ExpandedPeptides

def Mass(Peptide):
    mass = 0
    for peptidemass in Peptide.strip().split("-"):
        mass += int(peptidemass)
    return mass

def modifiedLinearSpectrum(Peptide):
    PrefixMass = [0] * (len(Peptide) + 1)
    for i in range(1, len(Peptide) + 1):
        PrefixMass[i] = PrefixMass[i - 1] + Peptide[i - 1]

    LinearSpectrumList = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrumList.append(PrefixMass[j] - PrefixMass[i])

    return sorted(LinearSpectrumList)

def modifiedLinearScore(Peptide, Spectrum):
    if len(Peptide) == 0:
        return 0
    SpectrumValues = list(map(int, Spectrum.strip().split()))
    SpectrumDictionary = {}
    for mass in SpectrumValues:
        SpectrumDictionary[mass] = SpectrumDictionary.get(mass, 0) + 1

    PeptideDictionary = {}
    PeptideList = [int(peptide) for peptide in Peptide.split("-")]
    for mass in modifiedLinearSpectrum(PeptideList):
        PeptideDictionary[mass] = PeptideDictionary.get(mass, 0) + 1
    
    score = 0
    for mass in PeptideDictionary:
        score += min(PeptideDictionary[mass], SpectrumDictionary.get(mass, 0))

    return score

def modifiedCyclicSpectrum(Peptide):
    PrefixMass = [0] * (len(Peptide) + 1)
    for i in range(1, len(Peptide) + 1):
        PrefixMass[i] = PrefixMass[i - 1] + Peptide[i - 1]

    peptideMass = PrefixMass[len(Peptide)]
    CyclicSpectrumList = [0]

    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            CyclicSpectrumList.append(PrefixMass[j] - PrefixMass[i])
            if i > 0 and j < len(Peptide):
                CyclicSpectrumList.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))

    return sorted(CyclicSpectrumList)

def modifiedCyclicScore(Peptide, Spectrum):
    if len(Peptide) == 0:
        return 0
    
    SpectrumValues = list(map(int, Spectrum.strip().split()))
    SpectrumDictionary = {}
    for mass in SpectrumValues:
        SpectrumDictionary[mass] = SpectrumDictionary.get(mass, 0) + 1

    PeptideDictionary = {}
    PeptideList = [int(peptide) for peptide in Peptide.split("-")]
    for mass in modifiedCyclicSpectrum(PeptideList):
        PeptideDictionary[mass] = PeptideDictionary.get(mass, 0) + 1
    
    score = 0
    for mass in PeptideDictionary:
        score += min(PeptideDictionary[mass], SpectrumDictionary.get(mass, 0))

    return score

def modifiedTrim(Leaderboard, Spectrum, N):
    LinearScoresDictionary = dict()
    
    for Peptide in Leaderboard:
        LinearScoresDictionary[Peptide] = modifiedLinearScore(Peptide, Spectrum)
    
    LeaderboardSorted = sorted(LinearScoresDictionary.items(), key = lambda a : a[1], reverse=True)
    Leaderboard = [p[0] for p in LeaderboardSorted]
    LinearScores = [p[1] for p in LeaderboardSorted]

    for j in range(N, len(Leaderboard)):
        if LinearScores[j] < LinearScores[N - 1]:
            return Leaderboard[:j]

    return Leaderboard

def modifiedSpectralConvolution(Spectrum, M):
    Spectrum = list(map(int, Spectrum.strip().split()))
    ConvolutionList = []
    ConvolutionDict = dict()

    for i in range(len(Spectrum)):
        for j in range(i + 1, len(Spectrum)):
            difference = abs(Spectrum[j] - Spectrum[i])
            if 57 <= difference <= 200:
                ConvolutionList.append(difference)
                ConvolutionDict[difference] = ConvolutionDict.get(difference, 0) + 1
    
    ConvolutionSorted = sorted(ConvolutionDict.items(), key=lambda a: a[1], reverse=True)
    MassList = [item[0] for item in ConvolutionSorted]
    FreqList = [item[1] for item in ConvolutionSorted]

    for j in range(M, len(MassList)):
        if FreqList[j] < FreqList[M - 1]:
            return MassList[:j]

    return MassList

def ConvolutionCyclopeptideSequencing(M, N, Spectrum):
    # Masses = list(set(AminoAcidMass.values()))
    Masses = modifiedSpectralConvolution(Spectrum, M)

    SpectrumValues = list(map(int, Spectrum.strip().split()))
    ParentMass = max(SpectrumValues)

    Leaderboard = {""}
    LeaderPeptide = [""]
    BestScore = 0

    while len(Leaderboard) > 0:
        Leaderboard = Expand(Leaderboard, Masses)
        deletions = []
        for Peptide in Leaderboard:
            if Mass(Peptide) == ParentMass:
                CurrentScore = modifiedCyclicScore(Peptide, Spectrum)
                if CurrentScore > BestScore:
                    LeaderPeptide = [Peptide]
                    BestScore = CurrentScore
                elif CurrentScore == BestScore:
                    LeaderPeptide.append(Peptide)
            elif Mass(Peptide) > ParentMass:
                deletions.append(Peptide)
        
        for deletion in deletions:
            Leaderboard.remove(deletion)

        Leaderboard = modifiedTrim(Leaderboard, Spectrum, N)
    print(BestScore)
    return LeaderPeptide


if __name__ == "__main__":
    file_input = open("/home/swativ5/Downloads/dataset_30246_8.txt", "r")
    file_input_text = file_input.read()

#     file_input_text = """20
# 60
# 57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493
# """

    M, N, Spectrum = file_input_text.strip().split("\n")
    M, N = int(M), int(N)
    f = open("test.txt", "w")
    LeaderPeptide = ConvolutionCyclopeptideSequencing(M, N, Spectrum)
    f.write(" ".join(LeaderPeptide))