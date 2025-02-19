'''
Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.

Input: A string Text, an integer k, and a 4 × k matrix Profile.
Output: A Profile-most probable k-mer in Text.
Code Challenge: Solve the Profile-most Probable k-mer Problem.

Sample Input:

ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2

Sample Output:

CCGAG
'''

def parsing_dataset(input_text):
    input_text = input_text.strip().split('\n')
    dna = input_text[0]
    k = int(input_text[1])
    profile = [list(map(float, i.split())) for i in input_text[2:]]
    return dna, k, profile

def ProfileMostProbableKmer(dna, k, profile):
    max_prob = -1
    most_probable_kmer = ''
    for i in range(len(dna) - k + 1):
        kmer = dna[i: i + k]
        prob = 1
        for j in range(k):
            if kmer[j] == 'A':
                prob *= profile[0][j]
            elif kmer[j] == 'C':
                prob *= profile[1][j]
            elif kmer[j] == 'G':
                prob *= profile[2][j]
            elif kmer[j] == 'T':
                prob *= profile[3][j]
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    return most_probable_kmer

if __name__ == '__main__':
    for i in range(3):
        file_input = open(f"ProfileMostProbableKmer/inputs/input_{i + 1}.txt")
        dna, k, profile = parsing_dataset(file_input.read())

        file_output = open(f"ProfileMostProbableKmer/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        if file_output_text == ProfileMostProbableKmer(dna, k, profile):
            print("yes")
        else:
            print("no", file_input, ProfileMostProbableKmer(dna, k, profile), file_output_text)
    file_input = '''AGGTATACCTAAAAGACTCCACTACATGTTTCATGGTATACCCGTAATAGCGCAAGTAGCATACAGTCTGAGACTTTCACCGTCCACCTATAAAAATTAGAGTTGGTACACGCTTTTGATGCGCGCATGCGCACGTTATATTCGCACAACTAGAGGGGAAGAAGTAGCGCTCCGCACCGTATCGTGTGACACCTCCCACAAGTAGTAAAGCGACTGCTACTACTTAGCTGTCCGCTCTCGTACCAAGAAACATCTCATAAGTTGATATACAGCAGGGCAGTACACGGCTTGTAACGCGACACTCCAACAGAGAGTCGAAAACAGGGGCGTTTTCTCTCTTCCCCATTCCGCGATCGCAAAGCTCGGAATCACCTAACAAAGCCCCTGCAGCTCCGAGAAAAATACAATTGTGATCCACCAGGCCAGGATAGCCCACAATGAAACTATTATACCTGCTACGTTGACCAGCGGATCAAAGTCTGCTAGCATGCCGCTTCGTTATCGCTCTTCCTTTAACTTTTGTCGTATCATTATCTCTGTGCAAACTAACAGTCAAGCGATCGTGAGCTCTAAATGGAGTCTCTAGCCCGCATGGTCCAAACCATTCGTTGAGACGGACGAATCCCGTATTCATGTCGACACGACTCTGTCGGTCCAATACGCCTATAACTGCTCTTAGGTTAGTAAAGAAGGGGTTGAGACAAACGATGGGGCGCCGCTACGGTCTGTTAGGGAATGTCCGAGGTACGAGGTCCGGCGCTCGAGCTAATACCAATCATTGCCGGCACTGCAGGCTACTTAGGATTGAGCGCATCATCAGCGGGTGATCTGTCGTTGGTCTTTTCGCAGAAGCGACATGCTTTTAGTGTCACCAGGAAATTAACCATCCTGGGTAGAACATGAGTTGACCGAGCTTTGTAATGTAGATTATTCCGCTAGCGCACCGATTGTTTGGGGCTCACGAAAGTGAAATATTCACAAATTCGATGCCCACAGCACC
12
0.289 0.301 0.217 0.193 0.229 0.277 0.277 0.181 0.229 0.361 0.181 0.301
0.157 0.217 0.277 0.373 0.205 0.217 0.241 0.241 0.253 0.205 0.229 0.205
0.289 0.289 0.241 0.193 0.265 0.217 0.229 0.241 0.313 0.241 0.337 0.313
0.265 0.193 0.265 0.241 0.301 0.289 0.253 0.337 0.205 0.193 0.253 0.181
'''
    dna, k, profile = parsing_dataset(file_input)
    print(ProfileMostProbableKmer(dna, k, profile))