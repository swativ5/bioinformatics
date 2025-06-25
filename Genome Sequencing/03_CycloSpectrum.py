'''
Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
    Input: An amino acid string Peptide.
    Output: Cyclospectrum(Peptide).

Code Challenge: Solve the Generating Theoretical Spectrum Problem.

Sample Input:
LEQN

Sample Output:
0 113 114 128 129 227 242 242 257 355 356 370 371 484

CyclicSpectrum(Peptide, Alphabet, AminoAcidMass)
    PrefixMass(0) ← 0
    for i ← 1 to |Peptide|
        for every symbol s in Alphabet
            if s = i-th amino acid in Peptide
                PrefixMass(i) ← PrefixMass(i − 1) + AminoAcidMass﻿[s]
    peptideMass ← PrefixMass(|Peptide|)
    CyclicSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| − 1
        for j ← i + 1 to |Peptide|
            add PrefixMass(j) − PrefixMass(i) to CyclicSpectrum
            if i > 0 and j < |Peptide|
                add peptideMass - (PrefixMass(j) − PrefixMass(i)) to CyclicSpectrum
    return sorted list CyclicSpectrum
'''

def GenerateAminoAcidMass(text):
    AminoAcidMass = {}
    lines = text.strip().split("\n")
    for line in lines:
        amino_acid, mass = line.split()
        AminoAcidMass[amino_acid] = int(mass)
    Alphabet = list(AminoAcidMass.keys())
    return Alphabet, AminoAcidMass

def CyclicSpectrum(Peptide, Alphabet, AminoAcidMass):
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

if __name__ == "__main__":
    f_amino = open("integer_mass_table.txt", "r")
    f_amino_text = f_amino.read()
    Alphabet, AminoAcidMass = GenerateAminoAcidMass(f_amino_text)

    file_input = open("/home/swativ5/Downloads/dataset_30215_4(1).txt", "r")
    file_input_text = file_input.read()
    Peptide = file_input_text.strip()
    spectrum = CyclicSpectrum(Peptide, Alphabet, AminoAcidMass)    
    f = open("test.txt", "w")
    f.write(" ".join(map(str, spectrum)))
