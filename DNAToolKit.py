
Nucleotides = ["A", "C", "G", "T"]

def validateStr(dna_seq):
    tempseq = dna_seq.upper()
    for nuc in tempseq:
        if nuc not in Nucleotides:
            return False
    return tempseq


def countNucFreq(seq):
    tempFreqdict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tempFreqdict[nuc] += 1
    return tempFreqdict

