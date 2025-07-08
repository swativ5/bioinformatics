'''Code Challenge: Implement StringSpelledByGappedPatterns.
    Input: Integers k and d followed by a sequence of (k, d)-mers (a1|b1), … , (an|bn) such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for 1 ≤ i ≤ n-1.
    Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer in Text is equal to (ai|bi)  for 1 ≤ i ≤ n (if such a string exists).

Sample Input:
4 2
GACC|GCGC ACCG|CGCC CCGA|GCCG CGAG|CCGG GAGC|CGGA

Sample Output:
GACCGAGCGCCGGA

StringSpelledByGappedPatterns(GappedPatterns, k, d)
    FirstPatterns ← the sequence of initial k-mers from GappedPatterns
    SecondPatterns ← the sequence of terminal k-mers from GappedPatterns
    PrefixString ← StringSpelledByPatterns(FirstPatterns, k)
    SuffixString ← StringSpelledByPatterns(SecondPatterns, k)
    for i = k + d + 1 to |PrefixString|
        if the i-th symbol in PrefixString does not equal the (i - k - d)-th symbol in SuffixString
            return "there is no string spelled by the gapped patterns"
    return PrefixString concatenated with the last k + d symbols of SuffixString
'''

def preprocessing(input_string):
    first_line, second_line = input_string.strip().split("\n")
    k, d = map(int, first_line.strip().split(" "))
    Patterns = second_line.strip().split(" ")
    
    FirstPatterns, SecondPatterns = [], []
    for pattern in Patterns:
        fpattern, spattern = pattern.strip().split("|")
        FirstPatterns.append(fpattern)
        SecondPatterns.append(spattern)
    
    GappedPatterns = [FirstPatterns, SecondPatterns]
    return k, d, GappedPatterns

def StringSpelledByPatterns(patterns):
    return patterns[0] + ''.join(p[-1] for p in patterns[1:])

def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    FirstPatterns, SecondPatterns = GappedPatterns[0], GappedPatterns[1]
    PrefixString = StringSpelledByPatterns(FirstPatterns)
    SuffixString = StringSpelledByPatterns(SecondPatterns)

    for i in range(k + d, len(PrefixString)):
        if PrefixString[i] != SuffixString[i - k - d]:
            return "there is no string spelled by the gapped patterns"
    return PrefixString + SuffixString[-(k + d):]


if __name__ == "__main__":
    for i in range(4):
        file_input = open(f"GappedGenomePath/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        k, d, GappedPatterns = preprocessing(file_input_text)

        file_output = open(f"GappedGenomePath/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        f_output = StringSpelledByGappedPatterns(GappedPatterns, k, d)

        if file_output_text == f_output:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(file_output_text, "\n", f_output)

    file_input = open(f"/home/swativ5/Downloads/dataset_30208_4.txt")
    file_input_text = file_input.read()
    k, d, GappedPatterns = preprocessing(file_input_text)
    f_output = StringSpelledByGappedPatterns(GappedPatterns, k, d)
    f = open("test.txt", "w")
    f.write(f_output)
