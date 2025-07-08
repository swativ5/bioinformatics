'''
Code Challenge: Implement CyclopeptideSequencing (pseudocode reproduced below).

CyclopeptideSequencing(Spectrum)
    CandidatePeptides ← a set containing only the empty peptide FinalPeptides ← empty list of strings
    while CandidatePeptides is nonempty
        CandidatePeptides ← Expand(CandidatePeptides)
        for each peptide Peptide in CandidatePeptides
            if Mass(Peptide) = ParentMass(Spectrum)
                if Cyclospectrum(Peptide) = Spectrum and Peptide is not in FinalPeptides
                    append Peptide to FinalPeptides
                remove Peptide from CandidatePeptides
            else if Peptide is not consistent with Spectrum
                remove Peptide from CandidatePeptides
    return FinalPeptides

Sample Input:
0 113 128 186 241 299 314 427

Sample Output:
186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
'''

def GenerateAminoAcidMass(text):
    AminoAcidMass = {}
    lines = text.strip().split("\n")
    for line in lines:
        amino_acid, mass = line.split()
        AminoAcidMass[amino_acid] = int(mass)
    Alphabet = list(AminoAcidMass.keys())
    return Alphabet, AminoAcidMass

def Expand(CandidatePeptide, Masses):
    ExpandedPeptides = set()

    for peptide in CandidatePeptide:
        for mass in Masses:
            if peptide == "":
                ExpandedPeptides.add(str(mass))
            else:
                ExpandedPeptides.add(peptide + "-" + str(mass))

    return ExpandedPeptides

def Mass(Peptide):
    mass = 0
    for peptidemass in Peptide.strip().split("-"):
        mass += int(peptidemass)
    return mass

def modifiedLinearSpectrum(Peptide):
    PrefixMass = [0] * (len(Peptide) + 1)
    for i in range(1, len(Peptide) + 1):
        PrefixMass[i] = PrefixMass[i - 1] + Peptide[i - 1]

    LinearSpectrumList = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrumList.append(PrefixMass[j] - PrefixMass[i])

    return sorted(LinearSpectrumList)


def isConsistent(Peptide, SpectrumDictionary, Alphabet, AminoAcidMass): 
    AminoAcidsList = [int(AminoAcids) for AminoAcids in Peptide.split("-")]
    LinearPeptide = modifiedLinearSpectrum(AminoAcidsList)
    PeptideDictionary = dict()
    for peptide in LinearPeptide:
        PeptideDictionary[peptide] = PeptideDictionary.get(peptide, 0) + 1

    for key, value in PeptideDictionary.items():
            if value > SpectrumDictionary.get(key, 0):
                return False
    
    return True


def modifiedCyclicSpectrum(Peptide):
    PrefixMass = [0] * (len(Peptide) + 1)
    for i in range(1, len(Peptide) + 1):
        PrefixMass[i] = PrefixMass[i - 1] + Peptide[i - 1]

    peptideMass = PrefixMass[len(Peptide)]
    CyclicSpectrumList = [0]

    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            CyclicSpectrumList.append(PrefixMass[j] - PrefixMass[i])
            if i > 0 and j < len(Peptide):
                CyclicSpectrumList.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))

    return sorted(CyclicSpectrumList)

def isConsistentCycloSpectrum(Peptide, SpectrumDictionary, Alphabet, AminoAcidMass):
    AminoAcidsList = [int(AminoAcids) for AminoAcids in Peptide.split("-")]
    CycloPeptide = modifiedCyclicSpectrum(AminoAcidsList)
    PeptideDictionary = dict()
    for peptide in CycloPeptide:
        PeptideDictionary[peptide] = PeptideDictionary.get(peptide, 0) + 1

    if PeptideDictionary == SpectrumDictionary:
        return True
    
    return False

def CyclopeptideSequencing(Spectrum):
    f_amino = open("integer_mass_table.txt", "r")
    f_amino_text = f_amino.read()
    Alphabet, AminoAcidMass = GenerateAminoAcidMass(f_amino_text)
    Masses = list(set(AminoAcidMass.values()))

    SpectrumValues = list(map(int, Spectrum.strip().split()))
    ParentMass = max(SpectrumValues)
    SpectrumDictionary = {}
    for mass in SpectrumValues:
        SpectrumDictionary[mass] = SpectrumDictionary.get(mass, 0) + 1

    CandidatePeptides = {""}
    FinalPeptides = []

    while len(CandidatePeptides) > 0:
        CandidatePeptides = Expand(CandidatePeptides, Masses)
        deletions = []
        for Peptide in CandidatePeptides:
            if Mass(Peptide) == ParentMass:
                if isConsistentCycloSpectrum(Peptide, SpectrumDictionary, Alphabet, AminoAcidMass) and Peptide not in FinalPeptides:
                    FinalPeptides.append(Peptide)
                deletions.append(Peptide)
            elif not isConsistent(Peptide, SpectrumDictionary, Alphabet, AminoAcidMass):
                deletions.append(Peptide)
            
        for deletion in deletions:
            CandidatePeptides.remove(deletion)

    return FinalPeptides

if __name__ == "__main__":
    file_input = open("/home/swativ5/Downloads/dataset_30217_6.txt", "r")
    file_input_text = file_input.read()
    Spectrum = file_input_text.strip()
    # Spectrum = "0 113 128 186 241 299 314 427"
    FinalPeptides = CyclopeptideSequencing(Spectrum)
    f = open("test.txt", "w")
    f.write(" ".join(sorted(FinalPeptides, reverse = True)))
