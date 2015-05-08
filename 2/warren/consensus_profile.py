from sys import argv
from collections import Counter
import string
def consensus_profile(dna_strings):
    counters = map(Counter, zip(*dna_strings))
    consensus = "".join(base_counts.most_common(1)[0][0] for base_counts in counters)
    profile_matrix = "\n".join(base + ": " + " ".join(str(count[base]) for count in counters) for base in "ACGT")
    return consensus + "\n" + profile_matrix

with open(argv[1]) as f:
    s = f.read()

    bad_chars = '>Rosalind0123456789'
    strings = ""
    for item in s.translate(string.maketrans("","",),bad_chars):
        strings += item.strip("\n")
    dna = strings.split("_")[1:]

    print consensus_profile(dna)
