"""Solve the Frequent Words Problem.
    Input: A string Text and an integer k.
    Output: All most frequent k-mers in Text.

BetterFrequentWords(Text, k)
    FrequentPatterns ← an array of strings of length 0
    freqMap ← FrequencyTable(Text, k)
    max ← MaxMap(freqMap)
    for all strings Pattern in freqMap
        if freqMap[pattern] = max
            append Pattern to frequentPatterns
    return frequentPatterns"""

def FrequentWords(Text, k):
    freqMap = dict()
    for i in range(0, len(Text) - k + 1):
        freqMap[Text[i: i + k]] = freqMap.get(Text[i: i + k], 0) + 1
    frequency = max(freqMap.values())
    maxfreq = [seq for seq, freq in freqMap.items() if freq == frequency]
    return maxfreq

if __name__ == "__main__":
    # for i in range(4):
    #     file_input = open(f"FrequentWords/inputs/input_{i + 1}.txt")
    #     file_input_text = file_input.readlines()
    #     Text, k = file_input_text[0].strip(), int(file_input_text[1].strip())
    #     file_output = open(f"FrequentWords/outputs/output_{i + 1}.txt")
    #     file_output_text = file_output.read().strip()
    #     print(FrequentWords(Text, k), file_output_text)
    Text = "CAGCAGTTCGAGAATCGCGAGAATCGACAAACACCGAGAATCGCAGCAGTTCGAGAATCGCAGCAGTTACAAACACCGAGAATCGACAAACACGACCCGGAGCTGCACTCAGCAGTTCGAGAATCGGCTGCACTCAGCAGTTCGAGAATCGGCTGCACTGACCCGGAACAAACACGACCCGGAGCTGCACTCAGCAGTTCAGCAGTTGACCCGGAGCTGCACTGCTGCACTACAAACACGACCCGGACAGCAGTTGACCCGGAGCTGCACTCAGCAGTTACAAACACGCTGCACTGACCCGGAGACCCGGAACAAACACGCTGCACTCAGCAGTTCGAGAATCGGCTGCACTACAAACACACAAACACCGAGAATCGGACCCGGAGACCCGGAACAAACACCGAGAATCGGACCCGGACAGCAGTTGCTGCACTGCTGCACTGCTGCACTCAGCAGTTCGAGAATCGACAAACACACAAACACACAAACACCGAGAATCGGCTGCACTACAAACACCAGCAGTTGCTGCACTACAAACACCAGCAGTTCAGCAGTTCAGCAGTTCAGCAGTTCGAGAATCGGCTGCACTCGAGAATCGACAAACACCAGCAGTTCGAGAATCGGACCCGGAGACCCGGAGACCCGGACAGCAGTTGACCCGGAACAAACACGACCCGGACAGCAGTTCAGCAGTTGCTGCACTCAGCAGTTACAAACACGCTGCACTGCTGCACTCGAGAATCGGACCCGGACGAGAATCGACAAACACGACCCGGAGACCCGGAGACCCGGAGCTGCACTCGAGAATCGGACCCGGACGAGAATCGCAGCAGTTGCTGCACTGCTGCACTGACCCGGAGACCCGGA"
    k = 14
    print(FrequentWords(Text, k))
    print(FrequentWords("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT", 3))