'''
Code Challenge: Solve the String Spelled by a Genome Path Problem.

Sample Input:
ACCGA CCGAA CGAAG GAAGC AAGCT

Sample Output:
ACCGAAGCT
'''

def GenomePath(kmers):
    sequence = kmers[0]
    for i in range(1, len(kmers)):
        sequence += kmers[i][-1]
    return sequence


if __name__ == "__main__":
    for i in range(4):
        file_input = open(f"GenomePath/inputs/input_{i + 1}.txt")
        file_input_text = file_input.readlines()
        kmers = file_input_text[0].strip().split()

        file_output = open(f"GenomePath/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        sequence = GenomePath(kmers)
        if file_output_text == sequence:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(sequence, file_output_text)

    file_input = open(f"/home/swativ5/Downloads/dataset_30182_3.txt")
    file_input_text = file_input.readlines()
    kmers = file_input_text[0].strip().split()
    print(GenomePath(kmers))
