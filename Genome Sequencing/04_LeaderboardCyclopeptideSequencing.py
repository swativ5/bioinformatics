'''
Code Challenge: Implement LeaderboardCyclopeptideSequencing.
    Input: An integer N and a collection of integers Spectrum.
    Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).

Sample Input:
10
0 71 113 129 147 200 218 260 313 331 347 389 460

Sample Output:
113-147-71-129

LeaderboardCyclopeptideSequencing(Spectrum, N)
    Leaderboard ← set containing only the empty peptide
    LeaderPeptide ← empty peptide
    while Leaderboard is non-empty
        Leaderboard ← Expand(Leaderboard)
        for each Peptide in Leaderboard
            if Mass(Peptide) = ParentMass(Spectrum)
                if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
                    LeaderPeptide ← Peptide
            else if Mass(Peptide) > ParentMass(Spectrum)
                remove Peptide from Leaderboard
        Leaderboard ← Trim(Leaderboard, Spectrum, N)
    output LeaderPeptide
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

def modifiedScore(Peptide, Spectrum):
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

def modifiedTrim(Leaderboard, Spectrum, N):
    LinearScoresDictionary = dict()
    
    for Peptide in Leaderboard:
        LinearScoresDictionary[Peptide] = modifiedScore(Peptide, Spectrum)
    
    LeaderboardSorted = sorted(LinearScoresDictionary.items(), key = lambda a : a[1], reverse=True)
    Leaderboard = [p[0] for p in LeaderboardSorted]
    LinearScores = [p[1] for p in LeaderboardSorted]

    for j in range(N, len(Leaderboard)):
        if LinearScores[j] < LinearScores[N - 1]:
            return Leaderboard[:j]

    return Leaderboard

def LeaderboardCyclopeptideSequencing(Spectrum, N):
    Masses = list(set(AminoAcidMass.values()))

    SpectrumValues = list(map(int, Spectrum.strip().split()))
    ParentMass = max(SpectrumValues)

    Leaderboard = {""}
    LeaderPeptide = ""

    while len(Leaderboard) > 0:
        Leaderboard = Expand(Leaderboard, Masses)
        deletions = []
        for Peptide in Leaderboard:
            if Mass(Peptide) == ParentMass:
                if modifiedScore(Peptide, Spectrum) > modifiedScore(LeaderPeptide, Spectrum):
                    LeaderPeptide = Peptide
            elif Mass(Peptide) > ParentMass:
                deletions.append(Peptide)
        
        for deletion in deletions:
            Leaderboard.remove(deletion)

        Leaderboard = modifiedTrim(Leaderboard, Spectrum, N)
    
    return LeaderPeptide

if __name__ == "__main__":
    AminoAcidMass = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
        'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128,
        'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

    file_input = open("/home/swativ5/Downloads/dataset_30244_8.txt", "r")
    file_input_text = file_input.read()

    N, Spectrum = file_input_text.strip().split("\n")
    N = int(N)
    f = open("test.txt", "w")
    f.write(LeaderboardCyclopeptideSequencing(Spectrum, N))