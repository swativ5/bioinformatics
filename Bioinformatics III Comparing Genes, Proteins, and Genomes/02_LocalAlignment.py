'''
Code Challenge: Solve the Local Alignment Problem.
    Input: Two protein strings written in the single-letter amino acid alphabet.
    Output: The maximum score of a local alignment of the strings, 
        followed by a local alignment of these strings achieving the maximum score. 
        Use the PAM250 scoring matrix for matches and mismatches 
        as well as the indel penalty σ = 5.

Sample Input:
MEANLY
PENALTY

Sample Output:
15
EANL-Y
ENALTY
'''

def read_pam250():
    pam250_str = open("Bioinformatics III Comparing Genes, Proteins, and Genomes/PAM250.txt").read().strip().split('\n')
    headers = pam250_str[0].split()
    pam250 = {}
    for line in pam250_str[1:]:
        values = line.split()
        amino_acid = values[0]
        scores = list(map(int, values[1:]))
        pam250[amino_acid] = {headers[i]: scores[i] for i in range(len(headers))}
    return pam250

def LocalAlignment(v, w, pam250, indel):
    n = len(v)
    m = len(w)

    scoring_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    max_score = 0
    max_pos = (0, 0)

    amino_acids = "   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y".replace(" ", "")
    aa_index = {aa: i for i, aa in enumerate(amino_acids)}
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_score = pam250[v[j - 1]][w[i - 1]]
            scoring_matrix[i][j] = max(
                0,
                scoring_matrix[i - 1][j] - indel,
                scoring_matrix[i][j - 1] - indel,
                scoring_matrix[i - 1][j - 1] + match_score
            )
            if scoring_matrix[i][j] > max_score:
                max_score = scoring_matrix[i][j]
                max_pos = (i, j)

    aligned_v, aligned_w = "", ""
    i, j = max_pos
    while scoring_matrix[i][j] != 0:
        current = scoring_matrix[i][j]
        if current == scoring_matrix[i - 1][j] - indel:
            aligned_v += '-'
            aligned_w += w[i - 1]
            i -= 1
        elif current == scoring_matrix[i][j - 1] - indel:
            aligned_v += v[j - 1]
            aligned_w += '-'
            j -= 1
        else:
            aligned_v += v[j - 1]
            aligned_w += w[i - 1]
            i -= 1
            j -= 1

    return max_score, aligned_v[::-1], aligned_w[::-1]

if __name__ == "__main__":
    # for i in range(1, 6):
    #     file_input = open(f"/home/swativ5/Downloads/LocalAlignment/inputs/test{i}.txt", "r")
    #     file_input_text = file_input.read()
    #     input_data = file_input_text.strip().split('\n')
    #     v = input_data[0]
    #     w = input_data[1]
    #     print(v, w)
        
    #     pam250 = read_pam250()
    #     indel = 5

    #     score, aligned_v, aligned_w = LocalAlignment(v, w, pam250, indel)
        
    #     file_output = open(f"/home/swativ5/Downloads/LocalAlignment/outputs/test{i}.txt", "r")
    #     file_output_text = file_output.read()
    #     expected_output = file_output_text.strip().split('\n')
    #     if expected_output[0] == str(score) and expected_output[1] == aligned_v and expected_output[2] == aligned_w:
    #         print("Correct")
    #     else:
    #         print("Wrong")
    #         print("Expected:", file_output_text.strip())
    #         print("Got:", str(score) + '\n' + aligned_v + '\n' + aligned_w)
    v = "MEANLY"
    w = "PENALTY"
    pam250 = read_pam250()
    indel = 5

    score, aligned_v, aligned_w = LocalAlignment(v, w, pam250, indel)
    print(score)
    print(aligned_v)
    print(aligned_w)

    