'''
Exercise Break: How many subpeptides does a linear peptide of given length n have? (Include the empty peptide and the entire peptide.)
    Input: An integer n.
    Output: The number of subpeptides of a linear peptide of length n.

Sample Input:
4

Sample Output:
11

number of linear peptides:
n = 4
    len([1 + 1 + 1 + 1 + 2 + 2 + 2 + 3 + 3 + 4] + 1) = 11
    len((1 * 4) + (2 * 3) + (3 * 2) + (4 * 1)] + 1) = 11
    [4 + 3 + 2 + 1] + 1 = 10 + 1 = 11
n = n
    [n + (n - 1) + (n - 2) + ... + 1] + 1 = (n * (n + 1)) / 2 + 1
    
'''

def NumberofLinearPeptides(n):
    return (n * (n + 1)) // 2 + 1

if __name__ == "__main__":
    n = 17266
    print(NumberofLinearPeptides(n))