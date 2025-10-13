'''
Edit Distance Problem: Find the edit distance between two strings.
    Input: Two strings.
    Output: The edit distance between these strings.

Code Challenge: Solve the Edit Distance Problem.

Sample Input:
GAGA
GAT

Sample Output:
2
'''

def EditDistance(v, w):
    n = len(v)
    m = len(w)

    scoring_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(n + 1):
        scoring_matrix[0][i] = i
    for j in range(m + 1):
        scoring_matrix[j][0] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if v[j - 1] == w[i - 1]:
                scoring_matrix[i][j] = scoring_matrix[i - 1][j - 1]
            else:
                scoring_matrix[i][j] = min(
                    scoring_matrix[i - 1][j] + 1,
                    scoring_matrix[i][j - 1] + 1,
                    scoring_matrix[i - 1][j - 1] + 1
                )

    return scoring_matrix[m][n]

if __name__ == "__main__":
    for i in range(1, 6):
        file_input_text = open(f"/home/swativ5/Downloads/EditDistance/inputs/input_{i}.txt").read().strip().split('\n')
        v = file_input_text[0].strip()
        w = file_input_text[1].strip()

        score = EditDistance(v, w)

        file_output_text = open(f"/home/swativ5/Downloads/EditDistance/outputs/output_{i}.txt").read().strip()

        if str(score) == file_output_text.strip():
            print(f"Correct")
        else:
            print(f"Wrong")
            print("Expected:", file_output_text.strip())
            print("Got:", str(score))


    file_input_text = open(f"/home/swativ5/Downloads/dataset_30200_3.txt").read().strip().split('\n')
    v = file_input_text[0].strip()
    w = file_input_text[1].strip()

    score = EditDistance(v, w)
    print(score)