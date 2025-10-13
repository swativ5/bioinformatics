'''
Code Challenge: Use OutputLCS (reproduced below) to solve the Longest Common Subsequence Problem.
    Input: Two strings s and t.
    Output: A longest common subsequence of s and t. (Note: more than one solution may exist, in which case you may output any one.)

Sample Input:
AACCTTGG
ACACTGTGA

Sample Output:
AACTGG

OutputLCS(backtrack, v, i, j)
    if i = 0 or j = 0
        return ""
    if backtracki, j = "↓"
        return OutputLCS(backtrack, v, i - 1, j)
    else if backtracki, j = "→"
        return OutputLCS(backtrack, v, i, j - 1)
    else
        return OutputLCS(backtrack, v, i - 1, j - 1) + vi

LCSBackTrack(v, w)
    for i ← 0 to |v|
        si, 0 ← 0
    for j ← 0 to |w| 
        s0, j ← 0
    for i ← 1 to |v|
        for j ← 1 to |w|
            match ← 0
            if vi-1 = wj-1
                match ← 1
            si, j ← max{si-1, j , si,j-1 , si-1, j-1 + match }
            if si,j = si-1,j
                Backtracki, j ← "↓"
            else if si, j = si, j-1
                Backtracki, j ← "→"
            else if si, j = si-1, j-1 + match
                Backtracki, j ← "↘"
    return Backtrack

IterativeOutputLCS(Backtrack, v, w)
   LCS ← an empty string
    i ← length of string
    j ← length of string w
    while i > 0 and j > 0
        if Backtrack(i, j) = "↓"
            i ← i-1
        else if Backtrack(i,j) = "→"
            j ← j-1
        else if Backtrack(i,j) = "↘"
            LCS ← concatenate v[i] with LCS
            i ← i-1
            j ← j-1
    return LCS
'''

import sys

def LCSBackTrack(v, w):
    n = len(v)
    m = len(w)
    s = [[0] * (m + 1) for _ in range(n + 1)] 
    backtrack = [[0] * (m + 1) for _ in range(n + 1)] 

    for i in range(1, n + 1): 
        for j in range(1, m + 1):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + match)
            if s[i][j] == s[i - 1][j]:
                backtrack[i][j] = "↓"
            elif s[i][j] == s[i][j - 1]:
                backtrack[i][j] = "→"
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i][j] = "↘"
    return backtrack

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    
    if backtrack[i][j] == "↓":
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] == "→":
        return OutputLCS(backtrack, v, i, j - 1)
    else:
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i - 1]

def IterativeOutputLCS(backtrack, v, w):
    LCS = ""
    i = len(v)
    j = len(w)

    while(i > 0 and j > 0):
        if backtrack[i][j] == "↓":
            i -= 1
        elif backtrack[i][j] == "→":
            j -= 1
        elif backtrack[i][j] == "↘":
            LCS = v[i - 1] + LCS
            i -= 1
            j -= 1
    return LCS


if __name__ == "__main__":
    # file_input = open("/home/swativ5/Downloads/dataset_30197_5(1).txt", "r")
    # file_input_text = file_input.read()
    # s, t = file_input_text.strip().split('\n')
    s = "CTCGAT"
    t = "TACGTC"
    backtrack = LCSBackTrack(s, t)

    # sys.setrecursionlimit(10000)
    # result = OutputLCS(backtrack, s, len(s), len(t))

    result = IterativeOutputLCS(backtrack, s, t)
    f = open("test.txt", "w")
    f.write(str(result))
    f.close()
    print(result)


    s = "CTCGAT"
    t = "TACGTC"
    backtrack = LCSBackTrack(s, t)
    result = IterativeOutputLCS(backtrack, s, t)
    print(result)