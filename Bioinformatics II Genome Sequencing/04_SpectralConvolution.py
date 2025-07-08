'''
Spectral Convolution Problem: Compute the convolution of a spectrum.
    Input: A collection of integers Spectrum in increasing order.
    Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should appear exactly k times; you may return the elements in any order.

Sample Input:
0 137 186 323

Sample Output:
137 137 186 186 323 49
'''

def SpectralConvolution(Spectrum):
    Spectrum = list(map(int, Spectrum.strip().split()))
    ConvolutionList = []
    
    for i in range(len(Spectrum)):
        for j in range(i + 1, len(Spectrum)):
            difference = abs(Spectrum[j] - Spectrum[i])
            if difference != 0:
                ConvolutionList.append(difference)

    return " ".join(map(str, ConvolutionList))

if __name__ == "__main__":
    file_input = open("/home/swativ5/Downloads/dataset_30246_4(2).txt", "r")
    file_input_text = file_input.read()

    # file_input_text = "0 137 186 323"
    SpectralConvolutionList = SpectralConvolution(file_input_text)

    f = open("test.txt", "w")
    f.write(SpectralConvolutionList)

