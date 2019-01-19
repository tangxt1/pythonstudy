"""
This is my first python program.
It computes the GC content of a DNA sequence.
"""
# get DNA sequence:
dna = 'atgccgtattggaacccccttgaagtcc'
no_c = dna.count('c')  
no_g = dna.count('g')
dna_length=len(dna)
gc_percent=(no_c+no_g)*100.0/dna_length  #compoute gc percentage
print(gc_percent)   #print GC% to screen
