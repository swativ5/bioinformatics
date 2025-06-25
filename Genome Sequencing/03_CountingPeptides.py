'''
Counting Peptides with Given Mass Problem: Compute the number of peptides of given mass.
    Input: An integer m.
    Output: The number of linear peptides having integer mass m.

Sample Input:
1024

Sample Output:
14712706211
'''
import math

def GenerateAminoAcidMass(text):
    AminoAcidMass = {}
    lines = text.strip().split("\n")
    for line in lines:
        amino_acid, mass = line.split()
        AminoAcidMass[amino_acid] = int(mass)
    Alphabet = list(AminoAcidMass.keys())
    return Alphabet, AminoAcidMass

def CountingPeptides(m, AminoAcidMass):
    Mass = list(set(AminoAcidMass.values()))
    table = [0] * (m + 1)
    table[0] = 1

    for mass in range(1, m + 1):
        for aminoacidmass in Mass:
            if mass - aminoacidmass >= 0:
                table[mass] += table[mass - aminoacidmass]
    
    return table[m]

if __name__ == "__main__":
    f_amino = open("integer_mass_table.txt", "r")
    f_amino_text = f_amino.read()
    Alphabet, AminoAcidMass = GenerateAminoAcidMass(f_amino_text)

    file_input = open("/home/swativ5/Downloads/dataset_30216_2.txt", "r")
    file_input_text = file_input.read()
    m = int(file_input_text.strip())
    spectrum = CountingPeptides(m, AminoAcidMass)

    f = open("test.txt", "w")
    f.write(str(spectrum))

    a1 = CountingPeptides(5000, AminoAcidMass)
    a2 = CountingPeptides(5001, AminoAcidMass)
    c = 2**(math.log2(a2) - math.log2(a1))
    print(c)