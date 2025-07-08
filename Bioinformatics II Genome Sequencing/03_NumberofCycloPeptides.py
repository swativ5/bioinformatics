'''
Exercise Break: How many subpeptides does a cyclic peptide of length n have?
    Input: An integer n.
    Output: The number of subpeptides of a cyclic peptide of length n.

Sample Input:
31315

Sample Output:
980597910


There are n starting positions (position 0 to n−1).
For each length k from 1 to n−1, there are exactly n subpeptides of that length in a cyclic peptide.
'''

def NumberofCycloPeptides(n):
    return n * (n - 1)

if __name__ == "__main__":
    n = 20626
    print(NumberofCycloPeptides(n))