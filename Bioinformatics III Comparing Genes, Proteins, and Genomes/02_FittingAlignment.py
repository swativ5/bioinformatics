'''
Code Challenge: Solve the Fitting Alignment Problem.
    Input: Two amino acid strings.
    Output: A highest-scoring fitting alignment between v and w. Use the BLOSUM62 scoring table and an indel penalty equal to 1.


Sample Input:
DISCREPANTLY
PATENT

Sample Output:
20
PA--NT
PATENT
'''

def Blosum62():
    file_text = open("Bioinformatics III Comparing Genes, Proteins, and Genomes/BLOSUM62.txt", "r").read().strip().split('\n')
    headers = file_text[0].split()
    blosum62 = {}
    for line in file_text[1:]:
        values = line.split()
        amino_acid = values[0]
        scores = list(map(int, values[1:]))
        blosum62[amino_acid] = {headers[i]: scores[i] for i in range(len(headers))}
    return blosum62

def FittingAlignment(v, w, scoring_matrix, indel_penalty):
    n = len(v)
    m = len(w)

    scoring = [[0] * (n + 1) for _ in range(m + 1)]
    backtrack = [[0] * (n + 1) for _ in range(m + 1)]

    # for i in range(1, m + 1):
    #     scoring[i][0] = 0
    # for j in range(1, n + 1):
    #     scoring[0][j] = scoring[0][j - 1] - indel_penalty

    max_score = float('-inf')
    max_i = 0
    max_j = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = scoring[i - 1][j - 1] + scoring_matrix[w[i - 1]][v[j - 1]] if v[j - 1] == w[i - 1] else scoring[i - 1][j - 1] - indel_penalty
            delete = scoring[i - 1][j] - indel_penalty
            insert = scoring[i][j - 1] - indel_penalty
            scoring[i][j] = max(match, delete, insert)

            if scoring[i][j] == match:
                backtrack[i][j] = 'D' 
            elif scoring[i][j] == delete:
                backtrack[i][j] = 'U'
            else:
                backtrack[i][j] = 'L'

            if i == m and scoring[i][j] > max_score:
                max_score = scoring[i][j]
                max_i = i
                max_j = j

    aligned_v = []
    aligned_w = []
    i, j = max_i, max_j

    while i > 0 and j > 0:
        if backtrack[i][j] == 'D':
            aligned_v.append(v[j - 1])
            aligned_w.append(w[i - 1])
            i -= 1
            j -= 1
        elif backtrack[i][j] == 'U':
            aligned_v.append('-')
            aligned_w.append(w[i - 1])
            i -= 1
        else:  # 'L'
            aligned_v.append(v[j - 1])
            aligned_w.append('-')
            j -= 1

    # while j > 0:
    #     aligned_v.append(v[j - 1])
    #     aligned_w.append('-')
    #     j -= 1

    aligned_v.reverse()
    aligned_w.reverse()

    return max_score, ''.join(aligned_v).strip(), ''.join(aligned_w).strip()

if __name__ == "__main__":
    for i in range(1, 5):
        file_input_text = open(f"/home/swativ5/Downloads/FittingAlignment/inputs/input_{i}.txt").read().strip().split('\n')
        v = file_input_text[0].strip()
        w = file_input_text[1].strip()

        scoring_matrix = Blosum62()
        indel_penalty = 1

        score, aligned_v, aligned_w = FittingAlignment(v, w, scoring_matrix, indel_penalty)

        file_output_text = open(f"/home/swativ5/Downloads/FittingAlignment/outputs/output_{i}.txt").read().strip().split('\n')
        expected_score = int(file_output_text[0].strip())
        expected_aligned_v = file_output_text[1].strip()
        expected_aligned_w = file_output_text[2].strip()

        if score == expected_score and aligned_v == expected_aligned_v and aligned_w == expected_aligned_w:
            print(f"Correct")
        else:
            print(f"Wrong")
            print("Expected:", expected_score, expected_aligned_v, expected_aligned_w)
            print("Got:", score, aligned_v, aligned_w)