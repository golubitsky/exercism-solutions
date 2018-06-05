def to_rna(dna_strand):
    convert = {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'U'
    }

    if any(char not in convert for char in dna_strand):
        raise ValueError(f"Can only convert {convert.keys()}")
    
    return "".join(list(map(lambda char:convert[char], dna_strand)))