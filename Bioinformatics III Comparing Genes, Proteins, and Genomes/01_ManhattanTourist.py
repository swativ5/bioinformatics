'''
Code Challenge: Find the length of a longest path in the Manhattan Tourist Problem.
    Input: Integers n and m, followed by an n × (m + 1) matrix Down and an (n + 1) × m matrix Right. The two matrices are separated by the "-" symbol.
    Output: The length of a longest path from source (0, 0) to sink (n, m) in the rectangular grid whose edges are defined by the matrices Down and Right.


Sample Input:
4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2

Sample Output:
34

ManhattanTourist(n, m, Down, Right)
    s0, 0 ← 0
    for i ← 1 to n
        si, 0 ← si-1, 0 + downi-1, 0
    for j ← 1 to m
        s0, j ← s0, j−1 + right0, j-1
    for i ← 1 to n
        for j ← 1 to m
            si, j ← max{si - 1, j + downi-1, j, si, j - 1 + righti, j-1}
    return sn, m
'''
def ManhattanTourist(n, m, Down, Right):
    s = [[0] * (m + 1) for _ in range(n + 1)]  

    for i in range(1, n + 1): 
        s[i][0] = s[i - 1][0] + Down[i - 1][0]
    
    for j in range(1, m + 1):  
        s[0][j] = s[0][j - 1] + Right[0][j - 1]
    
    for i in range(1, n + 1): 
        for j in range(1, m + 1):  
            s[i][j] = max(s[i - 1][j] + Down[i - 1][j], s[i][j - 1] + Right[i][j - 1])
    
    return s[n][m]
if __name__ == "__main__":
    file_input = open("/home/swativ5/Downloads/dataset_30205_10.txt", "r")
    file_input_text = file_input.read()
#     file_input_text = '''4 4
# 1 0 2 4 3
# 4 6 5 2 1
# 4 4 5 2 1
# 5 6 8 5 3
# -
# 3 2 4 0
# 3 2 4 2
# 0 7 3 3
# 3 3 0 2
# 1 3 2 2'''

    lines = file_input_text.strip().split("\n")
    n, m = map(int, lines[0].split())
    
    separator_index = lines.index("-")
    
    Down = []
    for i in range(1, separator_index):
        Down.append(list(map(int, lines[i].split())))
    
    Right = []
    for i in range(separator_index + 1, len(lines)):
        Right.append(list(map(int, lines[i].split())))
    
    result = ManhattanTourist(n, m, Down, Right)
    f = open("test.txt", "w")
    f.write(str(result))
    f.close()