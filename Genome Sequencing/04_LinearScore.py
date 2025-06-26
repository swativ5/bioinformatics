'''
 Code Challenge: Compute the score of a linear peptide with respect to a spectrum.
    Input: An amino acid string Peptide and a collection of integers Spectrum.
    Output: The linear score of Peptide with respect to Spectrum, LinearScore(Peptide, Spectrum).

Sample Input:
NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484

Sample Output:
8
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

if __name__ == "__main__":
    AminoAcidMass = {
        'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
        'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128,
        'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
    }

    file_input = open("/home/swativ5/Downloads/dataset_30249_1.txt", "r")
    file_input_text = file_input.read()
    Peptide, Spectrum = file_input_text.strip().split("\n")
    # Peptide = "NQEL"
    # Spectrum = "0 99 113 114 128 227 257 299 355 356 370 371 484"
    score = Score(Peptide, Spectrum)
    f = open("test.txt", "w")
    f.write(str(score))
