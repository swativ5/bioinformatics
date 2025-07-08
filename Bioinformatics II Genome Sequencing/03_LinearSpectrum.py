'''
LinearSpectrum(Peptide, Alphabet, AminoAcidMass)
    PrefixMass(0) ← 0
    for i ← 1 to |Peptide|
        for every symbol s in Alphabet
            if s = i-th amino acid in Peptide
                PrefixMass(i) ← PrefixMass(i − 1) + AminoAcidMass[s]
    LinearSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| − 1
        for j ← i + 1 to |Peptide|
            add PrefixMass(j) − PrefixMass(i) to LinearSpectrum
    return sorted list LinearSpectrum

Code Challenge: Implement LinearSpectrum.
    Input: An amino acid string Peptide.
    Output: The linear spectrum of Peptide.

Sample Input:
NQEL

Sample Output:
0 113 114 128 129 242 242 257 370 371 484
'''

def GenerateAminoAcidMass(text):
    AminoAcidMass = {}
    lines = text.strip().split("\n")
    for line in lines:
        amino_acid, mass = line.split()
        AminoAcidMass[amino_acid] = int(mass)
    Alphabet = list(AminoAcidMass.keys())
    return Alphabet, AminoAcidMass

def LinearSpectrum(Peptide, Alpahbet, AminoAcidMass):
    PrefixMass = [0] * (len(Peptide) + 1)
    for i in range(1, len(Peptide) + 1):
        PrefixMass[i] = PrefixMass[i - 1] + AminoAcidMass[Peptide[i - 1]]

    LinearSpectrumList = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrumList.append(PrefixMass[j] - PrefixMass[i])

    return sorted(LinearSpectrumList)

if __name__ == "__main__":
    f_amino = open("integer_mass_table.txt", "r")
    f_amino_text = f_amino.read()
    Alphabet, AminoAcidMass = GenerateAminoAcidMass(f_amino_text)

    file_input = open("/home/swativ5/Downloads/dataset_30248_2(1).txt", "r")
    file_input_text = file_input.read()
    Peptide = file_input_text.strip()
    spectrum = LinearSpectrum(Peptide, Alphabet, AminoAcidMass)    
    f = open("test.txt", "w")
    f.write(" ".join(map(str, spectrum)))
