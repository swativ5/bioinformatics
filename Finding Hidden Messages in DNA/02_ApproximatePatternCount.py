'''
Computing Countd(Text, Pattern) simply requires us to compute the Hamming distance 
between Pattern and every k-mer substring of Text, which is achieved by the following pseudocode.

   ApproximatePatternCount(Text, Pattern, d)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            Pattern′ ← Text(i , |Pattern|)
           if HammingDistance(Pattern, Pattern′) ≤ d
                count ← count + 1
        return count

Code Challenge: Implement ApproximatePatternCount.

Input: Strings Pattern and Text as well as an integer d.
Output: Countd(Text, Pattern).
'''

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            count += 1
    return count

def HammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance


if __name__ == "__main__":
    Text = "AACAAGCTGATAAACATTTAAAGAG"
    Pattern = "AAAAA"
    d = 2
    print(ApproximatePatternCount(Pattern, Text, d))

    Pattern = "CAAAT"
    Text = "CAGTAGACGGCAAAAGAGTCAGTAGTATGACGCAAGGTGTATTTTGATTGCGCGGGGTAGAACTACTGCGGAGTATCTCGATGCCTGGGATTCAACAAGTGTAATGCGGAGAACTATATAGCAGACTGGCGGCTGGCGAAACTGAATACGCACTTGGTGGGCGCGTTCGCCTGGCAAATGCCTACGAAGTAACTTCAGTTATTCCAAATGATAAACTATTTAACGGATTCGGAGTAGAATTGCCTGTGATGCTTATCGATCGACGATTACTCATTGATGTACCATCAATACGCTTTATGCCTAGCCGCCTGTGGTGTGTCCGGACTAGATCTTGCGTGAGTTACTCTTCTTCACGGCG"
    d = 3
    print(ApproximatePatternCount(Pattern, Text, d))

    Pattern = "TGT"
    Text = "CGTGACAGTGTATGGGCATCTTT"
    d = 1
    print(ApproximatePatternCount(Pattern, Text, d))


