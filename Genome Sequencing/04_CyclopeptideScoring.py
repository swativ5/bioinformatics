'''
Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.
    Input: An amino acid string Peptide and a collection of integers Spectrum.
    Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).

Code Challenge: Solve the Cyclopeptide Scoring Problem.

Sample Input:
NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484

Sample Output:
11
'''

def CyclicSpectrum(Peptide):
    PrefixMass = [0] * (len(Peptide) + 1)
    for i in range(1, len(Peptide) + 1):
        PrefixMass[i] = PrefixMass[i - 1] + AminoAcidMass[Peptide[i - 1]]

    peptideMass = PrefixMass[len(Peptide)]
    CyclicSpectrumList = [0]

    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            CyclicSpectrumList.append(PrefixMass[j] - PrefixMass[i])
            if i > 0 and j < len(Peptide):
                CyclicSpectrumList.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))

    return sorted(CyclicSpectrumList)

def Score(Peptide, Spectrum):
    SpectrumValues = list(map(int, Spectrum.strip().split()))
    SpectrumDictionary = {}
    for mass in SpectrumValues:
        SpectrumDictionary[mass] = SpectrumDictionary.get(mass, 0) + 1

    PeptideDictionary = {}
    for mass in CyclicSpectrum(Peptide):
        PeptideDictionary[mass] = PeptideDictionary.get(mass, 0) + 1
    
    score = 0
    for mass in PeptideDictionary:
        score += min(PeptideDictionary[mass], SpectrumDictionary.get(mass, 0))

    return score

if __name__ == "__main__":
    AminoAcidMass = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
        'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128,
        'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

    file_input = open("/home/swativ5/Downloads/dataset_30244_3.txt", "r")
    file_input_text = file_input.read()
    Peptide, Spectrum = file_input_text.strip().split("\n")
    # Peptide = "NQEL"
    # Spectrum = "0 99 113 114 128 227 257 299 355 356 370 371 484"
    score = Score(Peptide, Spectrum)
    f = open("test.txt", "w")
    f.write(str(score))
