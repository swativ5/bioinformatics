"""
Exercise Break: Generate the (3,2)-mer composition of TAATGCCATGGGATGTT in lexicographic order.
Include repeats, and return your answer as a list on a single line.
As a hint to help you with formatting, your answer should begin "(AAT|CAT) (ATG|ATG)..."
"""

def generate_composition(k, d, Text):
    kmers = []
    for i in range(len(Text) - (2 * k + d) + 1):
        kmers.append([Text[i : i + k], Text[i + k + d: i + 2 * k + d]])

    kmers.sort()
    return " ".join(f"({p[0]}|{p[1]})" for p in kmers)
if __name__ == "__main__":
    string = "TAATGCCATGGGATGTT"
    print(generate_composition(3, 2, string))
