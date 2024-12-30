import DNAToolKit as dna
import random 


randDNAStr = ''.join([random.choice(dna.Nucleotides) for nuc in range(50)])

print(dna.validateStr(randDNAStr))
print(dna.countNucFreq(randDNAStr))