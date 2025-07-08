'''
Protein Translation Problem: Translate an RNA string into an amino acid string.
    Input: An RNA string Pattern and the array GeneticCode.
    Output: The translation of Pattern into an amino acid string Peptide.

Code Challenge: Solve the Protein Translation Problem.

Sample Input:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output:
MAMAPRTEINSTRING
'''

def create_rna_table(input_text):
    rna_table = {}
    lines = input_text.strip().split('\n')
    for line in lines:
        parts = line.split()
        codon = parts[0]
        amino_acid = parts[1]
        rna_table[codon] = amino_acid
    return rna_table

def ProteinTranslation(rna_table, sequence):
    protein = ""
    for i in range(0, len(sequence) - 2, 3): 
        codon = sequence[i:i + 3]
        amino_acid = rna_table.get(codon, "")
        if amino_acid == "*":
            return protein
        protein += amino_acid
    return protein

if __name__ == "__main__":
    f_rna = open("RNA_codon_table_1.txt", "r")
    f_rna_text = f_rna.read()
    rna_table = create_rna_table(f_rna_text)

    file_input = open("/home/swativ5/Downloads/dataset_30213_4.txt", "r")
    file_input_text = file_input.read()
    protien = ProteinTranslation(rna_table, file_input_text)
    f = open("test.txt", "w")
    f.write(protien)