'''
Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
    Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
    Output: All substrings of Text encoding Peptide (if any such substrings exist).

Code Challenge: Solve the Peptide Encoding Problem. Click here for the RNA codon table corresponding to the array GeneticCode.

Sample Input:
ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
MA

Sample Output:
ATGGCC
GGCCAT
ATGGCC
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

def ReverseComplement(Pattern):
    Compliment = {"A":"T", "T":"A", "C":"G", "G":"C"};
    complement_list = [Compliment[c] for c in Pattern]
    reversed_compliment = "".join(complement_list[::-1])
    return reversed_compliment

def ProteinTranslation(rna_table, sequence):
    protein = ""
    for i in range(0, len(sequence) - 2, 3): 
        codon = sequence[i:i + 3]
        amino_acid = rna_table.get(codon, "")
        if amino_acid == "*":
            return protein
        protein += amino_acid
    return protein

def PeptideEncoding(Text, Peptide, RNATable):
    k = len(Peptide) * 3
    substrings = []

    for strand in [Text, ReverseComplement(Text)]:
        for i in range(len(strand) - k + 1):
            dna = strand[i : i + k]
            rna = dna.replace("T", "U")
            if ProteinTranslation(RNATable, rna) == Peptide:
                if strand == Text:
                    substrings.append(dna)
                else:
                    substrings.append(ReverseComplement(dna))

    return substrings

if __name__ == "__main__":
    f_rna = open("RNA_codon_table_1.txt", "r")
    f_rna_text = f_rna.read()
    rna_table = create_rna_table(f_rna_text)

    file_input = open("/home/swativ5/Downloads/dataset_30213_7.txt", "r")
    file_input_text = file_input.read()
    Text, Peptide = file_input_text.strip().split("\n")
    substrings = PeptideEncoding(Text, Peptide, rna_table)
    f = open("test.txt", "w")
    f.write("\n".join(substrings))