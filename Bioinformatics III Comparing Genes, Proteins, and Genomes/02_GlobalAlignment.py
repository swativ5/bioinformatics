'''
Code Challenge: Solve the Global Alignment Problem.
    Input: A match reward, a mismatch penalty, an indel penalty, 
        and two nucleotide strings.
    Output: The maximum alignment score of these strings followed by an 
        alignment achieving this maximum score.

Sample Input:
1 1 2
GAGA
GAT

Sample Output:
-1
GAGA
GA-T
'''

def GlobalAlignment(v, w, match, mismatch, indel):
    n = len(v)
    m = len(w)

    scoring_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        scoring_matrix[i][0] = -i * indel
    for j in range(1, n + 1):
        scoring_matrix[0][j] = -j * indel

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w[i - 1] == v[j - 1]:
                score = match
            else:
                score = -mismatch
            scoring_matrix[i][j] = max(
                scoring_matrix[i - 1][j] - indel,
                scoring_matrix[i][j - 1] - indel,
                scoring_matrix[i - 1][j - 1] + score
            )

    aligned_v, aligned_w = "", ""
    i, j = m, n
    while i > 0 or j > 0:
        current = scoring_matrix[i][j]
        if i > 0 and current == scoring_matrix[i - 1][j] - indel:
            aligned_v += '-'
            aligned_w += w[i - 1]
            i -= 1
        elif j > 0 and current == scoring_matrix[i][j - 1] - indel:
            aligned_v += v[j - 1]
            aligned_w += '-'
            j -= 1
        else:
            aligned_v += v[j - 1]
            aligned_w += w[i - 1]
            i -= 1
            j -= 1

    aligned_v = aligned_v[::-1]
    aligned_w = aligned_w[::-1]
    return scoring_matrix[m][n], aligned_v, aligned_w

if __name__ == "__main__":
    for i in range(1, 8):
        file_input = open(f"/home/swativ5/Downloads/GlobalAlignment/inputs/input_{i}.txt", "r")
        file_input_text = file_input.read()
        input_data = file_input_text.strip().split('\n')
        match, mismatch, indel = map(int, input_data[0].split())
        v = input_data[1]
        w = input_data[2]
        result = GlobalAlignment(v, w, match, mismatch, indel)
        f = open(f"/home/swativ5/Downloads/GlobalAlignment/outputs/output_{i}.txt", "r")
        if f.read().strip() == str(result[0]) + '\n' + result[1] + '\n' + result[2]:
            print("Correct")
        else:
            print("Wrong")
            print("Expected:", f.read().strip())
            print("Got:", str(result[0]) + '\n' + result[1] + '\n' + result[2])
        
        file_input = open(f"/home/swativ5/Downloads/dataset_30199_3.txt", "r")
        file_input_text = file_input.read()
        input_data = file_input_text.strip().split('\n')
        match, mismatch, indel = map(int, input_data[0].split())
        v = input_data[1]
        w = input_data[2]
        result = GlobalAlignment(v, w, match, mismatch, indel)
        f = open("test.txt", "w")
        f.write(str(result[0]) + '\n' + result[1] + '\n' + result[2])
        f.close()