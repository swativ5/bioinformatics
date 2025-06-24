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
        AminoAcidMass[amino_acid] = mass
    Alphabet = list(AminoAcidMass.keys())
    return Alphabet, AminoAcidMass



if __name__ == "__main__":
    f_amino = open("integer_mass_table.txt", "r")
    f_amino_text = f_amino.read()
    print(GenerateAminoAcidMass(f_amino_text))