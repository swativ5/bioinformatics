"""Code Challenge: Solve the Pattern Matching Problem.

Input: Two strings, Pattern and Genome.
Output: A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome."""
def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(0, len(Genome) - len(Pattern) + 1):
        if Genome[i : i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions

if __name__ == "__main__":
    # for i in range(5):
    #     file_input = open(f"PatternMatching/inputs/input_{i + 1}.txt")
    #     file_input_text = file_input.readlines()
    #     Pattern, Genome = file_input_text[0].strip(), file_input_text[1].strip()
    #     file_output = open(f"PatternMatching/outputs/output_{i + 1}.txt")
    #     file_output_text = file_output.read().strip()
    #     print(PatternMatching(Pattern, Genome), file_output_text)

    Pattern = "AA"
    Genome = "AAACATAGGATCAAC"
    positions = PatternMatching(Pattern, Genome)
    for i in positions:
        print(i, end=" ")
